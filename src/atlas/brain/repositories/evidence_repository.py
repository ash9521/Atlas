"""
Read-only repository for Evidence entities.
"""

from __future__ import annotations

from collections.abc import Iterable
from uuid import UUID

from atlas.brain.models import Evidence, EvidenceSource


class EvidenceRepository:
    """
    Read-only access to Evidence.
    """

    def __init__(self, evidence: Iterable[Evidence] = ()) -> None:
        self._evidence: tuple[Evidence, ...] = tuple(evidence)

    def list_all(self) -> tuple[Evidence, ...]:
        return self._evidence

    def find_by_company(
        self,
        company_id: UUID,
    ) -> tuple[Evidence, ...]:
        return tuple(
            evidence
            for evidence in self._evidence
            if evidence.company_id == company_id
        )

    def find_by_type(
        self,
        evidence_type: str,
    ) -> tuple[Evidence, ...]:
        return tuple(
            evidence
            for evidence in self._evidence
            if evidence.evidence_type == evidence_type
        )

    def find_by_source(
        self,
        source: EvidenceSource,
    ) -> tuple[Evidence, ...]:
        return tuple(
            evidence
            for evidence in self._evidence
            if evidence.source == source
        )
