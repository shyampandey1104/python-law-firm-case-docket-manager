"""Law Firm Case Docket, CNR Tracker, Hearing Timeline & Advocate Billing Engine."""

from datetime import datetime, date
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class CourtHearing(BaseModel):
    hearing_id: str
    hearing_date: str  # YYYY-MM-DD
    court_room: str
    judge_name: str
    stage_of_case: str  # Evidence, Arguments, Framing of Issues, Cross-Examination, Judgment
    advocate_appeared: str
    hearing_outcome: Optional[str] = None
    next_hearing_date: Optional[str] = None


class LegalCase(BaseModel):
    cnr_number: str  # 16-character Case Number Record (e.g., DLHC010012342024)
    case_title: str  # e.g., "ABC Corp vs XYZ Ltd"
    court_name: str  # Supreme Court of India, Delhi High Court, NCLT Delhi
    client_name: str
    opposing_party: str
    lead_advocate: str
    hourly_rate: float = 4000.0
    court_appearance_fee: float = 15000.0
    hearings: List[CourtHearing] = Field(default_factory=list)
    billable_hours_spent: float = 0.0
    status: str = "PENDING"  # PENDING, DISPOSED, WITHDRAWN, DECREED


class LawFirmDocketEngine:
    """Manages legal court dockets, limitation deadlines, and advocate billing."""

    def __init__(self, firm_name: str = "Lex Chambers & Associates"):
        self.firm_name = firm_name
        self.cases: Dict[str, LegalCase] = {}

    def register_case(self, case: LegalCase) -> LegalCase:
        if len(case.cnr_number) != 16:
            raise ValueError("Standard Indian CNR number must be exactly 16 characters.")
        self.cases[case.cnr_number] = case
        return case

    def log_hearing(self, cnr_number: str, hearing: CourtHearing) -> CourtHearing:
        case = self.cases.get(cnr_number)
        if not case:
            raise ValueError(f"Case with CNR {cnr_number} not found.")

        case.hearings.append(hearing)
        return hearing

    def log_billable_hours(self, cnr_number: str, hours: float) -> float:
        case = self.cases.get(cnr_number)
        if not case:
            raise ValueError("Case not found.")
        case.billable_hours_spent += hours
        return case.billable_hours_spent

    def generate_client_invoice(self, cnr_number: str) -> Dict[str, Any]:
        """Calculates total legal fees: billable hours research + court appearance retainers."""
        case = self.cases.get(cnr_number)
        if not case:
            raise ValueError("Case not found.")

        hourly_charge = case.billable_hours_spent * case.hourly_rate
        appearances_count = len(case.hearings)
        appearance_fee_total = appearances_count * case.court_appearance_fee
        total_professional_fee = hourly_charge + appearance_fee_total
        clerkage_expense = total_professional_fee * 0.10  # 10% standard advocate clerkage
        grand_total = total_professional_fee + clerkage_expense

        return {
            "firm_name": self.firm_name,
            "cnr_number": case.cnr_number,
            "case_title": case.case_title,
            "client_name": case.client_name,
            "court": case.court_name,
            "billable_hours": case.billable_hours_spent,
            "hourly_fee": round(hourly_charge, 2),
            "hearings_count": appearances_count,
            "appearance_fees": round(appearance_fee_total, 2),
            "clerkage_10pct": round(clerkage_expense, 2),
            "grand_total": round(grand_total, 2),
            "status": case.status
        }
