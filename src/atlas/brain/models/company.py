"""
Company domain model.

Represents the identity of a company known to Atlas.
"""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(slots=True, frozen=True)
class Company:
    """
    Represents the identity of a company.

    The Company model intentionally stores only identity.
    Evidence, confidence, contacts, and relationships belong
    to their own components.
    """

    id: UUID
    legal_name: str

    @classmethod
    def create(cls, legal_name: str) -> "Company":
        """
        Create a company with a unique Atlas identifier.
        """

        legal_name = legal_name.strip()

        if not legal_name:
            raise ValueError("Company legal name cannot be empty.")

        return cls(
            id=uuid4(),
            legal_name=legal_name,
        )
