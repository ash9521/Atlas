from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KompassParsedCompany:
    """
    Raw company extracted from Kompass.

    This model mirrors the source data and is intentionally
    independent of Atlas BuyerRecord.
    """

    company: str
    country: str
    website: str | None
    source_id: str | None
