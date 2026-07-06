"""
Discovery strategy service.

Generates deterministic search queries used to discover
potential international buyers.
"""

from atlas.buyer_engine.models.buyer_search_request import BuyerSearchRequest


class DiscoveryStrategyService:
    """
    Generates buyer discovery search queries.
    """

    DEFAULT_BUYER_TYPES = (
        "importer",
        "distributor",
        "wholesaler",
        "supplier",
    )

    @staticmethod
    def generate_queries(
        request: BuyerSearchRequest,
    ) -> list[str]:
        """
        Generate search queries from a buyer search request.
        """

        product = request.product.canonical_name.strip()
        country = request.country.strip() if request.country else None

        buyer_types = (
            [request.buyer_type.strip().lower()]
            if request.buyer_type
            else list(DiscoveryStrategyService.DEFAULT_BUYER_TYPES)
        )

        queries: list[str] = []

        for buyer_type in buyer_types:
            parts = [
                product,
                buyer_type,
            ]

            if country:
                parts.append(country)

            queries.append(" ".join(parts))

        return queries
