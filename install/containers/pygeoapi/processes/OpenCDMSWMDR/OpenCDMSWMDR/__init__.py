###############################################################################
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
###############################################################################
__version__ = "0.0.1"

import json
import logging
from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
from lxml import etree
import urllib3
import os.path

LOGGER = logging.getLogger(__name__)

PROCESS_METADATA = {
    'version': '0.0.1',
    'id': 'OpenCDMSWMDR',
    'title': {
        'en': 'ingestHost',
    },
    'description': {
        'en': 'Process to ingest WMDR host / station into CDMS',
    },
    'keywords': [],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'WIGOS_identifier': {
            'title': 'WIGOS Identifier',
            'description': 'Station to ingest',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': []
        }
    },
    'outputs': {
        'status': {
            'title': 'Status of request',
            'schema': {
                'type': 'numeric'
            }
        }

    },
    'example': {
        'inputs': {
            "WIGOS_identifier": "0-0-0-A1"
        },
        'outputs':{
            "status": 200
        }
    }
}


THISDIR = os.path.dirname(os.path.realpath(__file__))
MAPPINGS = f"{THISDIR}{os.sep}transforms"

class ingestHost(BaseProcessor):

    def __init__(self, processor_def):
        """
        Initialize object
        :param processor_def: provider definition
        :returns: pygeoapi.process.OpenCDMSWMDR.ingestHost
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        mimetype = 'application/json'
        wsi = data.get("WIGOS_identifier", None)
        if wsi is None:
            output = {
                "status": 400,
                "msg": "Invalid identifier"
            }
            return mimetype, output

        http = urllib3.PoolManager()

        # first check if we already have the station
        api = "http://localhost:5000/collections/stations/items"
        resp = http.request("GET", f"{api}/{wsi}?f=json")
        resp = json.loads(resp.data)
        if resp.get('code', 'recordExists') == 'recordExists':
            output = {
                "status": 409,
                "msg":  "Record with matching identifer already ingested"
            }
            return mimetype, output

        # First we need to fetch the metadata record from OSCAR Surface
        oscar_url = "https://oscar.wmo.int/surface/rest/api"
        url_ = f"{oscar_url}/wmd/download/{wsi}"
        resp = http.request("GET", url_)
        # check status
        if resp.status != 200:
            status = resp.status
            output = {
                "status": status,
                "msg": resp.msg
            }
            return mimetype, output
        xml = resp.data
        xml_root = etree.fromstring(xml)
        # load transform
        with open(f"{MAPPINGS}{os.sep}wmdr_to_json.xslt") as fh:
            xslt = fh.read()
        xslt_root = etree.fromstring(bytes(xslt,encoding="utf8"))
        # apply transform
        transform = etree.XSLT(xslt_root)
        t = str(transform(xml_root))
        # replace any empty strings with null
        t = t.replace('""','null').replace("\n","")
        # parse to and from JSON, despite being valid json an
        # exception is raised without doing this
        obj = json.loads(t)
        # upload data
        resp = http.request(
            "POST",
            "http://localhost:5000/collections/stations/items",
            body = json.dumps(obj),
            headers={
                "Content-Type": "application/geo+json"
            }
        )
        # return response status
        output = {
            "status": resp.status
        }

        return mimetype, output

    def __repr__(self):
        return '<ingestHost> {}'.format(self.name)


def str_to_geojson():
    pass