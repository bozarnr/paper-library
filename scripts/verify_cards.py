"""Static contract checks for public replication cards."""

from pathlib import Path

REQUIRED_SECTIONS = (
    "## Source",
    "## Reproduction scope",
    "## Expected versus observed",
    "## Deviations and limits",
    "## Reproduction verdict",
)


def validate(card: Path) -> list[str]:
    text = card.read_text(encoding="utf-8")
    return [section for section in REQUIRED_SECTIONS if section not in text]


def main() -> None:
    cards = sorted(Path("reproductions").glob("*.md"))
    if not cards:
        raise SystemExit("no public replication cards found")
    failures = {str(card): validate(card) for card in cards if validate(card)}
    if failures:
        raise SystemExit(f"incomplete cards: {failures}")
    print(f"verified {len(cards)} replication card(s)")


if __name__ == "__main__":
    main()
