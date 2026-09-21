import unittest

from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):
    def test_init_sets_member_id_and_zero_total_owed(self):
        fine = DuckFine("member-42")

        self.assertEqual(fine.member_id, "member-42")
        self.assertEqual(fine.total_owed, 0.0)

    def test_charge_returns_zero_within_grace_period(self):
        fine = DuckFine("member-1")

        result = fine.charge(2)

        self.assertEqual(result, 0.0)
        self.assertEqual(fine.total_owed, 0.0)

    def test_charge_applies_daily_fee_after_grace_period(self):
        fine = DuckFine("member-2")


        result = fine.charge(5)

        self.assertEqual(result, 1.5)
        self.assertEqual(fine.total_owed, 1.5)

    def test_charge_caps_fee_at_maximum(self):
        fine = DuckFine("member-3")

        result = fine.charge(100)

        self.assertEqual(result, DuckFine.MAX_FEE)
        self.assertEqual(fine.total_owed, DuckFine.MAX_FEE)

    def test_charge_deluxe_doubles_fee_before_cap(self):
        fine = DuckFine("member-4")

        result = fine.charge(6, deluxe=True)

        self.assertEqual(result, 4.0)
        self.assertEqual(fine.total_owed, 4.0)

    def test_charge_deluxe_is_capped_at_maximum(self):
        fine = DuckFine("member-5")

        result = fine.charge(100, deluxe=True)

        self.assertEqual(result, DuckFine.MAX_FEE)
        self.assertEqual(fine.total_owed, DuckFine.MAX_FEE)

    def test_charge_rejects_negative_days_late(self):
        fine = DuckFine("member-6")

        with self.assertRaisesRegex(ValueError, "days_late must not be negative"):
            fine.charge(-1)


if __name__ == "__main__":
    unittest.main()
