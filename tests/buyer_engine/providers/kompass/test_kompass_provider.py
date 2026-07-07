from atlas.buyer_engine.providers.kompass import (
    KompassProvider,
)


def test_provider_name() -> None:
    provider = KompassProvider()

    assert provider.name == "kompass"
