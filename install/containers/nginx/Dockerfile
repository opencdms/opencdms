FROM nginx:latest

RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.disabled
COPY nginx.conf /etc/nginx/conf.d/api.opencdms.org.conf

# Install Certbot and OpenSSL
RUN apt-get update \
    && apt-get install -y certbot python3-certbot-nginx openssl \
    && rm -rf /var/lib/apt/lists/*

# Create directory for SSL certificates
RUN mkdir -p /etc/nginx/ssl

# Generate self-signed certificates to allow nginx to start
# with standard configuration
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/nginx.key \
    -out /etc/nginx/ssl/nginx.crt \
    -subj "/C=UK/ST=Devon/L=Exeter/O=OpenCDMS/OU=e3s/CN=api.opencdms.org"

# Copy the startup script
COPY nginx_startup.sh /usr/local/bin/

# Ensure the script is executable
RUN chmod +x /usr/local/bin/nginx_startup.sh
