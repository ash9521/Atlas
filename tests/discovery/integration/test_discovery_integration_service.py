from unittest.mock import Mock

from atlas.discovery.integration import (
    DiscoveryIntegrationService,
)


def test_service_exposes_dependencies() -> None:
    pipeline = Mock()
    brain = Mock()
    kompass = Mock()

    service = DiscoveryIntegrationService(
        pipeline=pipeline,
        brain=brain,
        kompass=kompass,
    )

    assert service.pipeline is pipeline
    assert service.brain is brain


def test_discover_delegates_to_kompass() -> None:
    pipeline = Mock()
    brain = Mock()
    kompass = Mock()

    kompass.discover.return_value = ("buyer",)

    service = DiscoveryIntegrationService(
        pipeline=pipeline,
        brain=brain,
        kompass=kompass,
    )

    result = service.discover(
        product="turmeric",
        country="Germany",
    )

    assert result == ("buyer",)

    kompass.discover.assert_called_once_with(
        product="turmeric",
        country="Germany",
    )
