"""
Fake Customer builder

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
from typing import List, Dict, Optional
from consistent_faker.classes import FakeCustomer, FakeCompany
from consistent_faker.builders import FakeBaseBuilderObject


class FakeCustomerBuilder(FakeBaseBuilderObject):
    """
    Generates a list of customer based on the provided parameters

    Parameters
    -----------
    n:          Optional[int],the number of customers that are set to be built
    companies:  Optional[Dict[FakeCompany, float]]
    config:     Optional[Dict]
    """

    def __init__(
            self,
            companies: Dict[FakeCompany, float] = None,
            n: Optional[int] = None,
            **kwargs
    ) -> None:
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)

        if n is None:
            n = self.config.get("number_of_customers", 1)

        self._n = n
        self._companies = companies

    @property
    def companies(self) -> Dict[FakeCompany, float]:
        """
        Returns:
            Dict[FakeCompany, float]: a dictionary of companies to be used for
            the random customer generation and their associated weights
            (to be used for likelyhood generation)
        """
        return self._companies

    @property
    def customers(self) -> List[FakeCustomer]:
        """
        Returns:
            List[FakeCustomer]: the list of FakeCustomer that are built
        """
        return self._build_property

    @customers.setter
    def customers(self, value: List[FakeCustomer] = None) -> None:
        """ Customer setter """
        self._build_property = value

    def build(self) -> List[FakeCustomer]:
        """ build """
        self.customers = [
            FakeCustomer(self.companies, config=self.config) for x in range(0, self.n)
        ]
        return self.customers
