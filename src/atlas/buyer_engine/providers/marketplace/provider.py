from __future__ import annotations

from abc import ABC, abstractmethod

from atlas.buyer_engine.models import (
    BuyerRecord,
    BuyerSearchRequest,
)


class MarketplaceProvider(ABC):
    """
    Base contract for marketplace providers.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def search(
        self,
        request: BuyerSearchRequest,
    ) -> tuple[BuyerRecord, ...]:
        ...
