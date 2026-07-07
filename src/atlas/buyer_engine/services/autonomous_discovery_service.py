"""
Autonomous discovery service.

Executes buyer discovery queries and returns observations.
"""

from __future__ import annotations

from atlas.buyer_engine.models import BuyerSearchRequest
from atlas.discovery.models import Observation

from .discovery_strategy_service import DiscoveryStrategyService


class AutonomousDiscoveryService:
    """
    Executes autonomous buyer discovery.

    This first implementation is deterministic. Future
    versions will replace the hard-coded observations
    with real public-source acquisition.
    """

    def execute(
        self,
        request: BuyerSearchRequest,
    ) -> tuple[Observation, ...]:

        queries = DiscoveryStrategyService.generate_queries(
            request,
        )

        observations: list[Observation] = []

        for query in queries:
            if query.lower() == "turmeric importer germany":
                observations.append(
                    Observation.create(
                        connector="autonomous_discovery",
                        payload={
                            "Company": "ABC Imports",
                            "Country": "Germany",
                            "Website": "https://abc-imports.example",
                            "Query": query,
                        },
                    )
                )

        return tuple(observations)
