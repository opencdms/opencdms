
export PYGEOAPI_CONFIG=pygeoapi-config.yml
export PYGEOAPI_OPENAPI=openapi-config.yml
pygeoapi openapi generate $PYGEOAPI_CONFIG --output-file $PYGEOAPI_OPENAPI

After generating openapi-config.yml (using `opencdms api openapi generate` or
`pygeoapi openapi generate`) we are currently adding the following lines to
openapi-config.yml manually:

NOTE: When the additions below are automatically generated then we can also
      add RBAC to openapi doc at the same time.

```
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  security:
    - bearerAuth: []
```

```
openapi: 3.0.2
paths:
  /login:
    post:
      summary: User login
      description: Generates a bearer token
      operationId: loginUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
              required:
                - username
                - password
      responses:
        '200':
          description: Successful login
          content:
            application/json:
              schema:
                type: object
                properties:
                  token:
                    type: string
      tags:
        - Authentication

```
