# consistent_faker
consistent_faker is a library that allows to generate consistent objects
and allows them to compose them easily.

## Use case
There are a few use cases for consistent_faker

From generating some data to blank start a data product

or generating the data necessary to test data pipelines

To generating some datasets for a ML hackathon

## Dependencies
* python3
* pandas
* numpy 
* faker
* pycountry
* tld
* email-validator

## Install 
```pip3 install .```

## Running tests
```python3 run_tests.py```

## How to use consistent_faker
### Using the class, create a fake order
Create a FakeOrder directly: 
```
from consistent_faker import FakeOrder
FakeOrder()
````
### Using the builder, create fake orders
Create 20 FakeOrders using the builder: 
```
from consistent_faker import FakeOrderBuilder
FakeOrderBuilder(n=20).build()
```

### Using the builder, Setting a fake order with composition
Create an order with an associated customer
```
from consistent_faker import FakeOrder, FakeCustomer
this_customer = FakeCustomer()
FakeOrder(customer=this_customer)
```
