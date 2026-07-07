from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord

from .client import KompassClient
from .mapper import KompassMapper
from .parser import KompassParser


class KompassService:
    """
    Executes the Kompass acquisition pipeline.
    """

    def __init__(
        self,
        client: KompassClient | None = None,
        parser: KompassParser | None = None,
        mapper: KompassMapper | None = None,
    ) -> None:
        self._client = client or KompassClient()
        self._parser = parser or KompassParser()
        self._mapper = mapper or KompassMapper()

    def discover(
        self,
        product: str,
        country: str | None = None,
        *,
        live: bool = False,
    ) -> tuple[BuyerRecord, ...]:

        if live:
            payload = self._client.load_live(
                product=product,
                country=country,
            )
        else:
            payload = self._client.load_fixture()

        parsed = self._parser.parse(
            payload,
        )

        buyers = tuple(
            self._mapper.map(company)
            for company in parsed
        )

        return buyers
