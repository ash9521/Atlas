"""
Brain query request.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, frozen=True)
class BrainQuery:
    """
    Immutable request to the Brain query layer.
    """

    company_id: UUID
    evidence_type: str | None = None
