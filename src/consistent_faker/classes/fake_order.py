"""
Fake Order class object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import List, Dict, Optional
from datetime import datetime
from faker import Faker
import numpy as np
import pandas as pd
from consistent_faker.builders.fake_order_item_builder import FakeOrderItemBuilder
from consistent_faker.classes import FakePromotion, FakeCustomer, FakeAddress
from consistent_faker.classes import FakePayment, FakeBaseObject
from consistent_faker.utils import random_choice_weight_dict
from consistent_faker.weights.orders import DEFAULT_ADDRESS_CONFIGURATION_WEIGHTS

FAKE = Faker()


class FakeOrder(FakeBaseObject):
    """
    Generates consistent fake orders

    Parameters
    -----------
    uid:                Optional[uuid.UUID], the assigned order id
    customer:           Optional[FakeCustomer], customer object for which
        to generate the fake order
    config:             Optional[Dict], configuration dictionary
    variants:           Optional[Dict[FakeProductVariants, float]],
        which would contain the products to use to generate the orders
    order_items_cnt:    To be implemented
    order_items:        To be implemented
    ts:                 To be implemented
    shipping_address:   To be implemented
    billing_address:    To be implemented
    promotion:          To be implemented
    shipping_fee_incl_taxes: To be implemented
    payment:            To be implemented

    Examples
    -----------
    Constructing a random fake order
    >>> FakeOrder()
    FakeOrder('4814755c-bdcb-4f1a-a6f4-39214855fd11',
    'FakeCustomer(uid=db8c0ef4-9f60-422d-9d7b-2762b743286f,
    gender=F, first_name=Carolyn, last_name=Young)', 3)

    Constructing a fake order for a given customer
    >>> this_customer = FakeCustomer()
    >>> this_customer
    FakeCustomer(uid=9cddad32-a1eb-4832-a4bc-1e62ca2a2d1c, gender=M,
    first_name=Jose, last_name=Ramsey)
    >>> FakeOrder(customer=this_customer)
    FakeOrder('7cbd4b75-3311-4c0d-a785-10e589acf41d',
    'FakeCustomer(uid=9cddad32-a1eb-4832-a4bc-1e62ca2a2d1c,
    gender=M, first_name=Jose, last_name=Ramsey)', 14)

    Constructing a fake orders based on a defined set of products
    >>> this_variants = dict(
        (FakeProductVariant(), np.random.rand())
        for x in range(0,1)
        )
    >>> this_variants
    {FakeProductVariant(sku=FakeSku(ean=3664982106081, title=information),
    uid=01603c4f-f82b-482b-b380-982eaca3df54, price_incl_taxes=83.63): 0.7554435868936881}
    >>>FakeOrder(variants=this_variants).order_items[0].product_variant
    FakeProductVariant(sku=FakeSku(ean=3664982106081, title=information),
    uid=01603c4f-f82b-482b-b380-982eaca3df54, price_incl_taxes=83.63)

    TODO:
        Add specific kwargs initialization
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, customer: Optional[FakeCustomer] = None, **kwargs):
        """
        TODO PLACEHOLDER DOCSTRING FOR INIT
        """
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config", {})
        self._variants = kwargs.get("variants")

        self._customer = self._init_customer(customer)

        # generates a shipping and billing address
        self.shipping_addresses_cfg = self._init_addresses_configuration()
        self.billing_addresses_cfg = self._init_addresses_configuration()

        # initiating order Items
        self._order_items_cnt = self._init_order_item_cnt()
        self._order_items = self._init_order_items()

        # setting up a random time within an interval
        self._timestamp = self._init_ts()

        # setting up the shipping and billing address
        self._shipping_address = self._init_address(self.shipping_addresses_cfg)
        self._billing_address = self._init_address(self.billing_addresses_cfg)

        # initiating the Promotion Object
        self._promotion = self._init_promotion()

        # calculate order items aggregates
        self._total_product_price_incl_taxes = self._calc_total_product_price_incl()
        self._total_product_quantity = self._calc_total_product_quantity()

        # calculate the discount amount
        self._discount_amount = self.promotion.calc(self)
        # TODO Shipping fee
        self._shipping_fee_incl_taxes = np.float64(0)

        # total order price
        self._total_price = self._calc_total_price()

        # setting up the payment object
        self._payment = FakePayment()

    def __repr__(self):
        return "FakeOrder('%s', '%s', %i)" % (
            self.uid,
            self.customer,
            self.order_items_cnt,
        )

    @property
    def timestamp(self) -> datetime:
        """datetime: The datetime of creation of the order"""
        return self._timestamp

    @property
    def customer(self) -> FakeCustomer:
        """FakeCustomer: The Customer Associated with the order"""
        return self._customer

    @property
    def order_items_cnt(self) -> int:
        """int: The Number of unique distinct order items in the order"""
        return self._order_items_cnt

    @property
    def order_items(self) -> List:
        """List[FakeOrderItem]: All order Items Associated with the order"""
        return self._order_items

    @property
    def shipping_address(self) -> FakeAddress:
        """FakeAddress: The Shipping Address associated with the order"""
        return self._shipping_address

    @property
    def billing_address(self) -> FakeAddress:
        """FakeAddress: The Billing Address asscoiated with the order"""
        return self._billing_address

    @property
    def promotion(self) -> FakePromotion:
        """FakePromotion: The promotion object associated with the order"""
        return self._promotion

    @property
    def total_product_price_incl_taxes(self) -> np.float64:
        """
        np.float64: The total product price including taxes
        the price is excluding of any discount or shipping fee
        """
        return self._total_product_price_incl_taxes

    @property
    def total_product_quantity(self) -> np.int64:
        """int: quantity of all products contained within the order"""
        return self._total_product_quantity

    @property
    def shipping_fee_incl_taxes(self) -> np.float64:
        """np.float64 : The total sheeping fees including taxes for the order"""
        return self._shipping_fee_incl_taxes

    @property
    def discount_amount(self) -> np.float64:
        """np.float64: discount amount associated with the order"""
        return self._discount_amount

    @property
    def total_price(self) -> np.float64:
        """np.float64: total price to be paid by the customer"""
        return self._total_price

    @property
    def payment(self) -> FakePayment:
        """FakePayment"""
        return self._payment

    def to_dict(self) -> Dict:
        """
        Serialize the fake order object to a dictionary
        """
        order_dict = {
            "uid": str(self.uid),
            "customer": self.customer.to_dict(),
            "timestamp": self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "promotion": self.promotion.to_dict(),
            "order_items_cnt": self.order_items_cnt,
            "order_items": [oi.to_dict() for oi in self.order_items],
            "total_price": self.total_price,
            "total_product_price_incl_taxes": self.total_product_price_incl_taxes,
            "shipping_fee_incl_taxes": self.shipping_fee_incl_taxes,
            "discount_amount": self.discount_amount,
            "total_product_quantity": int(self.total_product_quantity),
            "shipping_address": self.shipping_address.to_dict(),
            "billing_address": self.billing_address.to_dict(),
            "payment": self.payment.to_dict(),
        }
        return order_dict

    @classmethod
    def to_dataframe(cls) -> pd.DataFrame:
        """
        Converts the fake order object to a pandas dataframe
        NOT IMPLEMENTED
        """
        return NotImplemented

    def _init_addresses_configuration(self) -> str:
        """
        Randomly selects an address configuration type out of, Customer's
        default address, a new address for the customer and a random address

        Returns:
            str: the key associated to the selected address config
        """
        order_config = self.config.get("orders", {}) if self.config else {}
        weights = order_config.get(
            "address_configuration_weights",
            DEFAULT_ADDRESS_CONFIGURATION_WEIGHTS
        )
        return random_choice_weight_dict(weights)

    def _init_address(self, address_cfg) -> FakeAddress:
        """
        Generate an Address for the Customer

        Returns:
            FakeAddress: an address generated based on the configuration either
            return's the customer's default address a new address with ties to
            the customer or a totally random address
        """
        if address_cfg == "usr_default":
            return self.customer.default_address
        if address_cfg == "usr_random":
            return FakeAddress(customer=self.customer, config=self.config)
        return FakeAddress(config=self.config)

    def _init_customer(self, customer):
        """
        Generate a Fake Customer if not provided as an argument
        """
        if customer and isinstance(customer, FakeCustomer):
            return customer
        if customer:
            raise TypeError("Customer Should be an instance of FakeCustomer")
        return FakeCustomer(config=self.config)

    def _init_order_item_cnt(self):
        """
        Generate a random order item count
        """
        # defining the default Variables
        order_config = self.config.get("orders", {}) if self.config else {}
        order_items_cnt_cfg = order_config.get("order_items_cnt", {})
        order_items_min = order_items_cnt_cfg.get("min", 1)
        order_items_max = order_items_cnt_cfg.get("max", 3)
        return np.random.randint(low=order_items_min, high=order_items_max)

    def _init_order_items(self):
        return FakeOrderItemBuilder(
            self.order_items_cnt, config=self.config, variants=self._variants
        ).build()

    def _init_ts(self):
        config = self.config
        start_ts = datetime.strptime(
            config.get("start_ts", "2010-01-01"), "%Y-%m-%d"
        )
        end_ts = datetime.strptime(
            config.get("end_ts", "2020-01-01"), "%Y-%m-%d"
        )
        return FAKE.format("date_time_ad",
                           tzinfo=None, end_datetime=end_ts, start_datetime=start_ts
                           )

    def _init_promotion(self) -> FakePromotion:
        return FakePromotion(config=self.config)

    def _calc_total_product_price_incl(self) -> np.float64:
        """
        Calculates the aggregate prices for all order items in an order

        Returns:
            np.float64: The aggregated prince including taxes for all products
            in the order calculated as SUM(Variant Price Incl Taxes * Quantity)
        """
        order_item_prices_incl_taxes = [
            order_item.product_quantity for order_item in self.order_items
        ]
        total_product_price_incl_taxes = np.sum(
            order_item_prices_incl_taxes, dtype=np.float64
        )
        return total_product_price_incl_taxes

    def _calc_total_product_quantity(self) -> np.int64:
        """
        Calculates the total number of items in the order

        Returns:
            np.int64: The total quantity of products in the order
        """
        order_items_quantity = [
            order_item.product_quantity for order_item in self.order_items
        ]
        return np.sum(order_items_quantity)

    def _calc_total_price(self) -> np.float64:
        """
        Calculates the total price to be paid by the customer after discount
        as such the price needs to be positive

        Returns:
            np.float64: total price paid by the customer
        """
        return max(
            np.float64(0),
            self.total_product_price_incl_taxes
            - self.discount_amount
            + self.shipping_fee_incl_taxes,
        )
