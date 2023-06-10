#!/bin/bash
# This script uses Certbot to generate SSL certificates
# It assumes that Nginx is installed and configured on the same machine.
# The script also sets up a renewal cron job for the SSL certificates, which
# runs every 24 hours, and reloads Nginx to apply the renewed certificates.
DOMAIN=${DOMAIN:-*.opencdms.org}
EMAIL=${EMAIL:-info@opencdms.org}

mkdir -p /etc/nginx/ssl
mkdir -p /var/www/certbot
certbot certonly --webroot -w /var/www/certbot --agree-tos --no-eff-email --email $EMAIL -d $DOMAIN
cp /etc/letsencrypt/live/opencdms.org/fullchain.pem /etc/nginx/ssl/nginx.crt
cp /etc/letsencrypt/live/opencdms.org/privkey.pem /etc/nginx/ssl/nginx.key
# Restarting the service will stop the container, just reload instead
service nginx reload

# Run certbot daily
(crontab -l 2>/dev/null; echo "0 0 * * * certbot renew --webroot -w /var/www/certbot && cp /etc/letsencrypt/live/opencdms.org/fullchain.pem /etc/nginx/ssl/nginx.crt && cp /etc/letsencrypt/live/opencdms.org/privkey.pem /etc/nginx/ssl/nginx.key && service nginx reload") | crontab -
