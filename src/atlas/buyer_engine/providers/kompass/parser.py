from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord


class KompassParser:
    """
    Converts verified Kompass responses into BuyerRecord objects.
    """

    def parse(
        self,
        payload: str,
    ) -> tuple[BuyerRecord, ...]:
        raise NotImplementedError(
            "Implemented after validating live response."
        )
