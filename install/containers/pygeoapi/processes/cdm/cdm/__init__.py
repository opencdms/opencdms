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

import logging
from minio import Minio
import os
from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from opencdms.adapters import opencdmsdb

LOGGER = logging.getLogger(__name__)

# Get connection details
UID = os.environ["POSTGRES_USER"]
PWD = os.environ["POSTGRES_PASSWORD"]
DBNAME = os.environ["POSTGRES_DB"]
DBHOST = os.environ["POSTGRES_HOST"]
DBPORT = os.environ["POSTGRES_PORT"]

PROCESS_METADATA = {
    'version': '0.0.1',
    'id': 'cdm',
    'title': {
        'en': 'import_observations',
    },
    'description': {
        'en': 'Process to ingest CDM formatted observations',
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
        'example_input': {
            'title': 'value',
            'description': 'Number to double',
            'schema': {
                'type': 'numeric'
            },
            'minOccurs': 1,
            'maxOccurs': 1,
            'metadata': None,
            'keywords': []
        }
    },
    'outputs': { },
    'example': {
        'inputs': {
            "value": 5
        },
        'outputs':{
            "result": 10
        }
    }
}


class import_observations(BaseProcessor):

    def __init__(self, processor_def):
        """
        Initialize object
        :param processor_def: provider definition
        :returns: pygeoapi.process.cdm.import_observations
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):
        mimetype = 'application/json'
        value = data.get("example_input", None)

        # first get minio connect
        client = Minio("opencdms-bucket:9000",
                       access_key="opencdms",
                       secret_key="insecure-change-me",
                       secure=False)

        # get names of bucket and data we want to read
        bucket = data.get("path", None)
        obj = data.get("object", None)
        handle = client.get_object(bucket, obj)

        # get other file settings
        header = data.get("header", 'HEADER')
        delimiter = data.get("delimiter", '|')
        null = data.get("null", 'NA')
        quote = data.get("quote", "E'\b'")

        # now DB connect
        engine = create_engine(
            f"postgresql+psycopg2://{UID}:{PWD}@{DBHOST}:{DBPORT}/{DBNAME}",
            echo=True)
        # start the mappers
        try:
            opencdmsdb.start_mappers()
        except Exception as e:
            LOGGER.error(e)
        # get the session
        session = sessionmaker(bind=engine)()
        # now we want to use cursor for bulk upload
        cursor = session.connection().connection.cursor()
        with handle as fh:
            cursor.copy_expert(f"COPY cdm.observation FROM STDIN WITH CSV {header} DELIMITER AS '{delimiter}' NULL AS '{null}' QUOTE {quote}", fh)  # noqa
        # commit and close session
        session.commit()
        session.close()

        output = {
            "result": "success"
        }
        return mimetype, output


    def __repr__(self):
        return '<import_observations> {}'.format(self.name)