from atlas.buyer_engine.providers.kompass import (
    KompassService,
)


def test_discover_fixture() -> None:

    service = KompassService()

    buyers = service.discover(
        product="turmeric",
        country="Germany",
    )

    assert len(buyers) > 0

    first = buyers[0]

    assert first.company != ""
    assert first.source == "kompass"
