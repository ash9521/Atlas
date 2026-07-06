"""
Candidate company domain model.

Represents a business discovered by the Buyer Engine
before evaluation by the Atlas Brain.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CandidateCompany:
    """
    Immutable candidate company.

    Represents a potential buyer discovered during
    the discovery process.
    """

    name: str
    source: str
    query: str

    @classmethod
    def create(
        cls,
        *,
        name: str,
        source: str,
        query: str,
    ) -> "CandidateCompany":
        """
        Create a validated candidate company.
        """

        name = name.strip()
        source = source.strip()
        query = query.strip()

        if not name:
            raise ValueError(
                "Candidate company name cannot be empty."
            )

        if not source:
            raise ValueError(
                "Candidate company source cannot be empty."
            )

        if not query:
            raise ValueError(
                "Candidate company query cannot be empty."
            )

        return cls(
            name=name,
            source=source,
            query=query,
        )
