import json
import logging
import paho.mqtt.client as mqtt
import requests

# broker connection details
broker = "opencdms-broker"
protocol = "MQTT"
port = 1883
uid = "opencdms"
pwd = "insecure-change-me"

# OGC-API Process endpoint
API = "http://opencdms-api:5000"
logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def on_connect(client, userdata, flags, rc):
    LOGGER.debug(f"Connected")
    for t in userdata['topics']:
        LOGGER.debug(f"Subscribing to {t}")
        try:
            client.subscribe(t)
            LOGGER.debug(f"Subscribed to {t}")
        except Exception as e:
            LOGGER.error(f"Error subscribing to topic {t}")
            LOGGER.error(e)


def on_message(client, userdata, msg):
    LOGGER.debug("New message received")
    topic = msg.topic
    payload = json.loads(msg.payload)
    LOGGER.debug(json.dumps(payload, indent=4))
    bucket = None
    obj = None
    if topic == 'fs':  # we have minio message
        LOGGER.debug("fs")
        # make sure we have Put event
        if payload['EventName'] == "s3:ObjectCreated:Put":
            # iterate over records
            for record in payload['Records']:
                received = record['eventTime']
                user = record['userIdentity']
                bucket = record['s3']['bucket']['name']
                obj = record['s3']['object']['key']
        else:
            LOGGER.warning(f"Unrecognised event {payload['EventName']}, ignored")  # noqa

        if None not in [bucket, obj]:
            request_inputs = {
                "mode": "sync",
                "inputs": {
                    "path": bucket,
                    "object": obj,
                },
                "outputs": {}
            }
            processor = "cdm"
            request_url = f'{API}/processes/{processor}/execution'
            # POST request
            LOGGER.debug(f"{request_url}")
            LOGGER.debug(f"{request_inputs}")
            r = requests.post(request_url, json=request_inputs)
            LOGGER.debug(r.text)
        else:
            LOGGER.debug(f"Bucket {bucket} or object {obj} is missing")
    else:
        LOGGER.debug(f"Topic {topic} ignored")


def load_config():
    pass


'''
Table to manage processes
id: autoincrement?
topic: 
path/prefix: path in bucket, regex on object
active: true|false
processor: name of pygeoapi process
inputs: json string with inputs to process (in addition to bucket)
last_run:
status:
output_target:
publish on receipt
'''


def update_scheduler():
    pass


# create new client
client = mqtt.Client(userdata={'topics': ['fs/#']})
# set up connection parameters
client.username_pw_set(uid, pwd)
# callbacks
client.on_connect = on_connect
client.on_message = on_message
# now connect
LOGGER.debug("Connecting")
client.connect(host=broker, port=port)
LOGGER.debug("Connected")
client.loop_forever()
