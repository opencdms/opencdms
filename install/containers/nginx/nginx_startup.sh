#!/bin/bash
# On startup, we stop nginx service, if running, and use certbot in
# standalone mode (without nginx) to create the required certificates
# if they don't already exist in the shared volume.
#
# From then on, nginx runs as a background service.
#
# Since cron is not installed in the debian slim image we use a
# loop in foreground to check regularly whether certificates need
# renewing, switching to using --webroot with nginx for the renewal.
#
# This foreground loop prevents the container from exiting.
#
# The nginx image was already configured to redirect logs to stderr,
# (e.g. error.log -> /dev/stderr), so errors will be seen if the
# container is attached to terminal.
mkdir -p /etc/nginx/ssl
mkdir -p /var/www/certbot

service nginx stop
certbot certonly --standalone --non-interactive --agree-tos --no-eff-email $CERTBOT_CONFIG
service nginx start

while true; do
    sleep 12h & wait -n ${!}
    certbot renew --webroot -w /var/www/certbot --non-interactive
    service nginx reload
done
