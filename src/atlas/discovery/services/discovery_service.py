from __future__ import annotations

from atlas.buyer_engine.models import BuyerRecord
from atlas.buyer_engine.providers.kompass import KompassService


class DiscoveryService:
    """
    Stable entry point into Atlas buyer discovery.

    The UI and future APIs interact only with this service.
    Internally it delegates work to one or more providers.
    """

    def __init__(self) -> None:
        self._kompass = KompassService()

    def discover(
        self,
        product: str,
        country: str,
    ) -> tuple[BuyerRecord, ...]:
        """
        Discover buyers using the currently enabled providers.
        """

        return self._kompass.discover(
            product=product,
            country=country,
            live=False,
        )
