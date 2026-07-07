from __future__ import annotations

from urllib.parse import quote_plus

from atlas.buyer_engine.acquisition import PublicDirectoryClient
from atlas.buyer_engine.contracts import PublicSourceAdapter
from atlas.buyer_engine.mapping import BuyerRecordMapper
from atlas.buyer_engine.parsers import OpenCorporatesParser
from atlas.discovery.models import Observation


class OpenCorporatesAdapter(PublicSourceAdapter):

    BASE_URL = (
        "https://api.opencorporates.com/v0.4/companies/search"
    )

    def __init__(
        self,
        client: PublicDirectoryClient | None = None,
    ) -> None:
        self._client = client or PublicDirectoryClient()
        self._parser = OpenCorporatesParser()
        self._mapper = BuyerRecordMapper()

    @property
    def name(self) -> str:
        return "opencorporates"

    def search(
        self,
        query: str,
    ) -> tuple[Observation, ...]:

        payload = self._client.get(
            f"{self.BASE_URL}?q={quote_plus(query)}"
        )

        records = self._parser.parse(
            payload,
        )

        return tuple(
            self._mapper.map(record)
            for record in records
        )
