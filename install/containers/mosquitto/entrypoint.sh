#!/bin/sh
mosquitto_passwd -b -c /mosquitto/config/password.txt $OPENCDMS_BROKER_USERNAME $OPENCDMS_BROKER_PASSWORD
mosquitto_passwd -b /mosquitto/config/password.txt everyone everyone

sed -i "s#_OPENCDMS_BROKER_QUEUE_MAX#$OPENCDMS_BROKER_QUEUE_MAX#" /mosquitto/config/mosquitto.conf
sed -i "s#_OPENCDMS_BROKER_USERNAME#$OPENCDMS_BROKER_USERNAME#" /mosquitto/config/acl.conf

/usr/sbin/mosquitto -c /mosquitto/config/mosquitto.conf