from __future__ import annotations

from abc import ABC, abstractmethod

from atlas.discovery.models import Observation


class PublicSourceAdapter(ABC):
    """
    Contract implemented by every public acquisition source.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def search(
        self,
        query: str,
    ) -> tuple[Observation, ...]:
        """
        Execute a public search and return observations.
        """
