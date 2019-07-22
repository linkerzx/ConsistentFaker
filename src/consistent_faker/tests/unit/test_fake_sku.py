"""
Unit tests for Fake SKu
"""
import unittest
from consistent_faker.classes import FakeSku
from consistent_faker.utils import is_json


class TestFakeSku(unittest.TestCase):
    """
    Unit tests for Fake SKu
    """

    def setUp(self):
        self._fake_sku = FakeSku()

    @property
    def fake_sku(self):
        """FakeSku"""
        return self._fake_sku

    def test_ean_type(self):
        """
        Test that the ean is a string
        """
        self.assertIs(type(self.fake_sku.ean), str)

    def test_title_type(self):
        """
        Test that the title is a string
        """
        self.assertIs(type(self.fake_sku.title), str)

    def test_description_type(self):
        """
        Test that the description is a string
        """
        self.assertIs(type(self.fake_sku.description), str)

    def test_to_dict_type(self):
        """
        Test that to_dict() returns a dict
        """
        self.assertIs(type(self.fake_sku.to_dict()), dict)

    def test_to_json_type(self):
        """
        Test that to_json returns a valid json
        """
        my_json = self.fake_sku.to_json()
        self.assertIs(type(my_json), str)
        self.assertIs(is_json(my_json), True)
