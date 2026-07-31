import unittest
from pathlib import Path

from scripts.verify_cards import replication_cards, validate, validate_paper_card


class ReplicationCardTests(unittest.TestCase):
    def test_public_cards_have_evidence_boundaries(self):
        cards = replication_cards()
        self.assertGreaterEqual(len(cards), 5)
        for card in cards:
            with self.subTest(card=card):
                self.assertEqual(validate(card), [])

    def test_metadata_cards_are_machine_checkable(self):
        cards = sorted(Path("paper_cards").glob("*.json"))
        self.assertGreaterEqual(len(cards), 5)
        for card in cards:
            with self.subTest(card=card):
                self.assertEqual(validate_paper_card(card), [])


if __name__ == "__main__":
    unittest.main()
