from atlas.discovery.services import DiscoveryService


def test_discover_returns_buyers() -> None:

    service = DiscoveryService()

    buyers = service.discover(
        product="turmeric",
        country="Germany",
    )

    assert len(buyers) > 0
