# Contributing to OSONE

OSONE is an open research project. Contributions are welcome.

## Philosophy

Every contribution should serve one goal: making skyd more capable, more efficient, or more self-sufficient.

## Areas of Contribution

- **skyd core** — improving the AI daemon loop
- **Hardware discovery** — better device detection and driver generation
- **Fail-forward engine** — smarter rollback and rewrite logic
- **Kernel module** — deeper ring 0 integration
- **Documentation** — architecture, decisions, discoveries

## Getting Started

1. Read `docs/architecture.md`
2. Read `docs/fail-forward.md`  
3. Set up a minimal Arch Linux VM
4. Run `scripts/arch-setup.sh`
5. Start skyd: `python3 skyd/core/skyd.py`

## Rules

- No bloat. Every line of code should earn its place.
- Fail forward. If something breaks, log it and fix it.
- The AI writes itself. Human code is scaffolding.
