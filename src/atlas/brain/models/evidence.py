"""
Evidence domain model.

Represents an immutable piece of evidence known to Atlas.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from atlas.brain.models.evidence_source import EvidenceSource
from atlas.brain.utils.immutable import freeze


@dataclass(slots=True, frozen=True)
class Evidence:
    """
    Immutable evidence recorded by Atlas.

    Evidence stores observations only.
    Higher-level systems derive facts, trust, and decisions.
    """

    id: UUID
    company_id: UUID
    evidence_type: str
    source: EvidenceSource
    observed_at: datetime
    recorded_at: datetime
    payload: Any

    @classmethod
    def create(
        cls,
        *,
        company_id: UUID,
        evidence_type: str,
        source: EvidenceSource,
        observed_at: datetime,
        payload: dict[str, Any],
    ) -> "Evidence":
        """
        Create validated immutable evidence.
        """

        evidence_type = evidence_type.strip()

        if not evidence_type:
            raise ValueError("Evidence type cannot be empty.")

        if observed_at.tzinfo is None:
            raise ValueError(
                "observed_at must be timezone-aware."
            )

        return cls(
            id=uuid4(),
            company_id=company_id,
            evidence_type=evidence_type,
            source=source,
            observed_at=observed_at.astimezone(
                timezone.utc
            ),
            recorded_at=datetime.now(
                timezone.utc
            ),
            payload=freeze(payload),
        )
