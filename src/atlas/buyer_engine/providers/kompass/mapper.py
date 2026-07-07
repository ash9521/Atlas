from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord

from atlas.buyer_engine.providers.kompass.models import (
    KompassParsedCompany,
)


class KompassMapper:
    """
    Maps KompassParsedCompany into Atlas BuyerRecord.
    """

    def map(
        self,
        company: KompassParsedCompany,
    ) -> BuyerRecord:

        return BuyerRecord(
            company=company.company,
            country=company.country,
            website=company.website,
            source="kompass",
            source_id=company.source_id,
        )
