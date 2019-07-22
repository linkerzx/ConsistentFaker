"""
Fake Customer builder
-----------------------------
[TODO PLACEHOLDER]
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
