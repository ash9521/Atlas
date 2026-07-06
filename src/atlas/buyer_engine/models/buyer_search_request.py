"""
Buyer search request model.

Represents an exporter's request to discover potential buyers.
"""

from __future__ import annotations

from dataclasses import dataclass

from atlas.buyer_engine.models.product import Product


@dataclass(slots=True, frozen=True)
class BuyerSearchRequest:
    """
    Immutable buyer search request.

    Carries the information required to begin buyer discovery.
    """

    product: Product
    country: str | None = None
    buyer_type: str | None = None
