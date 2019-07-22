"""
REPR Promotion formats
"""
COUPON_PROMOTION_REPR = (
    "FakePromotion(type=Coupon, "
    + "dicount_code={discount_code},"
    + " value_type={value_type}, value={value})"
)
NO_PROMOTION_REPR = "FakePromotion(type=no_promotion)"
OTHER_PROMOTION_REPR = (
    "FakePromotion(type={type}, value_type={value_type}, value={value})"
)
