"""
Trust score.

Trust is computed from conclusions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class TrustScore:
    """
    Overall trust assessment.
    """

    score: float
    confidence: str
