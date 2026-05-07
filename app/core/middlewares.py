import time
from fastapi import Request
from typing import Callable, Awaitable
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware


class TimingMW(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        start = time.perf_counter()
        # return await super().dispatch(request, call_next)
        response = await call_next(request)
        end = time.perf_counter()
        response.headers["X-Perf-Time"] = str(end - start)
        return response