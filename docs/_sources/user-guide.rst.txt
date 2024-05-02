User Guide
==========

Transaction Middleware follows the middleware protocol and, therefore, should be added as a middleware to your FastApi or Starlette application.

The steps, using FastAPI:

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


Then set the environment variables (or your .env file)

.. code-block:: bash

   TODO

Call the method sending the id_token provided by Cognito:

.. code-block:: bash

   curl -X GET http://localhost:8000/
