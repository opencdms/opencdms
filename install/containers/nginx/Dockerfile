FROM nginx:latest

RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled
COPY *.conf /etc/nginx/conf.d/

RUN apt update -y && apt upgrade -y

# apt version of certbot is old. It's also difficult to run snap in
# debian:11-slim because systemd is not running, therefore use pip
RUN apt install python3 python3-pip -y
RUN pip install --upgrade pip && pip install certbot

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Copy the startup script
COPY nginx_startup.sh /usr/local/bin/

# Ensure the script is executable
RUN chmod +x /usr/local/bin/nginx_startup.sh
