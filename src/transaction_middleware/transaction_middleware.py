from typing import Optional

from fastapi import Request, status
from fastapi.security.utils import get_authorization_scheme_param
from ksuid import Ksuid
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import JSONResponse, Response
from starlette.types import ASGIApp

from transaction_middleware.logging import logger


class TransactionMiddleware(BaseHTTPMiddleware):
    """Transaction middleware for FastAPI
    Manages transaction IDs in the request.

    Args:
        BaseHTTPMiddleware (_type_): _description_
    """

    def __init__(
        self,
        header_name: str = "X-Transaction-ID",
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

        # Generate a new transaction Id if it doesnt exists and is required
        if transaction_id is None and getattr(
            request.scope["endpoint"], "create_transaction_id", False
        ):
            # TODO: allow to specify a custom transaction ID generator
            transaction_id = str(Ksuid())
            request.state.transaction_id = transaction_id
        elif transaction_id is not None:
            request.state.transaction_id = transaction_id

        # Process the request
        response = await call_next(request)

        # Add transaction ID to the response
        if transaction_id:
            response.headers[self.header_name] = transaction_id
        return response
