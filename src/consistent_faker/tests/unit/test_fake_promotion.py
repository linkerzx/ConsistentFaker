"""
Unit tests for Fake Promotion
"""
import unittest
import numpy
from consistent_faker.classes import FakePromotion


class TestFakePromotion(unittest.TestCase):
    """
    Unit tests for Fake Promotion
    """

    def setUp(self):
        self._fake_promotion = FakePromotion()

    @property
    def fake_promotion(self):
        """FakePromotion"""
        return self._fake_promotion

    def test_discount_code_type(self):
        """
        Test that discount_code is a string
        """
        fake_promo = FakePromotion(type="coupon")
        self.assertIs(type(fake_promo.discount_code), str)

    def test_type_type(self):
        """
        Test that value_type is a numpy string
        """
        self.assertIs(type(self.fake_promotion.type), numpy.str_)

    def test_value_type_type(self):
        """
        Test that value_type is a numpy string
        """
        self.assertIs(type(self.fake_promotion.value_type), numpy.str_)

    def test_value_type(self):
        """
        Test that value_type is a numpy float
        """
        self.assertIs(type(self.fake_promotion.value), numpy.float64)

    def test_value_config(self):
        """
        Test that value is configurable
        """
        my_value = 4.3
        fake_promo = FakePromotion(value=my_value)
        self.assertEqual(fake_promo.value, my_value)

    def test_value_type_config(self):
        """
        Test that value type is configurable
        """
        my_value_type = "percentage"
        fake_promo = FakePromotion(value_type=my_value_type)
        self.assertEqual(fake_promo.value_type, my_value_type)

    def test_discount_code_config(self):
        """
        Test that discount_code is a string
        """
        my_type = "coupon"
        fake_promo = FakePromotion(type=my_type)
        self.assertEqual(fake_promo.type, my_type)
