"""
Fake Customer class object

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
import json
from typing import Dict, Optional
from faker import Faker
from consistent_faker.classes import FakeCompany, FakeBasicCustomer
from consistent_faker.classes.fake_address import FakeAddress

FAKE = Faker()


class FakeCustomer(FakeBasicCustomer):
    """
    Generates consistent fake orders, where for instance, the shipping
    and email address is generated based on personal user attributes.

    Parameters
    -----------
    companies:      Optional[Dict[FakeCompany, float]], dictionary of companies
        of their likelyhood to be granted
    config:         Optional[Dict], configuration dictionary
    uid:            Optional[uuid.UUID], the assigned customer id
    gender:         Optional[str], the gender of the customer M/F
    first_name:     Optional[str], the first name of the Customer
    last_name:      Optional[str], The last name of the customer
    date_of_birth:  Optional[datetime.date], the customers' date of birth
    company:        Optional[FakeCompany], the company associated with the customeer
    email_address:  Optional[str], the email address assigned to thee customer
    home_phone:     Optional[str]. the customer's home phone number
    mobile_phone:   Optional[str], the customer's mobile phone number
    default_address:Optional[FakeAddress], the deafault address assigned
        to the customer

    Examples
    -----------
    Create a random fake customer
    >>> FakeCustomer()
    FakeCustomer(uid=73e52e5d-7431-4368-9aae-5461d55e1ecf,
        gender=M, first_name=Louis, last_name=Obrien)

    Create a male fake customer
    >>>> FakeCustomer(gender="M")
    FakeCustomer(uid=3869b9a0-22b0-4d38-9b68-8303e097c0d7,
        gender=M, first_name=Michael, last_name=Greene)

    Create a male customer named John
    >>> FakeCustomer(gender="M", first_name="John")
    FakeCustomer(uid=e970e40b-fb92-439a-b5ef-0978ec1c4d44,
        gender=M, first_name=John, last_name=Jones)
    """

    def __init__(self, companies: Optional[Dict[FakeCompany, float]] = None, **kwargs):
        """
        Initiate the class :)
        """
        FakeBasicCustomer.__init__(self, companies, **kwargs)
        self._default_address = self._init_default_address(
            default_address=kwargs.get("default_address")
        )
        self._companies = companies

    @property
    def default_address(self) -> FakeAddress:
        """FakeAddress: The default address associated with the Customer"""
        return self._default_address


    @property
    def companies(self):
        """Optional[Dict[FakeCompany, float]] - companies dictionary of weights"""
        return self._companies

    def to_dict(self) -> Dict:
        """
        Serialize the fake customer object to a dictionary
        """
        customer_dict = {
            "uid": str(self.uid),
            "gender": self.gender,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
            "email_address": self.email_address,
            "home_phone": self.home_phone,
            "mobile_phone": self.mobile_phone,
            "company": self.company.to_dict(),
            "default_address": self.default_address.to_dict(),
        }
        return customer_dict

    def to_json(self):
        """
        Serialize the fake customer object to a json
        """
        return json.dumps(self.to_dict())

    def _init_default_address(self, default_address: str = None) -> FakeAddress:
        """
        Assign or generate a default address for the customeer
        """
        if default_address and isinstance(default_address, FakeAddress):
            return default_address
        if default_address:
            raise TypeError("default_address should be an instance of FakeAddress")
        return FakeAddress(self, config=self.config)
