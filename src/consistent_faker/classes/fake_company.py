"""
Fake Company class object

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
import re
from typing import Dict
from faker import Faker
from tld import is_tld
from consistent_faker.utils import get_top_level_domain
from consistent_faker.classes import FakeBaseObject


FAKE = Faker()


class FakeCompany(FakeBaseObject):
    """
    Create a Fake Company object which can be used in order to generate
    email addresses. The method generates a company id, name and domain

    Parameters
    -----------
    uid:            Optional[uuid.UUID]
    company_name:   Optional[str]:  name of the company
    company_domain: Optional[str]: top level domain name (eg .co.uk)

    Examples:
    -----------
    Generate a random fake company
    >>>FakeCompany()
    FakeCompany('Frank, Brown and Brown')
    """

    def __init__(self, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self._company_name = self._init_company_name(
            company_name=kwargs.get("company_name")
        )
        self._top_level_domain = self._init_top_level_domain(
            top_level_domain=kwargs.get("top_level_domain")
        )

    def __repr__(self):
        return "FakeCompany('%s')" % self.company_name

    @property
    def company_name(self) -> str:
        """str: Fake company name"""
        return self._company_name

    @property
    def top_level_domain(self):
        """
        str: Top level domain name
        example: .co.uk, .com, .org
        """
        return self._top_level_domain

    def get_company_domain(self) -> str:
        """
        Generate a domain name from the company name
        Returns:
            str: a domain name

        """
        lower_comp_name = self.company_name.lower()
        domain_prefix = re.sub("[^0-9a-zA-Z]+", "", lower_comp_name)
        return domain_prefix + self.top_level_domain

    def to_dict(self) -> Dict:
        """
        Serialize the fake order object to a dictionary
        """
        company_dict = {"uid": str(self.uid), "company_name": self.company_name}
        return company_dict

    @classmethod
    def to_dataframe(cls):
        """Not implemented"""
        return NotImplemented

    @classmethod
    def _init_top_level_domain(cls, top_level_domain: str = None) -> str:
        """
        Assign or generate a top level domain
        Returns:
            str: assign or generate a random top level domain
            eg: .com, .co.uk
        """
        if top_level_domain and isinstance(top_level_domain, str):
            if is_tld(top_level_domain[1:]):
                return top_level_domain
            raise ValueError(
                "%s is not a valid top level domain" % top_level_domain
            )
        if top_level_domain:
            return TypeError("top_level_domain kwarg should be an instance of str")
        return get_top_level_domain()

    @classmethod
    def _init_company_name(cls, company_name: str = None) -> str:
        """
        Assign or generate a company name
        Returns:
            str: company name
        """
        if company_name and isinstance(company_name, str):
            return company_name
        if company_name:
            return TypeError("company_name kwarg should be an instance of str")
        return FAKE.format('company')
