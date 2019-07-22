"""
Default weights for payment methods. These weights are used to randomly
generate payment meethods withinm the Fake payment object
"""
DEFAULT_PAYMENT_METHOD_WEIGHTS = {
    "visa": 0.3,
    "mastercard": 0.3,
    "paypal": 0.2,
    "direct_debit": 0.1,
    "cod": 0.1,  # cash on delivery
}
