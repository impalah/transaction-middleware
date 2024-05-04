# transaction-middleware

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
from transaction_middleware import (
    TransactionMiddleware,
    get_transaction_id,
    transaction_id_required,
)

app: FastAPI = FastAPI()
app.add_middleware(TransactionMiddleware)

@app.get(
    "/items/{id}",
    tags=["Item"],
)
async def read_items(
    request: Request,
    response: Response,
    id: str,
    transaction_id: str = Depends(get_transaction_id()),
):
    return {
        "id": id,
        "transaction_id": transaction_id if transaction_id else "No transaction ID",
    }


```

Then set the environment variables (or your .env file)

```bash
TRANSACTION_MIDDLEWARE_LOG_LEVEL=DEBUG
TRANSACTION_MIDDLEWARE_HEADER=X-Transaction-ID

```

Launch the server.

Call the method you want to test, and, optionally, set the transaction Id on the headers.

```bash
curl -X GET http://localhost:8000/items/1234 -H "X-Transaction-ID: 2fyJr1FbRj603pH4rweEfEzQ"
```


## Middleware configuration

The middleware configuration is done by environment variables (or using and .env file if your project uses python-dotenv).

The main variables are shown in the table below:

| Name | Description | Values | Default |
| --------- | --------- | --------- | --------- |
| TRANSACTION_MIDDLEWARE_LOG_LEVEL | Log level for the application | DEBUG, INFO, WARNING, ERROR, CRITICAL | INFO |
| TRANSACTION_MIDDLEWARE_LOG_FORMAT | Log format | See python logger documentation | %(log_color)s%(levelname)-9s%(reset)s %(asctime)s %(name)s %(message)s |
| TRANSACTION_MIDDLEWARE_HEADER | Name for the header | Any String | X-Transaction-ID |



