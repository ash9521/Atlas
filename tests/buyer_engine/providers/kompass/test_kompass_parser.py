from pathlib import Path

from atlas.buyer_engine.providers.kompass import (
    KompassParser,
)


def test_parse_fixture() -> None:

    payload = Path(
        "tests/fixtures/providers/kompass/search_turmeric_germany.html"
    ).read_text(
        encoding="utf-8",
    )

    parser = KompassParser()

    companies = parser.parse(
        payload,
    )

    assert len(companies) > 0

    first = companies[0]

    assert first.company != ""
    assert first.country is not None
