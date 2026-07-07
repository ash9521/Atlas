from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord, BuyerSearchRequest
from atlas.networking.http_client import HttpClient


class KompassProvider:
    """
    Downloads raw responses from Kompass.

    Parsing is delegated to KompassParser.
    """

    def __init__(
        self,
        client: HttpClient | None = None,
    ) -> None:
        self._client = client or HttpClient()

    @property
    def name(self) -> str:
        return "kompass"

    def fetch(
        self,
        url: str,
    ) -> str:
        response = self._client.get(url)
        response.raise_for_status()
        return response.text

    def search(
        self,
        request: BuyerSearchRequest,
    ) -> tuple[BuyerRecord, ...]:
        raise NotImplementedError(
            "Implemented after parser validation."
        )
