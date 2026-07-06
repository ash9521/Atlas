from dataclasses import FrozenInstanceError

import pytest

from atlas.buyer_engine.models.candidate_company import CandidateCompany


def test_create_candidate_company():
    company = CandidateCompany.create(
        name="ABC Spice Imports GmbH",
        source="Google",
        query="Turmeric importer Germany",
    )

    assert company.name == "ABC Spice Imports GmbH"
    assert company.source == "Google"
    assert company.query == "Turmeric importer Germany"


@pytest.mark.parametrize(
    ("field", "name", "source", "query"),
    [
        ("name", "", "Google", "Turmeric importer Germany"),
        ("source", "ABC Spice Imports GmbH", "", "Turmeric importer Germany"),
        ("query", "ABC Spice Imports GmbH", "Google", ""),
    ],
)
def test_candidate_company_required_fields(
    field: str,
    name: str,
    source: str,
    query: str,
):
    with pytest.raises(ValueError):
        CandidateCompany.create(
            name=name,
            source=source,
            query=query,
        )


def test_candidate_company_is_immutable():
    company = CandidateCompany.create(
        name="ABC Spice Imports GmbH",
        source="Google",
        query="Turmeric importer Germany",
    )

    with pytest.raises(FrozenInstanceError):
        company.name = "Another Company"
