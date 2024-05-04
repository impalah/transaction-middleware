import os
import uuid
from typing import Optional

from fastapi import Depends, FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.requests import Request
from starlette.responses import Response
from uvicorn import run

from transaction_middleware import TransactionMiddleware, get_transaction_id

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
    """Create a new item with a transaction ID if it does not exists

    Args:
        request (Request): The request object
        response (Response): The response object
        id (str): The item ID
        transaction_id (str, optional): The transaction ID. Defaults to Depends(get_transaction_id()).

    Returns:
        _type_: _description_
    """
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
    """Return the status of an item and the transaction id, if it exists
    It doesn't create a new transaction ID if it does not exists

    Args:
        request (Request): The request object
        response (Response): The response object
        id (str): The item ID
        transaction_id (str, optional): The transaction ID. Defaults to Depends(get_transaction_id(create_if_missing=False)).

    Returns:
        _type_: _description_
    """
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
    transaction_id: str = Depends(
        get_transaction_id(generator=lambda: str(uuid.uuid4()))
    ),
):
    """Gets a response with a transaction ID. If it does not exists, it creates a new one of type uuid4

    Args:
        request (Request): The request object
        response (Response): The response object
        id (str): The item ID
        transaction_id (_type_, optional): The transaction ID. Defaults to Depends(get_transaction_id(generator=lambda: str(uuid.uuid4()))).

    Returns:
        _type_: _description_
    """

    return {
        "id": id,
        "transaction_id": transaction_id if transaction_id else "No transaction ID",
    }


if __name__ == "__main__":

    # Be careful!!! This call does not read the .env file
    run(app, host="0.0.0.0", port=8000)
