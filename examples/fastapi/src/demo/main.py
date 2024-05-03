import os
from typing import Optional

from fastapi import Depends, FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import Response
from uvicorn import run

from transaction_middleware import (
    TransactionMiddleware,
    get_transaction_id,
    with_transaction_id,
)

templates = Jinja2Templates(directory="templates")

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


@app.get(
    "/status/{id}",
    tags=["Status"],
)
async def get_status(
    request: Request,
    response: Response,
    id: str,
    transaction_id: str = Depends(get_transaction_id(create_if_missing=False)),
):
    return {
        "id": id,
        "transaction_id": transaction_id if transaction_id else "No transaction ID",
    }


@app.get(
    "/simple/{id}",
    tags=["Simple"],
)
async def get_status(
    request: Request,
    response: Response,
    id: str,
    transaction_id: str = Depends(get_transaction_id()),
):

    return {
        "id": id,
        "transaction_id": transaction_id if transaction_id else "No transaction ID",
    }


if __name__ == "__main__":

    # Be careful!!! This call does not read the .env file
    run(app, host="0.0.0.0", port=8000)
