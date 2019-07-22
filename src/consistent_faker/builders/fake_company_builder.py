"""
Fake Company builder
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import List, Optional
from consistent_faker.classes import FakeCompany
from consistent_faker.builders import FakeBaseBuilderObject

class FakeCompanyBuilder(FakeBaseBuilderObject):
    """
    TODO
    """

    def __init__(self, n: Optional[int] = None, **kwargs):
        FakeBaseBuilderObject.__init__(self, n=n, **kwargs)

        if n is None:
            n = self.config.get("number_of_companies", 1)

        self._n = n
        self._build_property = None

    @property
    def companies(self) -> List[FakeCompany]:
        """
        Returns:
            List[FakeOrderItem]: the list of FakeOrderItem that are built
        """
        return self._build_property

    @companies.setter
    def companies(self, value: List[FakeCompany] = None) -> None:
        """ companies setter"""
        self._build_property = value

    def build(self) -> List[FakeCompany]:
        """build """
        self.build_property = [FakeCompany() for x in range(0, self.n)]
        return self.build_property
