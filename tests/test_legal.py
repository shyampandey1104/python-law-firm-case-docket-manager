import unittest
from legal.engine import LawFirmDocketEngine, LegalCase, CourtHearing


class TestLawFirmDocketEngine(unittest.TestCase):
    def setUp(self):
        self.engine = LawFirmDocketEngine()
        self.case = LegalCase(
            cnr_number="DLHC010099882024",  # 16 chars
            case_title="Sunrise Infra vs State of Delhi",
            court_name="High Court of Delhi",
            client_name="Sunrise Infrastructure Pvt Ltd",
            opposing_party="State of Delhi",
            lead_advocate="Adv. Shyam Pandey",
            hourly_rate=5000.0,
            court_appearance_fee=25000.0
        )
        self.engine.register_case(self.case)

    def test_case_logging_and_invoice(self):
        # Log a hearing
        self.engine.log_hearing("DLHC010099882024", CourtHearing(
            hearing_id="H-01",
            hearing_date="2026-04-12",
            court_room="Court 14",
            judge_name="Hon'ble Justice K. Sharma",
            stage_of_case="Final Arguments",
            advocate_appeared="Adv. Shyam Pandey",
            next_hearing_date="2026-05-10"
        ))

        # Log 10 billable research hours
        self.engine.log_billable_hours("DLHC010099882024", 10.0)

        # Generate invoice
        # Hourly: 10 * 5000 = 50,000
        # Appearance: 1 * 25,000 = 25,000
        # Total Prof: 75,000 + 10% Clerkage (7,500) = 82,500
        invoice = self.engine.generate_client_invoice("DLHC010099882024")
        self.assertEqual(invoice["billable_hours"], 10.0)
        self.assertEqual(invoice["appearance_fees"], 25000.0)
        self.assertEqual(invoice["clerkage_10pct"], 7500.0)
        self.assertEqual(invoice["grand_total"], 82500.0)


if __name__ == "__main__":
    unittest.main()
