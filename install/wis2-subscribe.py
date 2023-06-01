import base64
from datetime import datetime as dt
import json
import os
import paho.mqtt.client as mqtt
from pathlib import Path
import queue
import requests
import ssl
import threading
import logging

from urllib.parse import urlparse


# define queue for storing downloads
urlQ = queue.Queue()

LOGGER = logging.getLogger(__name__)

# define worker to do the downloads
def downloadWorker():
    while True:
        job = urlQ.get() # get latest job from queue
        key = job["key"]
        #filename = job["filename"]
        url_ = job["url"]
        # download the data
        try:
            r = requests.get(url_, verify=False)
            LOGGER.error(url_)
        except Exception as e:
            LOGGER.error(e)
        urlQ.task_done()


# now MQTT functions etc
def on_connect(client, userdata, flags, rc):
    LOGGER.error("connected")
    # subscribe to default topics
    for topic in default_topics:
        LOGGER.error(f"subscribing to {topic}")
        client.subscribe(topic)


def on_message(client, userdata, msg):
    LOGGER.error("message received")
    # get time of receipt
    receipt_time = dt.now().isoformat()
    # parse message
    parsed_message = json.loads(msg.payload)
    topic = msg.topic
    url_ = None
    publish_time = parsed_message['properties']['pubtime']
    observation_time = parsed_message['properties']['datetime']
    hash = parsed_message['properties']['integrity']['value']
    hash_method = parsed_message['properties']['integrity']['method']
    for link in parsed_message['links']:
        LOGGER.error(link)
        if (link.get('rel', None) == 'canonical') and (link.get('type', None) == 'application/x-bufr'):
            url_ = link.get('href', None)
            LOGGER.error(url_)

    if url_ is not None:
        job = {
            'key': hash,
            'url': url_,
            'topic': topic,
            'publish_time': publish_time,
            'receipt_time': receipt_time,
            'observation_time': observation_time,
            'hash': hash,
            'hash_method': hash_method
        }
        LOGGER.error(job)
        urlQ.put(job)


# start worker in the background
LOGGER.error("Spawning worker")
threading.Thread(target=downloadWorker, daemon=True).start()


LOGGER.error("Loading MQTT config")
broker = 'globalbroker.meteo.fr'
port = 443
pwd = "anonymous"
uid = "anonymous"
protocol = "ws"
#default_topics = ["origin/a/wis2/mwi/#"]
default_topics = ["origin/a/wis2/swe/#",
                  "origin/a/wis2/usa/#",
                  "origin/a/wis2/mwi/#"]

LOGGER.error("Initialising client")
client = mqtt.Client(transport="websockets")
client.tls_set(ca_certs=None, certfile=None, keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLS,
               ciphers=None)
client.username_pw_set(uid, pwd)
client.on_connect = on_connect
client.on_message = on_message
LOGGER.error("Connecting")
result = client.connect(host=broker, port=port)
LOGGER.error("Looping forever")
client.loop_forever()
