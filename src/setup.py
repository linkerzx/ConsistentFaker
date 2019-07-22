#!/usr/bin/env python

from setuptools import setup, find_namespace_packages


setup(
    name="consistent_faker",
    version="0.1",
    description="consistent_faker, Fake your data consistantly",
    author="Julien Kervizic",
    author_email="julien.kervizic@gmail.com",
    url="placeholder.com",
    packages=find_namespace_packages(),
    include_package_data=True,
    install_requires=[
        "pandas>=0.24.1",
        "numpy>=1.15.4",
        "Faker>=1.0.5",
        "pycountry>=18.12.8",
        "tld>=0.9.3",
        "email-validator>=1.0.4",
    ],
)
