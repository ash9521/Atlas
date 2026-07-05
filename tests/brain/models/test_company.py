import pytest

from atlas.brain.models.company import Company


def test_create_company():
    company = Company.create("Acme Foods")

    assert company.legal_name == "Acme Foods"
    assert company.id is not None


def test_empty_company_name_raises_error():
    with pytest.raises(ValueError):
        Company.create("")
