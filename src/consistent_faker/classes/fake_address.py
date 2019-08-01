"""
Fake Address class object

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
from typing import Dict, Optional
from faker import Faker
import numpy as np
import pycountry
from consistent_faker.classes import FakeBasicCustomer, FakeBaseObject
from consistent_faker.utils import random_choice_weight_dict
from consistent_faker.weights.addresses import ADDRESS_TYPE_WEIGHTS

FAKE = Faker()


class FakeAddress(FakeBaseObject):
    """
    Generates a semi random fake address

    Parameters
    -----------
    config:         Optional[Dict], configuration dictionary
    uid:            Optional[uuid.UUID], the assigned address id
    customer:       Optional[FakeBasicCustomer]
    address_type:   Optional[str], example: home, company
    first_name:     Optional[str], first name to be used for the address (Attn)
    last_name:      Optional[str], last name to be used for the address (Attn)
    address1:       Optional[str], first address line
    address2:       Optional[str], second address line
    city:           Optional[str], address's city
    zip:            Optional[str], address's postal code
    province:       Optional[str]
    country_code:   Optional[str], address' country

    Examples
    -----------
    Generate a random address
    >>>FakeAddress()
    FakeAddress(first_name=Eric, last_name=Serrano, address1=426 Garcia Falls Apt. 718,
        address2=Apt. 307, zip=55692, city=Lake Jesseshire, country_code=None)


    TODO:
        incorporate province
        kwargs fi

    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, customer: Optional[FakeBasicCustomer] = None, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config")

        self._customer = self._init_customer(customer)
        """
        Internal Address variables
        """
        self._address_type = kwargs.get("address_type", self._init_address_type())
        """
        Necessary fields for address
        """
        self._first_name = self._init_first_name(first_name=kwargs.get("first_name"))
        self._last_name = self._init_last_name(last_name=kwargs.get("last_name"))
        self._company = self._init_company()
        address_1, address_2 = self._init_addresses()
        self._address1 = kwargs.get("address1", address_1)
        self._address2 = kwargs.get("address2", address_2)
        self._city = self._init_city(city=kwargs.get("city"))
        self._province = self._init_province(kwargs.get("province"))
        self._zip = self._init_postal_code(zip_code=kwargs.get("zip"))
        fake_country_code = FAKE.format('country_code', representation="alpha-2")
        self._country_code = kwargs.get(
            "country_code", fake_country_code
        )  # make country code - weight based
        self._country = pycountry.countries.get(alpha_2=self._country_code).name

    def __repr__(self):
        repr_out = f"FakeAddress(first_name={self.first_name}, last_name={self.last_name},"
        repr_out += " address1={self.address1}, address2={self.address2}, zip={self.zip},"
        repr_out += " city={self.city}, country_code={self.country_code})"
        return repr_out

    @property
    def address_type(self) -> np.str_:
        """
        np.str_: address type
        examples: home, company
        """
        return self._address_type

    @property
    def first_name(self) -> str:
        """str: attn first name for the address"""
        return self._first_name

    @property
    def last_name(self) -> str:
        """str: attn last name for the address"""
        return self._last_name

    @property
    def address1(self) -> str:
        """str: first address line, usually consisting of street name"""
        return self._address1

    @property
    def address2(self) -> str:
        """str: second address line"""
        return self._address2

    @property
    def city(self) -> str:
        """str: city of the address"""
        return self._city

    @property
    def province(self) -> str:
        """str: province of the address"""
        return self._province

    @property
    def zip(self) -> str:
        """str: postal code of the address"""
        return self._zip

    @property
    def country_code(self) -> str:
        """
        str: not yet implemented
        """
        return self._country_code

    @property
    def country(self) -> str:
        """
        str: not yet implemented
        """
        return self._country

    @property
    def customer(self):
        """FakeCustomer: The customer associated to this address"""
        return self._customer

    def to_dict(self) -> Dict:
        """
        Serialize the fake address object to a dictionary
        """
        address_dict = {
            "address_type": self.address_type,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "province": self.province,
            "zip": self.zip,
            "country_code": self.country_code,
            "country": self.country,
        }
        return address_dict

    def _init_first_name(self, first_name: str = None):
        if first_name and isinstance(first_name, str):
            return first_name
        if first_name:
            raise TypeError("first_name kwarg should be an instance of str")
        if self.address_type in {"home", "company"}:
            return self.customer.first_name
        new_customer = FakeBasicCustomer(config=self.config)
        return new_customer.first_name

    def _init_last_name(self, last_name: str = None):
        if last_name and isinstance(last_name, str):
            return last_name
        if last_name:
            raise TypeError("last_name kwarg should be an instance of str")
        if self.address_type in {"home", "company"}:
            return self.customer.last_name
        new_customer = FakeBasicCustomer(config=self.config)
        return new_customer.last_name

    def _init_address_type(self) -> np.str_:
        config = self.config
        cfg_address_type_weights = None
        if config:
            address_config = config.get("address", {})
            cfg_address_type_weights = address_config.get("address_type_weights")
        if cfg_address_type_weights:
            weights = cfg_address_type_weights
        else:
            weights = ADDRESS_TYPE_WEIGHTS
        return random_choice_weight_dict(weights)

    def _init_company(self):
        if self.address_type in {"company"}:
            return self.customer.company
        return None

    @classmethod
    def _init_province(cls, province):
        if province:
            return province
        # TODO generate random province
        return None

    @classmethod
    def _init_postal_code(cls, zip_code: str = None) -> str:
        if zip_code and isinstance(zip_code, str):
            return zip_code
        if zip_code:
            raise TypeError("zip_code should be an instance of str")
        return FAKE.format('postalcode')

    @classmethod
    def _init_addresses(cls):
        # TODO check if it is a company address ->if it is
        address_1 = FAKE.format('street_address')
        address_2 = FAKE.format('secondary_address')
        return address_1, address_2

    def _init_customer(self, customer: FakeBasicCustomer = None) -> FakeBasicCustomer:
        if customer and not isinstance(customer, FakeBasicCustomer):
            raise TypeError("Customer needs to be an instance of FakeBasicCustomer")
        if customer:
            return customer
        return FakeBasicCustomer(config=self.config)

    @classmethod
    def _init_city(cls, city: str = None) -> str:
        if city and isinstance(city, str):
            return city
        if city:
            raise TypeError("city kwarg should be an instance of str")
        return FAKE.format('city')
