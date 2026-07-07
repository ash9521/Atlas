from __future__ import annotations

from atlas.brain.models import Evidence
from atlas.discovery.connectors import BaseConnector
from atlas.discovery.ingestion import EvidenceFactory
from atlas.discovery.models import InputSource, Observation
from atlas.discovery.normalization import ObservationNormalizer
from atlas.discovery.resolution import CompanyResolver


class DiscoveryPipelineService:
    """
    Orchestrates the discovery pipeline.
    """

    def __init__(
        self,
        *,
        connector: BaseConnector,
        normalizer: ObservationNormalizer,
        resolver: CompanyResolver,
        evidence_factory: EvidenceFactory,
    ) -> None:
        self._connector = connector
        self._normalizer = normalizer
        self._resolver = resolver
        self._factory = evidence_factory

    def process_observations(
        self,
        observations: tuple[Observation, ...],
    ) -> tuple[Evidence, ...]:
        evidence: list[Evidence] = []

        for observation in observations:
            normalized = self._normalizer.normalize(
                observation,
            )

            resolution = self._resolver.resolve(
                normalized,
            )

            if resolution.company is None:
                continue

            evidence.append(
                self._factory.create(
                    company=resolution.company,
                    observation=normalized,
                )
            )

        return tuple(evidence)

    def run(
        self,
        source: InputSource,
    ) -> tuple[Evidence, ...]:
        observations = tuple(
            self._connector.acquire(source)
        )

        return self.process_observations(
            observations,
        )
