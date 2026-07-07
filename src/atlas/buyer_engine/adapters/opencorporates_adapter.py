"""
OpenCorporates adapter.

Responsible for retrieving raw company search results.
"""

from __future__ import annotations

from atlas.buyer_engine.acquisition import PublicDirectoryClient
from atlas.buyer_engine.contracts import PublicSourceAdapter
from atlas.discovery.models import Observation


class OpenCorporatesAdapter(PublicSourceAdapter):
    """
    Public source adapter for OpenCorporates.
    """

    BASE_URL = (
        "https://api.opencorporates.com/v0.4/companies/search"
    )

    def __init__(
        self,
        client: PublicDirectoryClient | None = None,
    ) -> None:
        self._client = client or PublicDirectoryClient()

    @property
    def name(self) -> str:
        return "opencorporates"

    def search(
        self,
        query: str,
    ) -> tuple[Observation, ...]:
        url = (
            f"{self.BASE_URL}?q={query}"
        )

        response = self._client.get(url)

        observation = Observation.create(
            connector=self.name,
            payload={
                "RawResponse": response,
                "Query": query,
            },
        )

        return (observation,)
