import pytest

from atlas.buyer_engine.models.candidate_company import CandidateCompany
from atlas.buyer_engine.services.discovery_result_mapper import (
    DiscoveryResultMapper,
)


def test_map_valid_discovery_result():
    result = {
        "name": "ABC Spice Imports GmbH",
        "source": "Google",
        "query": "Turmeric importer Germany",
    }

    company = DiscoveryResultMapper.map(result)

    assert isinstance(company, CandidateCompany)
    assert company.name == "ABC Spice Imports GmbH"
    assert company.source == "Google"
    assert company.query == "Turmeric importer Germany"


@pytest.mark.parametrize(
    "result",
    [
        {
            "name": "",
            "source": "Google",
            "query": "Turmeric importer Germany",
        },
        {
            "name": "ABC Spice Imports GmbH",
            "source": "",
            "query": "Turmeric importer Germany",
        },
        {
            "name": "ABC Spice Imports GmbH",
            "source": "Google",
            "query": "",
        },
    ],
)
def test_invalid_discovery_result(result):
    with pytest.raises(ValueError):
        DiscoveryResultMapper.map(result)
