FROM nginx:latest

RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled
COPY *.conf /etc/nginx/conf.d/

RUN apt update -y && apt upgrade -y

RUN apt install python3 python3-certbot -y

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Copy the startup script
COPY nginx_startup.sh /usr/local/bin/

# Ensure the script is executable
RUN chmod +x /usr/local/bin/nginx_startup.sh
