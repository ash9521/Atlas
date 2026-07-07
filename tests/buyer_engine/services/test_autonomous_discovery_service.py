from atlas.buyer_engine.models import BuyerSearchRequest, Product
from atlas.buyer_engine.services import AutonomousDiscoveryService


def test_execute_returns_observations() -> None:
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
        country="Germany",
        buyer_type="Importer",
    )

    observations = AutonomousDiscoveryService().execute(
        request,
    )

    assert len(observations) == 1

    observation = observations[0]

    assert observation.connector == "autonomous_discovery"
    assert observation.payload["Company"] == "ABC Imports"
    assert observation.payload["Country"] == "Germany"
