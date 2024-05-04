# FastAPI Cognito Demo

Testing transaction middleware with fastapi.


## API server

### Create a configuration file

Rename or copy ".env.template" file to ".env" and set the values according with the data returned by terraform.

```bash

TRANSACTION_MIDDLEWARE_LOG_LEVEL=DEBUG
TRANSACTION_MIDDLEWARE_HEADER=X-Tranaction-ID

```

### Launch server

From the root folder launch the command:

```bash
poetry run dotenv run python -m uvicorn demo.main:app --host 0.0.0.0 --port 8000 --reload
```

("run dotenv" allows python to read and decode the .env file)



## Test the server

### Main page

- Access [http://localhost:8000](http://localhost:8000)

