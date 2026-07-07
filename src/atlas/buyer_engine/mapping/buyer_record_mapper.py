from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord
from atlas.discovery.models import Observation


class BuyerRecordMapper:
    """
    Converts BuyerRecord into a Discovery Observation.
    """

    def map(
        self,
        record: BuyerRecord,
    ) -> Observation:
        return Observation.create(
            connector=record.source,
            payload={
                "Company": record.company,
                "Country": record.country,
                "Website": record.website,
                "SourceId": record.source_id,
            },
        )
