"""
Fake Base Builder Object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import Optional, List, Dict
import numpy as np

class FakeBaseBuilderObject:
    """
    TODO
    """

    def __init__(self, n: Optional[int] = None, **kwargs):
        self._config = kwargs.get("config", {})
        self._n = n
        self._build_property = None
        self._weights = None


    @property
    def n(self) -> int:
        """
        Returns:
            int: the number of variants that are set to be built
        """
        return self._n

    @property
    def weights(self) -> List[float]:
        """
        Returns:
            List[np.float64]: list of randomly assigned weight that are built
        """
        return self._weights

    @property
    def build_property(self) -> object:
        """ Core build property"""
        return self._build_property

    @property
    def config(self) -> Dict:
        """
        Returns:
            dict: the configuration dict associated with the builder
        """
        return self._config

    @weights.setter
    def weights(self, value) -> None:
        """ Setter for weights"""
        self._weights = value

    @build_property.setter
    def build_property(self, value) -> None:
        """ Setter for core build property"""
        self._build_property = value

    def build_as_dict(self) -> List:
        """ Build as dict"""
        self.build()
        return [x.to_dict() for x in self.build_property]

    def build_weights(self) -> Dict[object, float]:
        """ build as a dict of product variants / weights """
        self.build()

        self._weights = [np.random.rand() for x in range(0, self.n)]
        return dict(zip(self.build_property, self.weights))

    @classmethod
    def build(cls):
        """ Not Implemented """
        return NotImplemented
