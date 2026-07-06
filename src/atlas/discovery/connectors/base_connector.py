from __future__ import annotations

from abc import ABC, abstractmethod

from atlas.discovery.models import InputSource, Observation


class BaseConnector(ABC):
    """
    Base class for all commercial intelligence connectors.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable connector name.
        """

    @abstractmethod
    def acquire(
        self,
        source: InputSource,
    ) -> list[Observation]:
        """
        Acquire observations from an input source.
        """
