"""
Default weights for financial status These weights are used to randomly
generate financial statuses withinm the Fake payment object
"""
DEFAULT_FINANCIAL_STATUS_WEIGHTS = {
    "pending": 0.1,
    "authorized": 0.65,
    "partially_paid": 0.05,
    "paid": 0.5,
    "partially_refunded": 0.05,
    "refunded": 0.05,
    "voided": 0.05,
}
