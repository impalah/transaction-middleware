User Guide
==========

Transaction Middleware follows the middleware protocol and, therefore, should be added as a middleware to your FastApi or Starlette application.

The steps, using FastAPI:

First, create the code to include the middleware and the endpoints you want to test.

.. code-block:: python

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

Then, optionally, set the environment variables (or your .env file).

.. code-block:: bash

   TRANSACTION_MIDDLEWARE_LOG_LEVEL=DEBUG
   TRANSACTION_MIDDLEWARE_HEADER=X-Transaction-ID

Launch the server.

Call the method you want to test, and, optionally, set the transaction Id on the headers.

.. code-block:: bash

   curl -X GET http://localhost:8000/items/1234 -H "X-Transaction-ID: 2fyJr1FbRj603pH4rweEfEzQ"
