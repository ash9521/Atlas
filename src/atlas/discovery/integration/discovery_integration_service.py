from __future__ import annotations

from atlas.brain.services import BrainQueryService
from atlas.buyer_engine.models import BuyerRecord
from atlas.buyer_engine.providers.kompass import KompassService
from atlas.discovery.services import DiscoveryPipelineService


class DiscoveryIntegrationService:
    """
    Coordinates discovery and Brain services.

    Today:
        - Executes buyer discovery.

    Future:
        - Convert discoveries into observations.
        - Execute DiscoveryPipelineService.
        - Persist evidence.
        - Query Brain.
    """

    def __init__(
        self,
        *,
        pipeline: DiscoveryPipelineService,
        brain: BrainQueryService,
        kompass: KompassService,
    ) -> None:
        self._pipeline = pipeline
        self._brain = brain
        self._kompass = kompass

    @property
    def pipeline(self) -> DiscoveryPipelineService:
        return self._pipeline

    @property
    def brain(self) -> BrainQueryService:
        return self._brain

    def discover(
        self,
        *,
        product: str,
        country: str,
    ) -> tuple[BuyerRecord, ...]:
        return self._kompass.discover(
            product=product,
            country=country,
        )
