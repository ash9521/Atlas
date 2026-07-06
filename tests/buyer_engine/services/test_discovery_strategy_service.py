from atlas.buyer_engine.models.buyer_search_request import BuyerSearchRequest
from atlas.buyer_engine.models.product import Product
from atlas.buyer_engine.services.discovery_strategy_service import (
    DiscoveryStrategyService,
)


def test_generate_queries_with_specific_buyer_type():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
        country="Germany",
        buyer_type="Importer",
    )

    queries = DiscoveryStrategyService.generate_queries(request)

    assert queries == [
        "Turmeric importer Germany",
    ]


def test_generate_queries_with_default_buyer_types():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
        country="Germany",
    )

    queries = DiscoveryStrategyService.generate_queries(request)

    assert queries == [
        "Turmeric importer Germany",
        "Turmeric distributor Germany",
        "Turmeric wholesaler Germany",
        "Turmeric supplier Germany",
    ]
