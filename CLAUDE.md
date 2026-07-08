# Atlas

Export intelligence platform. Mission: shrink the distance between
"I have a product" and "I have a paying international export customer."

## Current phase (this matters most)

Phase 1 goal: reliable buyer discovery with a good UI. "Reliable" is the
actual point, not just "a list of names" — a company confirmed by 2+
independent sources (e.g. Kompass + OpenCorporates) is meaningfully more
trustworthy than one from a single source. Revenue urgency is real:
prioritize whatever shortens distance-to-first-deal. Backlog anything
that doesn't.

## Non-negotiable safety rule

NEVER add live HTTP acquisition against Kompass. It's a DataDome-protected
site; Kompass is manual-fixture-import only, permanently. This already
happened once by accident (see adr-0007) — do not reintroduce
`load_live()`, browser-spoofing headers, or CAPTCHA-detection logic for
Kompass under any name, in any file.

## Architecture (read the ADRs for full reasoning, don't re-derive it)

- The Brain (`src/atlas/brain/`) is the system of record: Evidence
  (immutable, append-only) -> Facts -> Trust/Conclusions -> Decisions.
  See `docs/constitution/CONSTITUTION.md`.
- Buyer providers (Kompass, OpenCorporates) produce `BuyerRecord`.
- The bridge from providers to the Brain (`BuyerRecordMapper`,
  `KompassAdapter`, `OpenCorporatesAdapter`, `DiscoveryIntegrationService`)
  exists and works — see adr-0008, adr-0009. The live FastAPI UI does NOT
  use this bridge yet; it shows raw `BuyerRecord` rows via
  `DiscoveryService`. That's deliberate, not an oversight.
- Two canonical acquisition contracts only: `BaseConnector` (local/file
  sources) and `PublicSourceAdapter` (external web/API sources).
  `MarketplaceProvider` is un-adopted; don't build on it without asking.
- Full decision history: `docs/decisions/*.md`. Read these before
  proposing a new abstraction — check whether it was already tried,
  rejected, or deferred for a reason.

## Working style

- PowerShell-first. Complete, copy-paste-ready commands — full file
  contents, not diffs/snippets, unless asked otherwise.
- Explain what we're building and why before/while writing code. I'm
  learning software engineering through this project, not just receiving
  code.
- Check my understanding by asking me to explain something back in my own
  words — not "does this make sense?"
- No new abstraction until 2 real, different implementations justify it.
- One capability at a time: design -> implement -> test -> explain ->
  verify green -> commit. Don't batch unrelated changes together.
- **A fix isn't real until it's committed and pushed to `main`.** A
  working-tree change or a file handed to me is not durable — this
  already caused one regression (adr-0007's fix was lost when the repo
  was recreated because it was never committed).

## Quality gates

`.\scripts\02-quality-gates.ps1` — pytest, mypy strict, ruff. Must be
green before considering any change done.
