"""
Fake Order Item class object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import List, Dict
import numpy as np
from consistent_faker.classes import FakeProductVariant
from consistent_faker.utils import random_choice_non_normalized_weight_dict
from consistent_faker.classes import FakeBaseObject

class FakeOrderItem(FakeBaseObject):
    """
    Generates a semi random order item

    Parameters
    -----------
    uid:            Optional[uuid.UUID]
    config:         Optional[Dict], configuration dictionary
    variants:       Optional[Dict[FakeProductVariant, float]],
        product variants and weights to use for selection
    product_variant:Optional[FakeProductVariant], the product variant
    quantity:       Optional[int], the quantity of product in the line item

    Examples
    -----------
    Random order item generation
    >>>FakeOrderItem()
    FakeOrderItem(
        uid=71c0d99d-6bcc-434c-94cb-09ba6891aabc,
        product_variant=FakeProductVariant(sku=FakeSku(ean=0402131830639, title=me),
        uid=b285e7d8-01a3-497f-bf26-52d162f56e22, price_incl_taxes=146.74),
        quantity=5, line_item_price=733.7
    )
    """

    def __init__(self, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config", {})
        self.order_item_cfg = self.config.get("order_item", {}) if self.config else {}
        # define the order item quantity
        self._quantity = self._init_order_item_qty(quantity=kwargs.get("quantity"))
        # define the variant to use
        self._variants = self._init_variants(variants=kwargs.get("variants"))
        self._product_variant = self._init_product_variant(
            product_variant=kwargs.get("product_variant")
        )

    def __repr__(self):
        repr_str = (
            f"FakeOrderItem(uid={self.uid}, "
            + f"product_variant={self.product_variant},"
            + f" quantity={self.product_quantity},"
            + f" line_item_price={self.product_prices_incl_taxes})"
        )
        return repr_str

    @property
    def product_prices_incl_taxes(self) -> np.float64:
        """
        float: The total price of all products in the order line
        including taxes
        """
        return self.product_variant.price_incl_taxes * self.product_quantity

    @property
    def product_quantity(self) -> int:
        """
        int: The unit quantity in the order item
        """
        return self._quantity

    @property
    def product_variant(self) -> FakeProductVariant:
        """
        FakeProductVariant: The specific product variant associated with
        the order item
        """
        return self._product_variant

    @property
    def variants(self) -> List[FakeProductVariant]:
        """
        List[FakeProductVariants]: all the product variants that were used
        to populate the FakeOrderItem
        """
        return self._variants

    def to_dict(self) -> Dict:
        """
        Serialize the fake order item object to a dictionary
        """
        order_item_dict = {
            "uid": str(self.uid),
            "product_prices_incl_taxes": self.product_prices_incl_taxes,
            "product_quantity": self.product_quantity,
            "product_variant": self.product_variant.to_dict(),
        }
        return order_item_dict

    def _init_product_variant(
            self,
            product_variant: FakeProductVariant = None
        ) -> FakeProductVariant:
        """
        Assign or generate a product variant
        Returns:
            FakeProductVariant: a product variant
        """
        # pylint: disable=pointless-string-statement
        if product_variant and isinstance(product_variant, FakeProductVariant):
            """
            if product variant is fed as a kwarg and is of the right type
            Assign it to the order item object
            """
            return product_variant
        if product_variant:
            raise TypeError(
                "product_variant kwarg should be an instance of FakeProductVariant"
            )
        if self.variants:
            """
            if variants is setup randomly choose a variant from the dictionary
            based on their weight
            """
            variant = random_choice_non_normalized_weight_dict(self.variants)
        else:
            # Otherwise assign a new Fake product variant
            variant = FakeProductVariant(config=self.config)
        return variant

    def _init_order_item_qty(self, quantity: int = None) -> int:
        """
        Assign or generate an order item quantity
        Returns:
            int: order item quantity
        """
        if quantity and isinstance(quantity, int):
            return quantity
        if quantity:
            raise TypeError("quantity kwarg should be an instance of int")
        # calculate the order item quantity
        order_item_cfg = self.order_item_cfg
        min_qty = order_item_cfg.get("quantity", {}).get("min", 1)
        max_qty = order_item_cfg.get("quantity", {}).get("max", 3)

        default_quantity = np.random.randint(low=min_qty, high=max_qty)
        return default_quantity

    @classmethod
    def _init_variants(
            cls,
            variants: Dict[FakeProductVariant, float] = None
        ) -> Dict[FakeProductVariant, float]:
        """
        Type checks that variants is of the right type
        Returns:
            Dict[FakeProductVariant, float]: dictionary of product variants and weights
        """
        if (
                variants
                and isinstance(variants, dict)
                and isinstance(list(variants.keys())[0], FakeProductVariant)
                and isinstance(list(variants.values())[0], float)
        ):
            return variants
        if variants:
            raise TypeError(
                "variants kwarg should be an instance of Dict[FakeProductVariant, float]"
            )
        return None
