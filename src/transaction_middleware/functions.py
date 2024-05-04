from functools import wraps
from typing import Callable, List

from fastapi import HTTPException, Request
from ksuid import Ksuid

from transaction_middleware.logging import logger
from transaction_middleware.settings import settings


def get_transaction_id(
    create_if_missing: bool = True,
    header_name: str = settings.TRANSACTION_MIDDLEWARE_HEADER,
    generator: Callable[[], str] = lambda: str(Ksuid()),
) -> str:
    """Get the transaction ID from the request headers or generate a new one.

    Args:
        create_if_missing (bool, optional): If True, generates a new transaction ID if not found in the request headers. Defaults to True.
        header_name (str, optional): Name of the header to look for the transaction ID. Defaults to settings.TRANSACTION_MIDDLEWARE_HEADER.
        generator (Callable[[], str], optional): Function to generate a new transaction ID. Defaults to lambda: str(Ksuid()).

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
            transaction_id = generator()
            request.state.transaction_id = transaction_id

        return transaction_id

    return _get_transaction_id
