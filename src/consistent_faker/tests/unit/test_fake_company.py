"""
Unit Tests for Fake Company

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
