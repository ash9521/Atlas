"""
Decision returned by Atlas.

Represents the recommended next action after evaluating
trust and conclusions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class CompanyDecision:
    """
    Immutable decision.
    """

    action: str
    reason: str
