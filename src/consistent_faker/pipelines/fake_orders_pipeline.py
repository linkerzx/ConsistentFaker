"""
Pipelines providing fake orders based on certain conditions
"""
import pandas as pd
from consistent_faker.builders import FakeCompanyBuilder
from consistent_faker.builders import FakeCustomerBuilder
from consistent_faker.builders import FakeProductVariantBuilder
from consistent_faker.utils.orders import gen_orders_from_customers_df


def gen_fake_orders(config):
    """
    Pipelines to generate a set of orders based on a pre-defined composition method
    """
    nbr_companies = config.get("number_of_companies")
    nbr_users = config.get("number_of_customers")
    email_deduplication = config.get("email_deduplication")
    nbr_variants = config.get("number_of_variants")

    # Gen Customers
    companies = FakeCompanyBuilder(nbr_companies).build_weights()
    customers = FakeCustomerBuilder(companies, nbr_users, config=config).build_as_dict()
    if email_deduplication:
        customer_df = pd.DataFrame(customers).drop_duplicates(subset="email_address")
    else:
        customer_df = pd.DataFrame(customers)

    # Gen Variants
    variants = FakeProductVariantBuilder(nbr_variants, config=config).build_weights()

    # Gen Orders
    orders = gen_orders_from_customers_df(customer_df, config=config, variants=variants)

    return orders
