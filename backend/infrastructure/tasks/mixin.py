from typing import Any

import requests
from requests import Response, RequestException

from backend.core.exceptions import RequesterError
from backend.core.logger import Logger
from backend.domain.enums.common import RequestMethodEnum

logger = Logger.setup_logger(__name__)


class RequesterMixin:
    TIMEOUT: int = 50  # seconds

    def _request(
            self,
            method: RequestMethodEnum,
            url: str,
            body: dict[str, Any] | None = None,
            params: dict[str, Any] | None = None,
            headers: dict[str, Any] | None = None,
            cookies: dict[str, Any] | None = None,
            is_raise_for_status: bool = True,
    ) -> Response:
        method_str = method.value
        try:
            kwargs = self._prepare_request_kwargs(url, headers, params, cookies)

            if method_str != RequestMethodEnum.GET.value and body:
                kwargs["json"] = body

            method_func = getattr(requests, method_str)
            response = method_func(**kwargs)

            if is_raise_for_status:
                response.raise_for_status()

            logger.info(f"[RequesterMixin]: {method_str.upper()} {url} — {response.status_code}")
            return response

        except RequestException as e:
            logger.error(f"[RequesterMixin]: Request failed — {method_str.upper()} {url} — {e}")
            raise RequesterError(f"Request failed: {e}") from e

    def _prepare_request_kwargs(
            self,
            url: str,
            headers: dict[str, Any] | None = None,
            params: dict[str, Any] | None = None,
            cookies: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return {
            "url": url,
            "headers": {**(headers or {})},
            "params": params or {},
            "cookies": cookies or {},
            "timeout": self.TIMEOUT
        }
