from atlas.buyer_engine.providers.kompass import (
    KompassMapper,
)

from atlas.buyer_engine.providers.kompass.models import (
    KompassParsedCompany,
)


def test_map_company() -> None:

    mapper = KompassMapper()

    parsed = KompassParsedCompany(
        company="ABC Imports GmbH",
        country="Germany",
        website="https://example.com",
        source_id="123",
    )

    buyer = mapper.map(
        parsed,
    )

    assert buyer.company == "ABC Imports GmbH"
    assert buyer.country == "Germany"
    assert buyer.website == "https://example.com"
    assert buyer.source == "kompass"
    assert buyer.source_id == "123"
