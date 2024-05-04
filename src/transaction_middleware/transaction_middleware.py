from typing import Optional

from fastapi import Request, status
from fastapi.security.utils import get_authorization_scheme_param
from ksuid import Ksuid
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

from transaction_middleware.logging import logger
from transaction_middleware.settings import settings


class TransactionMiddleware(BaseHTTPMiddleware):
    """Transaction middleware for FastAPI
    Manages transaction IDs in the request.

    Args:
        BaseHTTPMiddleware (_type_): _description_
    """

    def __init__(
        self,
        header_name: str = settings.TRANSACTION_MIDDLEWARE_HEADER,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.header_name = header_name

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response | JSONResponse:

        # Check if transaction ID is already in the request
        transaction_id = request.headers.get(self.header_name)

        logger.debug("Transaction ID from request: {}", transaction_id)

        # Process the request
        response = await call_next(request)

        transaction_id = (
            request.state.transaction_id
            if hasattr(request.state, "transaction_id")
            else None
        )

        logger.debug("Transaction ID after request: {}", transaction_id)

        # Add transaction ID to the response
        if transaction_id:
            logger.debug(f"Adding Transaction ID to response: {transaction_id}")
            response.headers[self.header_name] = transaction_id
        return response
