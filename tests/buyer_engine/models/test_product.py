from uuid import UUID

import pytest

from atlas.buyer_engine.models.product import Product


def test_create_product():
    product = Product.create(
        canonical_name="Turmeric",
        hs_code="091030",
    )

    assert isinstance(product.id, UUID)
    assert product.canonical_name == "Turmeric"
    assert product.hs_code == "091030"


def test_product_name_cannot_be_empty():
    with pytest.raises(ValueError):
        Product.create(
            canonical_name="",
            hs_code="091030",
        )


def test_product_hs_code_cannot_be_empty():
    with pytest.raises(ValueError):
        Product.create(
            canonical_name="Turmeric",
            hs_code="",
        )
