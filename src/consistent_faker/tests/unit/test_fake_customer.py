"""
Unit Tests for Fake customer

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
import datetime
from consistent_faker.classes import FakeCustomer
from consistent_faker.classes import FakeAddress
from consistent_faker.classes import FakeCompany


class TestFakeCustomerBasicTypes(unittest.TestCase):
    """
    Type checking Unit Tests for Fake Company
    """

    def setUp(self):
        self._fake_customer = FakeCustomer()

    @property
    def fake_customer(self):
        """FakeCustomer"""
        return self._fake_customer

    def test_uid_type(self):
        """
        Test that the customer id is a guid
        """
        self.assertIs(type(self.fake_customer.uid), uuid.UUID)

    def test_first_name_type(self):
        """
        Test that the first name is a string
        """
        self.assertIs(type(self.fake_customer.first_name), str)

    def test_last_name_type(self):
        """
        Test that the last name is a string
        """
        self.assertIs(type(self.fake_customer.last_name), str)

    def test_date_of_birth_type(self):
        """
        Check that the date of birth is a date
        """
        self.assertIs(type(self.fake_customer.date_of_birth), datetime.date)

    def test_company_type(self):
        """
        Check that the company type is a fake company
        """
        self.assertIs(type(self.fake_customer.company), FakeCompany)

    def test_email_type(self):
        """
        Check that the email is a string
        """
        self.assertIs(type(self.fake_customer.email_address), str)

    def test_hpme_phone_type(self):
        """
        Check thet the home phone is a string
        """
        self.assertIs(type(self.fake_customer.home_phone), str)

    def test_mobile_phone_type(self):
        """
        Check that the mobile phone is a string
        """
        self.assertIs(type(self.fake_customer.mobile_phone), str)

    def test_default_address_type(self):
        """
        Test that the customer's default address is a fake address
        """
        self.assertIs(type(self.fake_customer.default_address), FakeAddress)


class TestFakeCustomerComposition(unittest.TestCase):
    """
    Composition Unit Tests for Fake Company
    """

    def setUp(self):
        self._fake_customer = FakeCustomer

    @property
    def fake_customer_(self):
        """FakeCustomer: """
        return self._fake_customer

    def test_customer_company_composition(self):
        """
        Test that the composition works between customer and company
        """
        company = FakeCompany()
        cust = self.fake_customer_(companies={company: 1.0})
        self.assertEqual(company, cust.company)

    def test_customer_companies_composition_type_error(self):
        """
        Check that feeding a different type than
        Dict[FakeCompany, np.float64] as companies kwarg result in an error
        """
        my_companies = "Companies should not be a string"
        try:
            cust = self.fake_customer_(companies=my_companies)
            raise Exception(cust.companies)
        except TypeError:
            pass #We intend to raise a type error here and therefore pass
        except Exception as exception:
            raise ValueError(exception) #Any Other exception should be flagged

    def test_customer_company_composition_type_error(self):
        """
        Check that feeding a different type than FakeCompany
        as company kwarg result in an error
        """
        my_company = "Companies should not be a string"
        try:
            cust = self.fake_customer_(company=my_company)
            raise Exception(cust.company)
        except TypeError:
            pass #We intend to raise a type error here and therefore pass
        except Exception as exception:
            raise ValueError(exception) #Any Other exception should be flagged
