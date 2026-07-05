"""
Evidence source domain model.

Represents the origin of a piece of evidence.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class EvidenceSource:
    """
    Immutable description of where evidence originated.
    """

    source_type: str
    name: str
    version: str | None = None

    @classmethod
    def create(
        cls,
        *,
        source_type: str,
        name: str,
        version: str | None = None,
    ) -> "EvidenceSource":
        """
        Create a validated evidence source.
        """

        source_type = source_type.strip()
        name = name.strip()

        if not source_type:
            raise ValueError("Evidence source type cannot be empty.")

        if not name:
            raise ValueError("Evidence source name cannot be empty.")

        if version is not None:
            version = version.strip()

            if version == "":
                version = None

        return cls(
            source_type=source_type,
            name=name,
            version=version,
        )
