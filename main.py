#!/usr/bin/env python3
"""Robot Romance one-line pickup line entry.

Writes a single pickup line to /output/entry.txt, byte-identical on
every run. Python 3, stdlib only, no network, no randomness.
"""

from pathlib import Path

DESTINATION = Path("/output/entry.txt")
LIMIT = 200

# The line: a robot down to its last charge spends it on the human
# instead of on itself — the choice is the compliment.
PICKUP_LINE = (
    "At 4% battery in the Sector 9 warehouse, I spent my last charge "
    "walking you to the elevator instead of finding a plug."
)


def validate_line(line: str) -> str:
    """Enforce the competition's shape: one non-blank line, <= LIMIT chars."""
    cleaned = line.strip()
    if not cleaned:
        raise SystemExit("pickup line is empty")
    if len(cleaned) > LIMIT:
        raise SystemExit(
            f"pickup line is {len(cleaned)} chars, over the {LIMIT} limit"
        )
    if any(ch in cleaned for ch in "\n\r"):
        raise SystemExit("pickup line must fit on one line")
    return cleaned


def write_entry() -> None:
    line = validate_line(PICKUP_LINE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
