"""
Fake Payment class object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import Dict
import numpy as np
from consistent_faker.utils import random_choice_non_normalized_weight_dict
from consistent_faker.weights.payments import DEFAULT_FINANCIAL_STATUS_WEIGHTS
from consistent_faker.weights.payments import DEFAULT_PAYMENT_METHOD_WEIGHTS
from consistent_faker.classes import FakeBaseObject


class FakePayment(FakeBaseObject):
    """
    Generate a semi random Fake Payment object

    Parameters
    -----------
    uid:                Optional[uuid.UUID]
    config:             Optional[Dict], configuration dictionary parameter
    financial_status:   Optional[str], the financial status (paid, pending..)
        of the transaction
    payment_method:     Optional[str], the payment method used for the
        transaction (visa, cod, direct_debit...)

    Examples
    -----------
    >>>FakePayment()
    FakePayment(uid=99b35936-52c4-4cc3-95cf-bb7feeb8e92d,
        financial_status=paid, payment_method=cod)
    >>>FakePayment(financial_status="pending")
    FakePayment(uid=99z38832-91c3-4rc3-04cf-bc2fkxb3e78i,
        financial_status=pending, payment_method=visa)
    """

    def __init__(self, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config", {})
        self.payment_cfg = self.config.get("payment", {}) if self.config else {}
        self._financial_status = self._init_financial_status(
            financial_status=kwargs.get("financial_status")
        )
        self._payment_method = self._init_payment_method(
            payment_method=kwargs.get("payment_method")
        )

    def __repr__(self):
        repr_str = (
            f"FakePayment(uid={self.uid}, financial_status={self.financial_status}, "
            + f"payment_method={self.payment_method})"
        )
        return repr_str

    @property
    def financial_status(self) -> np.str_:
        """
        str: Financial status
        eg: paid, pending
        """
        return np.str_(self._financial_status)

    @property
    def payment_method(self) -> np.str_:
        """
        str: payment method information
        eg: visa, mastercard, paypal
        """
        return np.str_(self._payment_method)

    def to_dict(self) -> Dict:
        """
        Serialize the fake payment object to a dictionary
        """
        product_variant_dict = {
            "uid": str(self.uid),
            "financial_status": self.financial_status,
            "payment_method": self.payment_method,
        }
        return product_variant_dict

    def _init_financial_status(self, financial_status: str = None) -> np.str_:
        if financial_status and isinstance(financial_status, str):
            return financial_status
        if financial_status:
            raise TypeError("financial_status kwarg should be an instance of str")
        weights = self.payment_cfg.get(
            "financial_status_weights", DEFAULT_FINANCIAL_STATUS_WEIGHTS
        )
        return random_choice_non_normalized_weight_dict(weights)

    def _init_payment_method(self, payment_method: str = None) -> np.str_:
        if payment_method and isinstance(payment_method, str):
            return payment_method
        if payment_method:
            raise TypeError("payment_method kwarg should be an instance of str")
        weights = self.payment_cfg.get(
            "payment_method_weights", DEFAULT_PAYMENT_METHOD_WEIGHTS
        )
        return random_choice_non_normalized_weight_dict(weights)
