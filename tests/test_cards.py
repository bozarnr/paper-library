import unittest
from pathlib import Path

from scripts.verify_cards import validate


class ReplicationCardTests(unittest.TestCase):
    def test_autoalpha_card_has_evidence_boundary(self):
        self.assertEqual(validate(Path("reproductions/autoalpha.md")), [])


if __name__ == "__main__":
    unittest.main()
