## Creating openapi-config.yml

```
export PYGEOAPI_CONFIG=pygeoapi-config.yml
export PYGEOAPI_OPENAPI=openapi-config.yml

# Use either pygeoapi or opencdms command line interface
opencdms api openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI
```
