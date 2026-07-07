from atlas.buyer_engine.providers.kompass import (
    KompassParser,
)


def test_parser_exists() -> None:
    parser = KompassParser()

    assert parser is not None
