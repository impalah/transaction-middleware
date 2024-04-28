from typing import List

from fastapi import HTTPException, Request


def transaction_id_required(create_if_missing: bool = True):
    """Decorator to mark a FastAPI endpoint as requiring a transaction ID.

    Args:
        create_if_missing (bool, optional): Create transaction if it does not exists. Defaults to True.
    """

    def decorator(func):
        func.create_transaction_id = create_if_missing
        return func

    return decorator


def get_transaction_id(request: Request, create_if_missing: bool = True) -> str:
    """Get the transaction ID from the request headers or generate a new one.

    Args:
        request (Request): _description_
        create_if_missing (bool, optional): _description_. Defaults to True.

    Raises:
        HTTPException: _description_

    Returns:
        str: _description_
    """

    # Extract transaction id from request
    transaction_id = (
        request.state.transaction_id
        if hasattr(request.state, "transaction_id")
        else None
    )

    return transaction_id
