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

    def get(self, url: str) -> httpx.Response:
        """
        Perform a secure HTTP GET request.
        """

        if not url.startswith("https://"):
            raise ValueError(
                "Only HTTPS URLs are permitted."
            )

        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=False,
        ) as client:
            return client.get(
                url,
                headers={
                    "User-Agent": (
                        "Atlas/0.1 "
                        "(Commercial Intelligence Engine)"
                    ),
                },
            )
