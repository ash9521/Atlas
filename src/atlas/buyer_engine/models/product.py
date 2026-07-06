"""
Product domain model.

Represents the identity of an export product known to Atlas.
"""

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(slots=True, frozen=True)
class Product:
    """
    Represents the identity of an export product.

    The Product model intentionally stores only product identity.
    Buyer discovery, market intelligence, specifications,
    and commercial knowledge belong to their own components.
    """

    id: UUID
    canonical_name: str
    hs_code: str

    @classmethod
    def create(
        cls,
        *,
        canonical_name: str,
        hs_code: str,
    ) -> "Product":
        """
        Create a product with a unique Atlas identifier.
        """

        canonical_name = canonical_name.strip()
        hs_code = hs_code.strip()

        if not canonical_name:
            raise ValueError(
                "Product canonical name cannot be empty."
            )

        if not hs_code:
            raise ValueError(
                "Product HS code cannot be empty."
            )

        return cls(
            id=uuid4(),
            canonical_name=canonical_name,
            hs_code=hs_code,
        )
