from pygeoapi.api import *


class APIExtended(API):
    def get_vocabularies_url(self):
         return f"{self.base_url}/vocabularies"

    @gzip
    @pre_process
    @jsonldify
    def describe_vocabularies(self, request: Union[APIRequest, Any],
                            vocab=None) -> Tuple[dict, int, str]:
        """
        Provide vocabulary metadata

        :param request: A request object
        :param vocab: vocab identifier, defaults to None to obtain
                        information about all vocabularies

        :returns: tuple of headers, status code, content
        """

        if not request.is_valid():
            return self.get_format_exception(request)
        headers = request.get_response_headers()

        fcm = {
            'vocabularies': [],
            'links': []
        }

        vocabularies = filter_dict_by_key_value(self.config['resources'],
                                                'type', 'vocabulary')

        if all([vocab is not None, vocab not in vocabularies.keys()]):
            msg = 'Vocabulary not found'
            return self.get_exception(
                HTTPStatus.NOT_FOUND, headers, request.format, 'NotFound', msg)

        if vocab is not None:
            vocabularies_dict = {
                key: value for key, value in vocabularies.items() if
                key == vocab
                # noqa
            }
        else:
            vocabularies_dict = vocabularies

        LOGGER.debug("Creating vocabularies")

        for key, value in vocabularies_dict.items():
            vocab_data = get_provider_default(value['providers'])
            vocab_data_type = vocab_data['type']
            vocab_data_format = None

            if 'format' in vocab_data:
                vocab_data_format = vocab_data['format']

            LOGGER.debug(value)

            vocab_ = {
                'id': key,
                'title': l10n.translate(value['title'], request.locale),
                'description': l10n.translate(value['description'],
                                            request.locale),  # noqa
                'links': []
            }

            LOGGER.debug('Processing configured vocabulary links')
            for link in l10n.translate(value['links'], request.locale):
                lnk = {
                    'type': link['type'],
                    'rel': link['rel'],
                    'title': l10n.translate(link['title'], request.locale),
                    'href': l10n.translate(link['href'], request.locale),
                }
                if 'hreflang' in link:
                    lnk['hreflang'] = l10n.translate(
                        link['hreflang'], request.locale)
                content_length = link.get('length', 0)
                if content_length > 0:
                    lnk['length'] = content_length

                vocab_['links'].append(lnk)

            # TODO: provide translations
            LOGGER.debug('Adding JSON and HTML link relations')
            vocab_['links'].append({
                'type': FORMAT_TYPES[F_JSON],
                'rel': 'root',
                'title': 'The landing page of this server as JSON',
                'href': f"{self.base_url}?f={F_JSON}"
            })
            vocab_['links'].append({
                'type': FORMAT_TYPES[F_HTML],
                'rel': 'root',
                'title': 'The landing page of this server as HTML',
                'href': f"{self.base_url}?f={F_HTML}"
            })
            vocab_['links'].append({
                'type': FORMAT_TYPES[F_JSON],
                'rel': request.get_linkrel(F_JSON),
                'title': 'This document as JSON',
                'href': f'{self.get_vocabularies_url()}/{key}?f={F_JSON}'
            })
            vocab_['links'].append({
                'type': FORMAT_TYPES[F_JSONLD],
                'rel': request.get_linkrel(F_JSONLD),
                'title': 'This document as RDF (JSON-LD)',
                'href': f'{self.get_vocabularies_url()}/{key}?f={F_JSONLD}'
            })
            vocab_['links'].append({
                'type': FORMAT_TYPES[F_HTML],
                'rel': request.get_linkrel(F_HTML),
                'title': 'This document as HTML',
                'href': f'{self.get_vocabularies_url()}/{key}?f={F_HTML}'
            })

            if vocab is not None and key == vocab:
                fcm = vocab_
                break

            fcm['vocabularies'].append(vocab_)

        if vocab is None:
            vocabulary_url = self.get_vocabularies_url()
            response = {
                'vocabularies': vocabularies,
                'links': [{
                    'type': FORMAT_TYPES[F_JSON],
                    'rel': request.get_linkrel(F_JSON),
                    'title': 'This document as JSON',
                    'href': f'{vocabulary_url}?f={F_JSON}'
                }, {
                    'type': FORMAT_TYPES[F_JSONLD],
                    'rel': request.get_linkrel(F_JSONLD),
                    'title': 'This document as RDF (JSON-LD)',
                    'href': f'{vocabulary_url}?f={F_JSONLD}'
                }, {
                    'type': FORMAT_TYPES[F_HTML],
                    'rel': request.get_linkrel(F_HTML),
                    'title': 'This document as HTML',
                    'href': f'{vocabulary_url}?f={F_HTML}'
                }]
            }

        if request.format == F_HTML:  # render
            fcm['vocabularies_path'] = self.get_vocabularies_url()
            if vocab is not None:
                response = render_j2_template(self.tpl_config,
                                            'vocabularies/vocabulary.html',
                                            fcm, request.locale)
            else:
                response = render_j2_template(self.tpl_config,
                                            'vocabularies/index.html', fcm,
                                            request.locale)

            return headers, HTTPStatus.OK, response

        # ToDo - add F_JSONLD format

        return headers, HTTPStatus.OK, to_json(fcm, self.pretty_print)

    @gzip
    @pre_process
    def get_vocabulary_items(
            self, request: Union[APIRequest, Any],
            vocab) -> Tuple[dict, int, str]:
        """
        Queries vocabulary

        :param request: A request object
        :param vocab: vocabulary name

        :returns: tuple of headers, status code, content
        """

        if not request.is_valid(PLUGINS['formatter'].keys()):
            return self.get_format_exception(request)

        # Set Content-Language to system locale until provider locale
        # has been determined
        headers = request.get_response_headers(SYSTEM_LOCALE,
                                            **self.api_headers)
        properties = []
        reserved_fieldnames = ['bbox', 'bbox-crs', 'crs', 'f', 'lang', 'limit',
                            'offset', 'resulttype', 'datetime', 'sortby',
                            'properties', 'skipGeometry', 'q',
                            'filter', 'filter-lang']

        vocabularies = filter_dict_by_key_value(self.config['resources'],
                                                'type', 'vocabulary')

        if vocab not in vocabularies.keys():
            msg = 'vocabulary not found'
            return self.get_exception(
                HTTPStatus.NOT_FOUND, headers, request.format, 'NotFound', msg)

        LOGGER.debug('Processing query parameters')

        LOGGER.debug('Processing offset parameter')
        try:
            offset = int(request.params.get('offset'))
            if offset < 0:
                msg = 'offset value should be positive or zero'
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'InvalidParameterValue', msg)
        except TypeError as err:
            LOGGER.warning(err)
            offset = 0
        except ValueError:
            msg = 'offset value should be an integer'
            return self.get_exception(
                HTTPStatus.BAD_REQUEST, headers, request.format,
                'InvalidParameterValue', msg)

        LOGGER.debug('Processing limit parameter')
        try:
            limit = int(request.params.get('limit'))
            # TODO: We should do more validation, against the min and max
            #       allowed by the server configuration
            if limit <= 0:
                msg = 'limit value should be strictly positive'
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'InvalidParameterValue', msg)
        except TypeError as err:
            LOGGER.warning(err)
            limit = int(self.config['server']['limit'])
        except ValueError:
            msg = 'limit value should be an integer'
            return self.get_exception(
                HTTPStatus.BAD_REQUEST, headers, request.format,
                'InvalidParameterValue', msg)

        resulttype = request.params.get('resulttype') or 'results'

        datetime_ = ''
        if 'extents' in vocabularies[vocab]:
            LOGGER.debug('Processing datetime parameter')
            datetime_ = request.params.get('datetime')
            try:
                datetime_ = validate_datetime(vocabularies[vocab]['extents'],
                                            datetime_)
            except ValueError as err:
                msg = str(err)
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'InvalidParameterValue', msg)

        LOGGER.debug('processing q parameter')
        q = request.params.get('q') or None

        LOGGER.debug('Loading provider')

        try:
            provider_def = get_provider_by_type(
                vocabularies[vocab]['providers'], 'feature')
            p = load_plugin('provider', provider_def)
        except ProviderTypeError:
            try:
                provider_def = get_provider_by_type(
                    vocabularies[vocab]['providers'], 'record')
                p = load_plugin('provider', provider_def)
            except ProviderTypeError:
                msg = 'Invalid provider type'
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'NoApplicableCode', msg)
        except ProviderConnectionError:
            msg = 'connection error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)
        except ProviderQueryError:
            msg = 'query error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)

        LOGGER.debug('processing property parameters')
        for k, v in request.params.items():
            if k not in reserved_fieldnames and k in list(p.fields.keys()):
                LOGGER.debug(f'Adding property filter {k}={v}')
                properties.append((k, v))

        LOGGER.debug('processing sort parameter')
        val = request.params.get('sortby')

        if val is not None:
            sortby = []
            sorts = val.split(',')
            for s in sorts:
                prop = s
                order = '+'
                if s[0] in ['+', '-']:
                    order = s[0]
                    prop = s[1:]

                if prop not in p.fields.keys():
                    msg = 'bad sort property'
                    return self.get_exception(
                        HTTPStatus.BAD_REQUEST, headers, request.format,
                        'InvalidParameterValue', msg)

                sortby.append({'property': prop, 'order': order})
        else:
            sortby = []

        LOGGER.debug('processing properties parameter')
        val = request.params.get('properties')

        if val is not None:
            select_properties = val.split(',')
            properties_to_check = set(p.properties) | set(p.fields.keys())

            if (len(list(set(select_properties) -
                        set(properties_to_check))) > 0):
                msg = 'unknown properties specified'
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'InvalidParameterValue', msg)
        else:
            select_properties = []

        LOGGER.debug('processing filter parameter')
        filter_ = None

        # Get provider locale (if any)
        prv_locale = l10n.get_plugin_locale(provider_def, request.raw_locale)

        LOGGER.debug('Querying provider')
        LOGGER.debug(f'offset: {offset}')
        LOGGER.debug(f'limit: {limit}')
        LOGGER.debug(f'resulttype: {resulttype}')
        LOGGER.debug(f'sortby: {sortby}')
        LOGGER.debug(f'datetime: {datetime_}')
        LOGGER.debug(f'properties: {properties}')
        LOGGER.debug(f'select properties: {select_properties}')
        LOGGER.debug(f'language: {prv_locale}')
        LOGGER.debug(f'q: {q}')

        try:
            content = p.query(offset=offset, limit=limit,
                            resulttype=resulttype, properties=properties,
                            datetime_=datetime_, sortby=sortby,
                            select_properties=select_properties,
                            q=q, language=prv_locale)
            LOGGER.debug(content)
            # content is now a feature collection
        except ProviderConnectionError as err:
            LOGGER.error(err)
            msg = 'connection error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)
        except ProviderQueryError as err:
            LOGGER.error(err)
            msg = 'query error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)
        except ProviderGenericError as err:
            LOGGER.error(err)
            msg = 'generic error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)

        serialized_query_params = ''
        for k, v in request.params.items():
            if k not in ('f', 'offset'):
                serialized_query_params += '&'
                serialized_query_params += urllib.parse.quote(k, safe='')
                serialized_query_params += '='
                serialized_query_params += urllib.parse.quote(str(v), safe=',')

        # TODO: translate titles
        uri = f'{self.get_vocabularies_url()}/{vocab}/items'
        content['links'] = [{
            'type': 'application/json',
            'rel': request.get_linkrel(F_JSON),
            'title': 'This document as JSON',
            'href': f'{uri}?f={F_JSON}{serialized_query_params}'
        }, {
            'rel': request.get_linkrel(F_JSONLD),
            'type': FORMAT_TYPES[F_JSONLD],
            'title': 'This document as RDF (JSON-LD)',
            'href': f'{uri}?f={F_JSONLD}{serialized_query_params}'
        }, {
            'type': FORMAT_TYPES[F_HTML],
            'rel': request.get_linkrel(F_HTML),
            'title': 'This document as HTML',
            'href': f'{uri}?f={F_HTML}{serialized_query_params}'
        }]

        if offset > 0:
            prev = max(0, offset - limit)
            content['links'].append(
                {
                    'type': 'application/json',
                    'rel': 'prev',
                    'title': 'items (prev)',
                    'href': f'{uri}?offset={prev}{serialized_query_params}'
                })

        if len(content['items']) == limit:
            next_ = offset + limit
            content['links'].append(
                {
                    'type': 'application/json',
                    'rel': 'next',
                    'title': 'items (next)',
                    'href': f'{uri}?offset={next_}{serialized_query_params}'
                })

        content['links'].append(
            {
                'type': FORMAT_TYPES[F_JSON],
                'title': l10n.translate(
                    vocabularies[vocab]['title'], request.locale),
                'rel': 'vocabulary',
                'href': uri
            })

        # Set response language to requested provider locale
        # (if it supports language) and/or otherwise the requested pygeoapi
        # locale (or fallback default locale)
        l10n.set_response_language(headers, prv_locale, request.locale)

        if request.format == F_HTML:  # render
            # For constructing proper URIs to items

            content['items_path'] = uri
            content['vocab_path'] = '/'.join(uri.split('/')[:-1])
            content['vocabularies_path'] = self.get_vocabularies_url()

            content['offset'] = offset

            content['id_field'] = p.id_field
            if p.uri_field is not None:
                content['uri_field'] = p.uri_field
            if p.title_field is not None:
                content['title_field'] = l10n.translate(p.title_field,
                                                        request.locale)
                # If title exists, use it as id in html templates
                content['id_field'] = content['title_field']
            content = render_j2_template(self.tpl_config,
                                        'vocabularies/items/index.html',
                                        content, request.locale)
            return headers, HTTPStatus.OK, content
        elif request.format == 'csv':  # render
            formatter = load_plugin('formatter',
                                    {'name': 'CSVTable'})

            try:
                content = formatter.write(
                    data=content,
                    options={
                        'provider_def': get_provider_by_type(
                            vocabularies[vocab]['providers'],
                            'feature')
                    }
                )
            except FormatterSerializationError as err:
                LOGGER.error(err)
                msg = 'Error serializing output'
                return self.get_exception(
                    HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                    'NoApplicableCode', msg)

            headers['Content-Type'] = formatter.mimetype

            if p.filename is None:
                filename = f'{vocab}.csv'
            else:
                filename = f'{p.filename}'

            cd = f'attachment; filename="{filename}"'
            headers['Content-Disposition'] = cd

            return headers, HTTPStatus.OK, content

        elif request.format == F_JSONLD:
            msg = "JSON LD not implemented for vocabularies"
            raise NotImplementedError(msg)

        return headers, HTTPStatus.OK, to_json(content, self.pretty_print)

    @gzip
    @pre_process
    def get_vocabulary_item(self, request: Union[APIRequest, Any],
                            vocab, identifier) -> Tuple[dict, int, str]:
        """
        Get a single vocabulary item

        :param request: A request object
        :param vocab: vocab name
        :param identifier: item identifier

        :returns: tuple of headers, status code, content
        """

        if not request.is_valid():
            return self.get_format_exception(request)

        # Set Content-Language to system locale until provider locale
        # has been determined
        headers = request.get_response_headers(SYSTEM_LOCALE,
                                            **self.api_headers)
        LOGGER.debug('Processing query parameters')

        vocabularies = filter_dict_by_key_value(self.config['resources'],
                                                'type', 'vocabulary')

        if vocab not in vocabularies.keys():
            msg = 'vocabulary not found'
            return self.get_exception(
                HTTPStatus.NOT_FOUND, headers, request.format, 'NotFound', msg)

        LOGGER.debug('Loading provider')

        try:
            provider_def = get_provider_by_type(
                vocabularies[vocab]['providers'], 'feature')
            p = load_plugin('provider', provider_def)
        except ProviderTypeError:
            try:
                provider_def = get_provider_by_type(
                    vocabularies[vocab]['providers'], 'record')
                p = load_plugin('provider', provider_def)
            except ProviderTypeError:
                msg = 'Invalid provider type'
                return self.get_exception(
                    HTTPStatus.BAD_REQUEST, headers, request.format,
                    'InvalidParameterValue', msg)

        # Get provider language (if any)
        prv_locale = l10n.get_plugin_locale(provider_def, request.raw_locale)

        try:
            LOGGER.debug(f'Fetching id {identifier}')
            content = p.get(identifier, language=prv_locale)
        except ProviderConnectionError as err:
            LOGGER.error(err)
            msg = 'connection error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)
        except ProviderItemNotFoundError:
            msg = 'identifier not found'
            return self.get_exception(HTTPStatus.NOT_FOUND, headers,
                                    request.format, 'NotFound', msg)
        except ProviderQueryError as err:
            LOGGER.error(err)
            msg = 'query error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)
        except ProviderGenericError as err:
            LOGGER.error(err)
            msg = 'generic error (check logs)'
            return self.get_exception(
                HTTPStatus.INTERNAL_SERVER_ERROR, headers, request.format,
                'NoApplicableCode', msg)

        if content is None:
            msg = 'identifier not found'
            return self.get_exception(HTTPStatus.BAD_REQUEST, headers,
                                    request.format, 'NotFound', msg)

        uri = content['properties'].get(p.uri_field) if p.uri_field else \
            f'{self.get_vocabularies_url()}/{vocab}/items/{identifier}'

        if 'links' not in content:
            content['links'] = []
        if content['links'] is None:
            content['links'] = []

        content['links'].extend([{
            'type': FORMAT_TYPES[F_JSON],
            'rel': 'root',
            'title': 'The landing page of this server as JSON',
            'href': f"{self.base_url}?f={F_JSON}"
        }, {
            'type': FORMAT_TYPES[F_HTML],
            'rel': 'root',
            'title': 'The landing page of this server as HTML',
            'href': f"{self.base_url}?f={F_HTML}"
        }, {
            'rel': request.get_linkrel(F_JSON),
            'type': 'application/json',
            'title': 'This document as JSON',
            'href': f'{uri}?f={F_JSON}'
        }, {
            'rel': request.get_linkrel(F_JSONLD),
            'type': FORMAT_TYPES[F_JSONLD],
            'title': 'This document as RDF (JSON-LD)',
            'href': f'{uri}?f={F_JSONLD}'
        }, {
            'rel': request.get_linkrel(F_HTML),
            'type': FORMAT_TYPES[F_HTML],
            'title': 'This document as HTML',
            'href': f'{uri}?f={F_HTML}'
        }, {
            'rel': 'vocabulary',
            'type': FORMAT_TYPES[F_JSON],
            'title': l10n.translate(vocabularies[vocab]['title'],
                                    request.locale),
            'href': f'{self.get_vocabularies_url()}/{vocab}'
        }])

        if 'prev' in content:
            content['links'].append({
                'rel': 'prev',
                'type': FORMAT_TYPES[request.format],
                'href': f"{self.get_vocabularies_url()}/{vocab}/items/{content['prev']}?f={request.format}"
                # noqa
            })
        if 'next' in content:
            content['links'].append({
                'rel': 'next',
                'type': FORMAT_TYPES[request.format],
                'href': f"{self.get_vocabularies_url()}/{vocab}/items/{content['next']}?f={request.format}"
                # noqa
            })

        # Set response language to requested provider locale
        # (if it supports language) and/or otherwise the requested pygeoapi
        # locale (or fallback default locale)
        l10n.set_response_language(headers, prv_locale, request.locale)

        if request.format == F_HTML:  # render
            content['title'] = l10n.translate(vocabularies[vocab]['title'],
                                            request.locale)
            content['id_field'] = p.id_field
            if p.uri_field is not None:
                content['uri_field'] = p.uri_field
            if p.title_field is not None:
                content['title_field'] = l10n.translate(p.title_field,
                                                        request.locale)
            content['vocabularies_path'] = self.get_vocabularies_url()

            content = render_j2_template(self.tpl_config,
                                        'vocabularies/items/item.html',
                                        content, request.locale)
            return headers, HTTPStatus.OK, content

        elif request.format == F_JSONLD:
            msg = "JSONLD not yet implemented for vocab"
            raise NotImplementedError(msg)

        return headers, HTTPStatus.OK, to_json(content, self.pretty_print)
