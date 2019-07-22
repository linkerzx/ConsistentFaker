"""
Fake Product Variant class object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import Dict
from faker import Faker
import numpy as np
from consistent_faker.classes import FakeSku, FakeBaseObject


FAKE = Faker()


class FakeProductVariant(FakeBaseObject):
    """
    Generate a random product variant

    Parameters
    -----------
    uid:                Optional[uuid.UUID]
    config:             Optional[Dict], configuration dictionary
    sku:                Optional[FakeSku], sku to be associated to the product variant
    price_incl_taxes:   Optional[float], product's price including taxes

    Examples
    -----------
    Generate a random product variant
    >>>FakeProductVariant()
    FakeProductVariant(sku=FakeSku(ean=6326820664326, title=arm),
        uid=038260ce-2a92-48bc-acd4-f30790258849, price_incl_taxes=62.12)

    Generate a product variant associated with a SKU
    >>>this_sku = FakeSku();this_sku
    FakeSku(ean=8445137149116, title=picture)
    >>>FakeProductVariant(sku=this_sku)
    FakeProductVariant(sku=FakeSku(ean=8445137149116, title=picture),
        uid=17201fdb-900b-4ca8-8be6-b761ba6f39c3, price_incl_taxes=25.66)
    """

    def __init__(self, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self._config = kwargs.get("config", {})
        self._sku = self._init_sku(sku=kwargs.get("sku"))

        self._price_incl_taxes = self._init_price_incl_taxes(
            price_incl_taxes=kwargs.get("price_incl_taxes")
        )

    def __repr__(self):
        repr_str = (
            f"FakeProductVariant(sku={self.sku}, uid={self.uid},"
            + f" price_incl_taxes={self.price_incl_taxes})"
        )
        return repr_str

    @property
    def sku(self) -> FakeSku:
        """FakeSku: sku associated to the product variant"""
        return self._sku

    @property
    def price_incl_taxes(self) -> np.float64:
        """np.float64: price including of taxes for the product variant"""
        return self._price_incl_taxes * np.float64(1)

    def to_dict(self) -> Dict:
        """
        Serialize the fake product variant object to a dictionary
        """
        product_variant_dict = {
            "uid": str(self.uid),
            "sku": self.sku.to_dict(),
            "price_incl_taxes": self.price_incl_taxes,
        }
        return product_variant_dict

    def _init_sku(self, sku: FakeSku = None) -> FakeSku:
        """
        Assign or generate a sku to be associated with the product variant
        Returns:
            FakeSku
        """
        if sku and isinstance(sku, FakeSku):
            return sku
        if sku:
            raise TypeError("Sku kwarg should be an instance of FakeSku")
        return FakeSku(config=self._config)

    def _init_price_incl_taxes(self, price_incl_taxes: float = None) -> float:
        if price_incl_taxes and isinstance(price_incl_taxes, float):
            return price_incl_taxes
        if price_incl_taxes:
            raise TypeError("price_incl_taxes should be an instance of float")
        default_cfg = (
            self._config.get("product_variant", {}) if self._config else {}
        )
        default_cfg_price_incl_taxes = default_cfg.get("price_incl_taxes", {})
        price_incl_taxes_min = default_cfg_price_incl_taxes.get("min_int", 0)
        price_incl_taxes_max = default_cfg_price_incl_taxes.get("max_int", 200)

        rand_price_incl_tax = np.random.randint(
            low=price_incl_taxes_min, high=price_incl_taxes_max
        ) + round(np.random.ranf(), 2) * np.float64(1)
        return rand_price_incl_tax
