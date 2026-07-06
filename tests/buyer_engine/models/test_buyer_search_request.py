from dataclasses import FrozenInstanceError

import pytest

from atlas.buyer_engine.models.buyer_search_request import BuyerSearchRequest
from atlas.buyer_engine.models.product import Product


def test_create_buyer_search_request():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
    )

    assert request.product == product
    assert request.country is None
    assert request.buyer_type is None


def test_create_buyer_search_request_with_filters():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
        country="Germany",
        buyer_type="Importer",
    )

    assert request.country == "Germany"
    assert request.buyer_type == "Importer"


def test_buyer_search_request_is_immutable():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    request = BuyerSearchRequest(
        product=product,
    )

    with pytest.raises(FrozenInstanceError):
        request.country = "India"
