"""
Autonomous buyer discovery orchestration.
"""

from __future__ import annotations

from atlas.brain.models import Evidence
from atlas.buyer_engine.models import BuyerSearchRequest
from atlas.discovery.services import DiscoveryPipelineService

from .autonomous_discovery_service import (
    AutonomousDiscoveryService,
)


class AutonomousBuyerDiscoveryService:
    """
    Coordinates autonomous buyer discovery.
    """

    def __init__(
        self,
        pipeline: DiscoveryPipelineService,
    ) -> None:
        self._pipeline = pipeline
        self._discovery = AutonomousDiscoveryService()

    def execute(
        self,
        request: BuyerSearchRequest,
    ) -> tuple[Evidence, ...]:

        observations = self._discovery.execute(
            request,
        )

        return self._pipeline.process_observations(
            observations,
        )
