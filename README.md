# auth-middleware

Async Transaction Middleware for FastAPI/Starlette.

## Installation

Using pip:

```bash
pip install transaction-middleware
```

Using poetry

```bash
poetry add transaction-middleware
```


## How to use it

Transaction Middleware follows the middleware protocol and, therefore, should be added as a middleware to your FastApi or Starlette application.

The steps, using FastAPI:

```python

from fastapi import FastAPI, Depends

from starlette.requests import Request
from starlette.responses import Response


```

Then set the environment variables (or your .env file)

```bash

```

Call the method

```bash
curl -X GET http://localhost:8000/ -H "Authorization: Bearer MY_ID_TOKEN"
```


## Middleware configuration

The middleware configuration is done by environment variables (or using and .env file if your project uses python-dotenv).

The main variables are shown in the table below:

| Name | Description | Values | Default |
| --------- | --------- | --------- | --------- |
| TRANSACTION_MIDDLEWARE_LOG_LEVEL | Log level for the application | DEBUG, INFO, WARNING, ERROR, CRITICAL | INFO |
| TRANSACTION_MIDDLEWARE_LOG_FORMAT | Log format | See python logger documentation | %(log_color)s%(levelname)-9s%(reset)s %(asctime)s %(name)s %(message)s |
| TRANSACTION_MIDDLEWARE_DISABLED | Transaction middleware enabled/disabled | false, true | false |



