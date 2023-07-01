FROM wmoim/dim_eccodes_baseimage:2.28.0

ENV TZ="Etc/UTC" \
    DEBIAN_FRONTEND="noninteractive" \
    PYGEOAPI_CONFIG="/config/pygeoapi-config.yml" \
    PYGEOAPI_OPENAPI="/config/openapi-config.yml" \
    DEBIAN_PACKAGES="cron bash vim git libffi-dev python3-cryptography libssl-dev libudunits2-0 python3-paho-mqtt python3-dateparser python3-tz python3-setuptools" \
    POSTGRES_USER=opencdms \
    POSTGRES_PASSWORD=insecure-change-me \
    POSTGRES_DB=opencdms \
    POSTGRES_HOST=opencdms-database \
    POSTGRES_PORT=5432

RUN echo "Acquire::Check-Valid-Until \"false\";\nAcquire::Check-Date \"false\";" | cat > /etc/apt/apt.conf.d/10no--check-valid-until \
    && apt-get update -y \
    && apt-get install -y ${DEBIAN_PACKAGES} \
    && apt-get install -y python3 python3-pip libpq-dev \
    && pip3 install --no-cache-dir click==8.1.3 \
    && pip3 install --no-cache-dir https://github.com/wmo-im/csv2bufr/archive/pygeoapi-debug.zip \
    && pip3 install --no-cache-dir https://github.com/opencdms/opencdms/archive/main-tmp.zip

WORKDIR /tmp
COPY requirements-providers.txt .
COPY processes/ /tmp/processes/

RUN pip3 install -r requirements-providers.txt

# Temporary workaround for https://github.com/geopython/pygeoapi/commit/6a871e8591d62a2af228c5fdca8a127a534c231a#commitcomment-120341690
RUN pip install git+https://github.com/geopython/pygeoapi.git@master

# Running setup directly (using easyinstall) is causing errors, switch to using pip
#RUN cd /tmp/processes/cdm && python3 setup.py install
#RUN cd /tmp/processes/OpenCDMSWMDR && python3 setup.py install
RUN cd /tmp/processes/ && pip install -e cdm
RUN cd /tmp/processes/ && pip install -e OpenCDMSWMDR

# clean up
RUN rm -R /tmp

ADD ./config /config

# create openapi config file (needs to be done after initilisation of DB, => commented out)
#RUN pygeoapi openapi generate $PYGEOAPI_CONFIG > $PYGEOAPI_OPENAPI
