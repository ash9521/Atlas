# Atlas

Atlas is a production-quality export intelligence platform being built to help identify, evaluate, and build trusted relationships with international buyers.

## Mission

Atlas exists to transform fragmented business evidence into trustworthy intelligence that helps businesses discover, evaluate, and build relationships with international buyers.

The Brain is Atlas's single source of truth. Facts are stored as immutable evidence, while higher-level components compute conclusions such as trust, risk, and recommendations.

## Core Principles

- The repository is the single source of truth.
- The Brain is the system of record.
- Evidence is immutable.
- Evidence is append-only.
- Facts are stored.
- Conclusions are computed.
- Trust is derived from evidence, never stored directly.
- Business value takes priority over unnecessary features.

## Current Status

Sprint 1 established the Brain foundation.

Completed:

- Development environment
- Git repository
- Atlas Constitution
- Project bootstrap
- Company domain model
- EvidenceSource value object
- Evidence entity
- Deep immutability utility
- Public Brain model exports
- Comprehensive unit tests

Current Quality Gate

- PASS: 16/16 tests passing

## Repository Structure

- docs/
- scripts/
- src/
- tests/

Project Constitution:

docs/constitution/CONSTITUTION.md

## Next Sprint

Sprint 2 will focus on the Brain Query Layer, allowing Atlas to retrieve and answer questions about stored evidence while continuing to treat the Brain as the single source of truth.

## Development Standards

- Modular architecture
- Immutable domain models
- PowerShell-first workflow
- Repository always kept in a working state
- Green build required before every commit
