Example of using transaction-middleware
============

An example of using transaction-middleware with FastAPI is provided in the `examples` directory of the source code repository.

To run the example, follow these instructions:

1. Change to the `examples/fastapi` directory:

```bash
cd examples/fastapi
```

2. Install the required dependencies:

```bash
poetry install
```

3. Create an .env file with the following content:

```bash
TRANSACTION_MIDDLEWARE_LOG_LEVEL=DEBUG
TRANSACTION_MIDDLEWARE_HEADER=X-Transaction-ID
```

4. Run the example:

```bash
poetry run dotenv run python -m uvicorn demo.main:app --host 0.0.0.0 --port 8000 --reload
```

5. Open your browser and navigate to `http://localhost:8000/docs` to access the FastAPI Swagger UI.

6. Use the Swagger UI to test the `/items/{item_id}` endpoint. The transaction ID will be included in the response headers.

7. You can also use the `curl` command to test the endpoint:

```bash
curl -X 'GET' \
  'http://localhost:8000/items/1' \
  -H 'accept: application/json'
```

8. Check the logs to see the transaction ID being logged:

9. You can also include the transaction id header in the request:

```bash
curl -X 'GET' \
  'http://localhost:8000/items/1' \
  -H 'accept: application/json' \
  -H 'X-Transaction-ID: 123456'
```

The http methods you can test are:

- GET /items/{item_id} : Get an item by id and return the transaction id in the response headers. Transaction id will be created if it does not exists.
- GET /status/{item_id}: Get the status of an item by id and return the transaction id in the response headers. Transaction id will not be created if it does not exists.
- GET /simple/{item_id}: Get an item by id and return the transaction id in the response headers. Transaction id will be created and the tipe will be UUID4.

