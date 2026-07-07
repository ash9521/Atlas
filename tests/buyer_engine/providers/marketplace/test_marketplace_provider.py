from atlas.buyer_engine.models import (
    BuyerSearchRequest,
    Product,
)
from atlas.buyer_engine.providers.marketplace import (
    MarketplaceProvider,
)


class DummyMarketplace(MarketplaceProvider):

    @property
    def name(self) -> str:
        return "dummy"

    def search(
        self,
        request: BuyerSearchRequest,
    ):
        return ()


def test_marketplace_provider_contract():

    request = BuyerSearchRequest(
        product=Product.create(
            canonical_name="Turmeric",
            hs_code="091030",
        ),
    )

    provider = DummyMarketplace()

    assert provider.name == "dummy"
    assert provider.search(request) == ()
