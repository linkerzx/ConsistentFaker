"""
Unit Tests for Fake Company Builder
"""
import unittest
from consistent_faker.builders import FakeCompanyBuilder
from consistent_faker.classes import FakeCompany


class TestFakeCompanyBuilder(unittest.TestCase):
    """
    Unit Tests for Fake Company Builder
    """

    def setUp(self):
        self._fake_company_builder_ = FakeCompanyBuilder

    @property
    def fake_company_builder_(self):
        """
        returns a FakeCompanyBuilder callable
        """
        return self._fake_company_builder_

    def test_single_generation_type(self):
        """
        Test that the builder is able to generate 1 company type
        """
        self.assertIs(type(self.fake_company_builder_(n=1).build_weights()), dict)

    def test_single_generation_items_type(self):
        """
        Test that the builder is able to generate only 1 FakeCompany
        """
        companies = self.fake_company_builder_(n=1).build_weights()
        companies_keys = list(companies.keys())
        companies_values = list(companies.values())

        self.assertIs(type(companies_keys[0]), FakeCompany)
        self.assertIs(type(companies_values[0]), float)

    def test_generation_length(self):
        """
        Test that the builder is able to generate only the right amount of records
        """
        for i in range(1, 30, 3):
            self.assertIs(len(self.fake_company_builder_(n=i).build_weights()), i)
