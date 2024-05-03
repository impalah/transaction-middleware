from functools import wraps
from typing import List

from fastapi import HTTPException, Request
from ksuid import Ksuid

from transaction_middleware.logging import logger


def get_transaction_id(
    create_if_missing: bool = True,
    header_name: str = "X-Transaction-ID",
) -> str:
    """Get the transaction ID from the request headers or generate a new one.

    Args:
        create_if_missing (bool, optional): If True, generates a new transaction ID if not found in the request headers. Defaults to True.
        request (Request): _description_

    Raises:
        HTTPException: _description_

    Returns:
        str: _description_
    """

    def _get_transaction_id(request: Request) -> str:

        # First check if it exists on request.state
        transaction_id: str = (
            request.state.transaction_id
            if hasattr(request.state, "transaction_id")
            else None
        )

        logger.debug(f"Transaction ID from state: {transaction_id}")

        if not transaction_id:
            # Extract transaction id from request if does not exists on state
            transaction_id = request.headers.get(header_name)
            logger.debug(f"Transaction ID from headers: {transaction_id}")

        if transaction_id is None and create_if_missing:
            transaction_id = str(Ksuid())
            request.state.transaction_id = transaction_id

        return transaction_id

    return _get_transaction_id
