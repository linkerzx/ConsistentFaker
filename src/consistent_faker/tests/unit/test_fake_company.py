"""
Unit Tests for Fake Company
"""
import unittest
import uuid
from consistent_faker.classes import FakeCompany


class TestFakeCompany(unittest.TestCase):
    """
    Unit Tests for Fake Company
    """

    def setUp(self):
        self._fake_company = FakeCompany()

    @property
    def fake_company(self):
        """FakeCompany"""
        return self._fake_company

    def test_company_name_type(self):
        """
        Test that company_name is a string
        """
        self.assertIs(type(self.fake_company.company_name), str)

    def test_uid_type(self):
        """
        Test that the uid is a guid
        """
        self.assertIs(type(self.fake_company.uid), uuid.UUID)

    def test_get_company_domain_type(self):
        """
        Test that get_company_domain() returns a str
        """
        self.assertIs(type(self.fake_company.get_company_domain()), str)

    def test_to_dict_type(self):
        """
        Test that to_dict() returns a dict
        """
        self.assertIs(type(self.fake_company.to_dict()), dict)

    def test_configuration_company_name(self):
        """
        Test that the fake company can be configured with a specific company name
        """
        my_company_name = "test company"
        fake_company = FakeCompany(company_name=my_company_name)
        self.assertEqual(fake_company.company_name, my_company_name)

    def test_configuration_top_level_domain(self):
        """
        Test that the fake company can be configured with a specific company domain
        """
        my_top_level_domain = ".co.uk"
        fake_company = FakeCompany(top_level_domain=my_top_level_domain)
        self.assertEqual(fake_company.top_level_domain, my_top_level_domain)
