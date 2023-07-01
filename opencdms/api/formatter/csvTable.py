# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2022 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import io
import logging

import unicodecsv as csv

from pygeoapi.formatter.base import BaseFormatter, FormatterSerializationError

LOGGER = logging.getLogger(__name__)


class CSVFormatter(BaseFormatter):
    """CSV formatter"""

    def __init__(self, formatter_def: dict):
        """
        Initialize object

        :param formatter_def: formatter definition

        :returns: `pygeoapi.formatter.csv_.CSVFormatter`
        """

        geom = False
        if 'geom' in formatter_def:
            geom = formatter_def['geom']

        super().__init__({'name': 'csv', 'geom': geom})
        self.mimetype = 'text/csv; charset=utf-8'

    def write(self, options: dict = {}, data: dict = None) -> str:
        """
        Generate data in CSV format

        :param options: CSV formatting options
        :param data: dict of GeoJSON data

        :returns: string representation of format
        """

        is_point = False
        try:
            fields = list(data['items'][0].keys())
        except IndexError:
            LOGGER.error('no features')
            return str()

        LOGGER.debug(f'CSV fields: {fields}')

        try:
            output = io.BytesIO()
            writer = csv.DictWriter(output, fields)
            writer.writeheader()

            for item in data['items']:
                writer.writerow(item)

        except ValueError as err:
            LOGGER.error(err)
            raise FormatterSerializationError('Error writing CSV output')

        return output.getvalue()

    def __repr__(self):
        return f'<CSVFormatter> {self.name}'
