"""
Util to generate orders for some customers
"""
import numpy as np
from consistent_faker.utils.lists import flatten


def gen_orders_from_customers_df(customer_df, config=None, variants=None):
    """
    Util to generate orders for some customers given a given product catalogue
    and configuration dictionary
    """
    output = []

    from consistent_faker.classes import FakeCustomer
    from consistent_faker.builders.fake_order_builder import FakeOrderBuilder

    max_orders_per_cust = config.get("max_orders_per_cust", 15)
    min_orders_per_cust = config.get("min_orders_per_cust", 0)

    for row in customer_df.iterrows():
        fake_customer = FakeCustomer(**row[1])
        number_of_orders = np.random.randint(
            low=min_orders_per_cust, high=max_orders_per_cust
        )
        fake_order = FakeOrderBuilder(
            fake_customer, number_of_orders, config=config, variants=variants
        ).build()
        output.append(fake_order)
    return [x for x in flatten(output)]
