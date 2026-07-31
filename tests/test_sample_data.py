import csv
import unittest
from pathlib import Path


class SampleDataTests(unittest.TestCase):
    def test_evidence_matrix_links_to_public_artifacts(self):
        with Path("sample_data/evidence_matrix_sample.csv").open(encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))

        self.assertEqual(len(rows), 5)
        for row in rows:
            with self.subTest(paper_id=row["paper_id"]):
                self.assertTrue(Path(row["public_artifact"]).exists())
                self.assertIn(row["claim_ceiling"], {"reading-note", "implemented", "replicated-partial", "replicated-strict"})


if __name__ == "__main__":
    unittest.main()
