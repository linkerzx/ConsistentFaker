"""
Fake Promotion classs definition

Copyright (c) 2019 Julien Kervizic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import Dict
import numpy as np
from faker import Faker
from consistent_faker.utils import random_choice_weight_dict
from consistent_faker.weights.promotions import DEFAULT_PROMOTION_TYPE_WEIGHTS
from consistent_faker.weights.promotions import DEFAULT_PROMOTION_VALUE_TYPE_WEIGHTS
from consistent_faker.classes import FakeBaseObject

FAKE = Faker()


class FakePromotion(FakeBaseObject):
    """
    Generate a fake promotion object, the promotion objects can impact pricing
    by setting up a discount level and can provide an applicable coupon code

    Parameters
    -----------
    config:         Optional[Dict]
    type:           Optional[str], coupon, no_promotion or discount
    value_type:     Optional[str], percentage or fixed_amount
    value:          Optional[float], the amount or percentage
        (as a number not a fraction) to be used for the discount/coupon
    discount_code:  Optional[str]
    discount_codes: Not implemented #random choice out of discount codes

    Examples
    -----------
    >>> FakePromotion()
    FakePromotion(type=no_promotion)
    >>> FakePromotion()
    FakePromotion(type=discount, value_type=percentage, value=32.0)


    TODO:
        make it so the fake promotion can import from a list of available coupon codes
    """

    def __init__(self, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config", {})
        self.promo_config = self.config.get("promotion", {}) if self.config else {}
        self._type = self._init_promotion_type(type_=kwargs.get("type"))
        self._value_type = self._init_promotion_value_type(
            value_type=kwargs.get("value_type")
        )
        self._value = self._init_promotion_value(value=kwargs.get("value"))
        self._discount_code = self._init_discount_code(
            discount_code=kwargs.get("discount_code")
        )

    def __repr__(self):
        if self.type == "coupon":
            repr_str = f"FakePromotion(type=Coupon, dicount_code={self.discount_code}, "
            repr_str += f"value_type={self.value_type}, value={self.value})"
        elif self.type == "no_promotion":
            repr_str = f"FakePromotion(type=no_promotion)"
        else:
            repr_str = f"FakePromotion(type={self.type}, value_type={self.value_type}, "
            repr_str += f"value={self.value})"
        return repr_str

    @property
    def discount_code(self) -> str:
        """
        Returns:
            str: discount code in case of coupon
            NULL otherwisee
        """
        return self._discount_code

    @property
    def value_type(self) -> np.str_:
        """
        str: value type of the promotion, ie: percentage or fixed amount
        """
        return self._value_type

    @property
    def value(self) -> np.float64:
        """
        np.float64: the value of the discount in numbers
        0.00 if not applied
        """
        return self._value * np.float64(1)

    @property
    def type(self) -> str:
        """
        str: the promotion type applying to the order
        """
        return self._type

    def to_dict(self) -> Dict:
        """
        Serialize the fake promotion object to a dictionary
        """
        if self.type == "no_promotion":
            promotion_dict = {}
        else:
            promotion_dict = {
                "type": self.type,
                "value": self.value,
                "value_type": self.value_type,
            }
            if self.type == "coupon":
                promotion_dict.update({"discount_code": self.discount_code})
        return promotion_dict

    def calc(self, order) -> np.float64:
        """np.float64"""
        return self._calc(order)

    def _init_promotion_type(self, type_: str = None) -> str:
        """
        Assign or randomly generate a promotion type based on a weghted dict

        Returns:
            str: The key of the dictionary
        """
        if type_ and isinstance(type_, str):
            if type_ in {"coupon", "discount", "no_promotion"}:
                return type_
            raise ValueError(
                "type should be either coupon, discount or no_promotion"
            )
        if type_:
            raise TypeError("type kwarg should be an instance of str")
        weights = self.promo_config.get(
            "promotion_type_weights", DEFAULT_PROMOTION_TYPE_WEIGHTS
        )
        return random_choice_weight_dict(weights)

    def _init_promotion_value_type(self, value_type: str = None) -> str:
        """
        Returns:
            str: key promotion value type
        """
        if value_type and isinstance(value_type, str):
            return value_type
        if value_type:
            raise TypeError("value_type kwarg should be an instance of str")
        weights = self.promo_config.get(
            "promotion_value_type_weights", DEFAULT_PROMOTION_VALUE_TYPE_WEIGHTS
        )
        return random_choice_weight_dict(weights)

    def _init_promotion_value(self, value: float = None) -> np.float64:
        """
        Assign a discount value when the promotion type is valid

        Returns:
            np.float64: discount

        """
        if value and isinstance(value, float):
            return value * np.float64(1)
        if value:
            raise TypeError("value kwarg should be an instance of float")
        if self.value_type == "percentage":
            promotion_value_percentage_cfg = self.promo_config.get(
                "promotion_value_percentage", {}
            )
            min_value_pct = promotion_value_percentage_cfg.get("min", 1)
            max_value_pct = promotion_value_percentage_cfg.get("max", 70)

            promotion_value = np.random.randint(
                low=min_value_pct, high=max_value_pct
            )
        elif self.value_type == "fixed_amount":
            promotion_value_fixed_cfg = self.promo_config.get(
                "promotion_value_fixed_amount", {}
            )
            min_value_fix = promotion_value_fixed_cfg.get("min", 1)
            max_value_fix = promotion_value_fixed_cfg.get("max", 15)

            promotion_value = np.random.randint(
                low=min_value_fix, high=max_value_fix
            )
        else:
            promotion_value = None
        return promotion_value * np.float64(1.0)

    def _init_discount_code(self, discount_code: str = None) -> str:
        """
        Generate a discount code when the promotion is a coupon

        Returns:
            str: the discount code
        """
        if discount_code and isinstance(discount_code, str):
            return discount_code
        if discount_code:
            raise TypeError("discount_code kwarg should be an instance of str")
        if self.type == "coupon":
            # TODO add mix of letters and numbers
            # TODO supports Global Discount code application
            discount_code = "".join(FAKE.format('random_letters', length=16))
        else:
            discount_code = None
        return discount_code

    def _calc(self, order: FakeBaseObject = None) -> np.float64:
        """
        Calculates the discount amount based on product price,
        And type of discount

        Returns:
            float64: with the order  discount amount
        """
        if self.type != "no_promotion":
            total_product_price = order.total_product_price_incl_taxes * np.float64(1.0)
            if self.value_type == "percentage":
                return (
                    total_product_price * order.promotion.value / 100 * np.float64(1.0)
                )
            if self.value_type == "fixed_amount":
                return min(total_product_price, self.value) * np.float64(1.0)
        return 0.00 * np.float64(1.0)
