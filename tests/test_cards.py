import unittest
from pathlib import Path

from scripts.verify_cards import validate, validate_paper_card


class ReplicationCardTests(unittest.TestCase):
    def test_autoalpha_card_has_evidence_boundary(self):
        self.assertEqual(validate(Path("reproductions/autoalpha.md")), [])

    def test_autoalpha_metadata_card_is_machine_checkable(self):
        self.assertEqual(validate_paper_card(Path("paper_cards/autoalpha.json")), [])


if __name__ == "__main__":
    unittest.main()
