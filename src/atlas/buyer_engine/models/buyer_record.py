from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BuyerRecord:
    """
    Canonical buyer record returned by every public source.
    """

    company: str
    country: str
    website: str | None
    source: str
    source_id: str | None = None
