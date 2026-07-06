# ADR-0006 — Fact Engine

## Status

Accepted

## Context

Sprint 2 introduced:

- Immutable Evidence
- Brain Queries
- Company Dossier
- Company Facts

The Constitution states:

- Evidence is stored.
- Facts are computed.
- Conclusions are computed.
- Trust is derived from evidence.

Sprint 2 computes facts inside BrainQueryService.

As Atlas grows, fact computation must become its own subsystem.

## Decision

Introduce a dedicated Fact Engine during Sprint 3.

Responsibilities:

- Compute facts only.
- Never mutate evidence.
- Never persist facts.
- Produce deterministic output.
- Remain independent of conclusions and trust.

The Brain Query Layer will delegate fact computation to the Fact Engine.

## Consequences

Benefits

- Clear separation of responsibilities.
- Easier testing.
- Better scalability.
- Stable architecture.

Trade-offs

- Additional abstraction.
- More classes.

Accepted by:

- CEO
- CTO
- Chief Architect
- QA
- Red Team
- CAT
