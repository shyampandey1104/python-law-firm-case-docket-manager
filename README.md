# Python Law Firm Case Docket & Court Hearing Manager ⚖️📜

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

A LegalTech litigation case docket management, Indian e-Courts CNR number tracking, hearing causelist diary, and advocate professional fee billing system. Built in Python for law chambers, senior advocates, and corporate legal departments.

---

## 🚀 Key Features

- **16-Digit CNR Number Standardization**: Tracks case numbers conforming to Indian High Courts & District Courts e-Courts schema.
- **Hearing Timeline & Cause List Diary**: Records court room numbers, presiding judges, arguments, and interim orders.
- **Professional Advocate Fee Billing**: Combines hourly research billing, senior counsel appearance fees, and standard 10% clerkage disbursements.
- **Limitation Period & Deadline Alerts**: Helps legal teams prevent missed limitation deadlines for filing appeals and writ petitions.

---

## 📦 Installation & Setup

```bash
git clone https://github.com/shyampandey1104/python-law-firm-case-docket-manager.git
cd python-law-firm-case-docket-manager
pip install -r requirements.txt
```

---

## 🛠️ Usage Example

```python
from legal.engine import LawFirmDocketEngine, LegalCase, CourtHearing

engine = LawFirmDocketEngine("Trilegal Chambers")

case = LegalCase(
    cnr_number="DLHC010022332025",
    case_title="Bharat Retail vs Union of India",
    court_name="Delhi High Court",
    client_name="Bharat Retail Ltd",
    opposing_party="Union of India",
    lead_advocate="Adv. Shyam Pandey",
    hourly_rate=4500.0,
    court_appearance_fee=20000.0
)
engine.register_case(case)

# Record research time
engine.log_billable_hours("DLHC010022332025", 8.0)

# Generate fee invoice
inv = engine.generate_client_invoice("DLHC010022332025")
print(f"Grand Total Fee: ₹{inv['grand_total']} (Includes 10% Clerkage)")
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📄 License
MIT License. Created with ❤️ by [Shyam Pandey](https://github.com/shyampandey1104).
