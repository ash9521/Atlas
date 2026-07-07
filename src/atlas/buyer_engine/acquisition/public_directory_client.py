"""
Generic HTTP client for public business directories.
"""

from __future__ import annotations

from atlas.networking.http_client import HttpClient


class PublicDirectoryClient:
    """
    Shared HTTP client for public directory adapters.
    """

    def __init__(
        self,
        client: HttpClient | None = None,
    ) -> None:
        self._client = client or HttpClient()

    def get(
        self,
        url: str,
    ) -> str:
        """
        Download the HTML for a public directory page.
        """

        response = self._client.get(url)

        response.raise_for_status()

        return response.text
