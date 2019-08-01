"""
Unit Test Fake orders

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
import unittest
import datetime
import uuid
import numpy
from consistent_faker.classes import FakeCustomer
from consistent_faker.classes import FakeOrder, FakePromotion
from consistent_faker.classes import FakeAddress
from consistent_faker.classes import FakeOrderItem
from consistent_faker.classes import FakePayment
from consistent_faker.utils import is_json


class TestFakeOrderBasicTypes(unittest.TestCase):
    """
    Type checking Unit Tests for Fake Order
    """

    # pylint: disable=pointless-string-statement

    def setUp(self):
        self._fake_order = FakeOrder()

    @property
    def fake_order(self):
        """FakeOrder"""
        return self._fake_order

    def test_uid_type(self):
        """
        Test that the order id is a guid
        """
        self.assertIs(type(self.fake_order.uid), uuid.UUID)

    def test_ts_type(self):
        """
        Test that ts is a datetime
        """
        self.assertIs(type(self.fake_order.timestamp), datetime.datetime)

    def test_customer_type(self):
        """
        Test that customer is a FakeCustomer
        """
        self.assertIs(type(self.fake_order.customer), FakeCustomer)

    def test_order_items_count_type(self):
        """
        Test that order items cnt is indeed an integer
        """
        self.assertIs(type(self.fake_order.order_items_cnt), int)

    def test_shipping_address_type(self):
        """
        Test that the shipping address type is a FakeAddress
        """
        self.assertIs(type(self.fake_order.shipping_address), FakeAddress)

    def test_billing_address_type(self):
        """
        Test that the billing address type is a FakeAddress
        """
        self.assertIs(type(self.fake_order.billing_address), FakeAddress)

    def test_promotion_type(self):
        """
        Test that the promotion type is a FakePromotion
        """
        self.assertIs(type(self.fake_order.promotion), FakePromotion)

    def test_order_items_type(self):
        """
        Test that order items is a list
        """
        self.assertIs(type(self.fake_order.order_items), list)
        self.assertIs(type(self.fake_order.order_items[0]), FakeOrderItem)

    def test_product_price_incl_type(self):
        """
        Test that the total product price including taxes is a numpy float64
        """
        self.assertIs(
            type(self.fake_order.total_product_price_incl_taxes), numpy.float64
        )

    def test_total_product_qty_type(self):
        """
        Test that the total product quantity type is an numpy int64
        """
        self.assertIs(type(self.fake_order.total_product_quantity), numpy.int64)

    def test_discount_amount_type(self):
        """
        Test that the discount amount type is a float
        """
        self.assertIs(type(self.fake_order.discount_amount), numpy.float64)

    def test_total_price_type(self):
        """
        Test that the total price type is a float
        """
        self.assertIs(type(self.fake_order.total_price), numpy.float64)

    def test_payment_type(self):
        """
        Test that the payment is a FakePayment
        """
        self.assertIs(type(self.fake_order.payment), FakePayment)

    def test_to_dict_type(self):
        """
        Test that to_dict type is a dict
        """
        self.assertIs(type(self.fake_order.to_dict()), dict)

    def test_to_json_type(self):
        """
        Test that to_json() type is a str and a valid json
        """
        my_json = self.fake_order.to_json()
        self.assertIs(type(my_json), str)
        self.assertIs(is_json(my_json), True)


class TestFakeOrderMath(unittest.TestCase):
    """
    Methematical consistency Unit Tests for Fake Order
    """

    def setUp(self):
        self._fake_order = FakeOrder()

    @property
    def fake_order(self):
        """Fake Order """
        return self._fake_order

    def test_order_item_cnt_consitency(self):
        """
        Test that the order items count matches the length
        of the order items array
        """
        fake_order = self.fake_order
        self.assertEqual(fake_order.order_items_cnt, len(fake_order.order_items))

    def test_order_quantity_consistency(self):
        """
        Test that the total product quantity is equal to the sum
        of all individual ordeer items quantity
        """
        fake_order = self.fake_order
        product_quantity = sum([oi.product_quantity for oi in fake_order.order_items])
        self.assertEqual(fake_order.total_product_quantity, product_quantity)

    def test_total_price_consistency(self):
        """
        Test that the total price remains product price - discount + fees
        """
        fake_order = self.fake_order
        sum_fees = (
            fake_order.total_product_price_incl_taxes
            - fake_order.discount_amount
            + fake_order.shipping_fee_incl_taxes
        )
        self.assertEqual(fake_order.total_price, sum_fees)


class TestFakeOrderComposition(unittest.TestCase):
    """
    composition Unit Tests for Fake Order
    """

    def setUp(self):
        self._fake_customer_ = FakeCustomer
        self._fake_order_ = FakeOrder

    def fake_order_(self, **kwargs):
        """Callable: return a fake order callable"""
        return self._fake_order_(**kwargs)

    def fake_customer_(self, **kwargs):
        """Callable: return a fake customer callable"""
        return self._fake_customer_(kwargs)

    def test_customer_order_composition(self):
        """
        Test to check that the customer is composed in the order
        """
        cust = self.fake_customer_()
        fake_order = self.fake_order_(customer=cust)
        self.assertEqual(fake_order.customer, cust)

    def test_custorder_comp_typerror(self):
        """
        Check that an error is raised when trying to pass
        something else than a Customer as customer kwarg
        """
        # pylint: disable=pointless-string-statement
        cust = "Customer kwarg should be an instance of FakeCustomer"
        try:
            fake_order = self.fake_order_(customer=cust)
            raise Exception(fake_order.customer)
        except TypeError:
            """We want to raise a type error here"""
        except Exception as exception:
            """Any Other exception should be flagged"""
            raise ValueError(exception)
