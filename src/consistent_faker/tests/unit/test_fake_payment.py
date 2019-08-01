"""
Unit tests for Fake Payment

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
import uuid
import numpy
from consistent_faker.classes import FakePayment


class TestFakePayment(unittest.TestCase):
    """
    Unit tests for Fake Payment
    """

    def setUp(self):
        self._fake_payment = FakePayment()

    @property
    def fake_payment(self):
        """FakePayement"""
        return self._fake_payment

    def test_uid_type(self):
        """
        Test that the uid is a guid
        """
        self.assertIs(type(self.fake_payment.uid), uuid.UUID)

    def test_financial_status_type(self):
        """
        Test that the financial status is a numpy string
        """
        self.assertIs(type(self.fake_payment.financial_status), numpy.str_)

    def test_payment_method_type(self):
        """
        Test that the payment_method is a numpy string
        """
        self.assertIs(type(self.fake_payment.payment_method), numpy.str_)

    def test_configurability(self):
        """
        Test that the payment_method is configurable
        """
        my_financial_status = "random_financial_status"
        my_payment_method = "random_payment_method"
        fake_payment = FakePayment(
            financial_status=my_financial_status, payment_method=my_payment_method
        )
        self.assertEqual(fake_payment.financial_status, my_financial_status)
        self.assertEqual(fake_payment.payment_method, my_payment_method)

    def test_config_types(self):
        """
        testing that the kwarg config for financial status and payment method work
        as intended
        """
        my_financial_status = "random_financial_status"
        my_payment_method = "random_payment_method"
        fake_payment = FakePayment(
            financial_status=my_financial_status, payment_method=my_payment_method
        )
        self.assertIs(type(fake_payment.financial_status), numpy.str_)
        self.assertIs(type(fake_payment.payment_method), numpy.str_)
