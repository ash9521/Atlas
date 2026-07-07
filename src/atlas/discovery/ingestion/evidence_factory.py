from __future__ import annotations

from atlas.brain.models import (
    Evidence,
    EvidenceSource,
)
from atlas.brain.models.company import Company
from atlas.discovery.normalization.models import (
    NormalizedObservation,
)


class EvidenceFactory:
    """
    Creates immutable Brain Evidence from a resolved observation.
    """

    def create(
        self,
        *,
        company: Company,
        observation: NormalizedObservation,
    ) -> Evidence:
        source = EvidenceSource.create(
            source_type="connector",
            name=observation.connector,
        )

        return Evidence.create(
            company_id=company.id,
            evidence_type="buyer.discovery",
            source=source,
            observed_at=observation.acquired_at,
            payload=dict(observation.payload),
        )
