"""
Kompass public directory adapter.

Responsible only for downloading search pages.
"""

from __future__ import annotations

from urllib.parse import quote_plus

from atlas.buyer_engine.acquisition import (
    PublicDirectoryClient,
)


class KompassAdapter:
    """
    Downloads Kompass search pages.
    """

    BASE_URL = "https://gb.kompass.com/searchCompanies/"

    def __init__(
        self,
        client: PublicDirectoryClient | None = None,
    ) -> None:
        self._client = client or PublicDirectoryClient()

    def search(
        self,
        query: str,
    ) -> str:

        url = (
            self.BASE_URL
            + quote_plus(query)
        )

        return self._client.get(url)
