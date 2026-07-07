"""
Shared HTTP client for Atlas.

All outbound HTTP requests must pass through this client.
"""

from __future__ import annotations

from dataclasses import dataclass

import httpx


DEFAULT_TIMEOUT_SECONDS = 10.0


@dataclass(slots=True, frozen=True)
class HttpClient:
    """
    Secure HTTP client used throughout Atlas.
    """

    timeout: float = DEFAULT_TIMEOUT_SECONDS

    def get(
        self,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        cookies: dict[str, str] | None = None,
        follow_redirects: bool = False,
    ) -> httpx.Response:
        """
        Perform a secure HTTP GET request.
        """

        if not url.startswith("https://"):
            raise ValueError(
                "Only HTTPS URLs are permitted."
            )

        request_headers = {
            "User-Agent": (
                "Atlas/0.1 "
                "(Commercial Intelligence Engine)"
            ),
        }

        if headers is not None:
            request_headers.update(headers)

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=follow_redirects,
        ) as client:

            return client.get(
                url,
                headers=request_headers,
                params=params,
                cookies=cookies,
            )
