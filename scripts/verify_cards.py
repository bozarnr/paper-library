"""Static contract checks for public replication cards and paper metadata."""

import json
from pathlib import Path

REQUIRED_SECTIONS = (
    "## Source",
    "## Reproduction scope",
    "## Expected versus observed",
    "## Deviations and limits",
    "## Reproduction verdict",
)


def replication_cards(root: Path = Path("reproductions")) -> list[Path]:
    return sorted(card for card in root.glob("*.md") if card.name != "index.md")


def validate(card: Path) -> list[str]:
    text = card.read_text(encoding="utf-8")
    return [section for section in REQUIRED_SECTIONS if section not in text]


def validate_paper_card(card: Path, schema: Path = Path("schemas/paper_card_schema.json")) -> list[str]:
    payload = json.loads(card.read_text(encoding="utf-8"))
    rules = json.loads(schema.read_text(encoding="utf-8"))
    errors: list[str] = []
    for key in rules["required"]:
        if key not in payload:
            errors.append(f"missing key: {key}")
    if payload.get("implementation_status") not in rules["allowed_status"]:
        errors.append("invalid implementation_status")
    if payload.get("replication_status") not in rules["allowed_status"]:
        errors.append("invalid replication_status")
    if payload.get("claim_ceiling") not in rules["allowed_claim_ceiling"]:
        errors.append("invalid claim_ceiling")
    for evidence in payload.get("evidence_files", []):
        if not Path(evidence).exists():
            errors.append(f"missing evidence file: {evidence}")
    return errors


def main() -> None:
    cards = replication_cards()
    if not cards:
        raise SystemExit("no public replication cards found")
    failures = {str(card): validate(card) for card in cards if validate(card)}
    paper_cards = sorted(Path("paper_cards").glob("*.json"))
    if not paper_cards:
        raise SystemExit("no machine-readable paper cards found")
    paper_failures = {str(card): validate_paper_card(card) for card in paper_cards if validate_paper_card(card)}
    if failures:
        raise SystemExit(f"incomplete cards: {failures}")
    if paper_failures:
        raise SystemExit(f"incomplete paper cards: {paper_failures}")
    print(f"verified {len(cards)} replication card(s) and {len(paper_cards)} paper metadata card(s)")


if __name__ == "__main__":
    main()
