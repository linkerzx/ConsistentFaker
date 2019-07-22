"""
Fake Email class object
-----------------------------
[TODO PLACEHOLDER]
"""
from typing import Dict
import numpy as np
from email_validator import validate_email
from faker import Faker
from faker.utils.decorators import lowercase
from consistent_faker.utils import random_choice_weight_dict, get_top_level_domain
from consistent_faker.formats.emails import WORK_FORMATS, PUBLIC_FORMATS, CUSTOM_FORMATS
from consistent_faker.weights.emails import (
    DEFAULT_INTEGERS_IN_EMAILS_WEIGHTS,
    DEFAULT_PUBLIC_DOMAIN_WEIGHTS,
    DEFAULT_EMAIL_PROVIDER_TYPE_WEIGHTS,
)
from consistent_faker.classes import FakeBaseObject

FAKE = Faker()


class FakeEmail(FakeBaseObject):
    """
    Generates a fake email address that is consistent with the parameters provided

    Parameters
    -----------
    uid:            Optional[uuid.UUID], the assigned email id
    config:         Optional[Dict], configuration dictionary
    first_name:     Optional[str], the first name of the Customer
    last_name:      Optional[str], the last name name of the Customer
    company_domain: Optional[str]
    email_address:  Optional[str], the customer's email address

    Examples
    -----------
    >>>FakeEmail(first_name="Julien", last_name="Kervizic")
    FakeEmail(email_address=jkervizic24@hotmail.com, email_type=public)

    TODO add more kwargs selector
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, first_name: str = None, last_name: str = None, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config", {})
        self.email_config = self.config.get("email", {}) if self.config else {}
        self.kwargs = kwargs
        self._first_name = self._init_first_name(first_name=first_name)
        self._last_name = self._init_last_name(last_name=last_name)
        self._email_type = self._init_email_provider_type()
        self._format = self._init_format()
        self._match_dict = self._init_match_dict()
        self._email_address = self._init_email(
            email_address=kwargs.get("email_address")
        )

    def __repr__(self):
        return f"FakeEmail(email_address={self.email}, email_type={self.email_type})"

    def __str__(self) -> str:
        return self.email

    @property
    def first_name(self) -> str:
        """
        str: Customer's first name
        """
        return self._first_name

    @property
    def last_name(self) -> str:
        """
        str: Customer's last name
        """
        return self._last_name

    @property
    def format(self) -> np.str_:
        """
        np.str: The email format string used for this email
        """
        return self._format

    @property
    def email_type(self) -> str:
        """
        str: email type information
        eg: public, work, custom
        """
        return self._email_type

    @property
    def match_dict(self) -> Dict:
        """
        dict: dictionary with the different attributes
        that needs to be string matched
        """
        return self._match_dict

    @property
    def email(self) -> str:
        """
        str: The Customer's email information
        """
        return self._email_address

    @classmethod
    def _init_pseudonym(cls) -> str:
        """
        TODO Placeholder for a Better Pseudnomiser
        Right now just a random length
        Random chain of characters
        """
        digits = FAKE.format('random_digit_not_null')
        pseudonym = "".join(FAKE.format('random_letters', length=digits))
        return pseudonym

    def _init_rand_int(self) -> int:
        """
        Assign a semi random integer

        Returns:
            int: Integer based on either the date of birth
            Or a random number, this number is to be used to
            fill the different email formats
        """
        date_of_birth = self.kwargs.get("date_of_birth")
        random_int = np.random.randint(low=0, high=100)
        if date_of_birth:

            random_int_val = {
                "year_of_birth": int(str(date_of_birth.year)[2:]),
                "random_int": random_int,
            }

            weights = self.email_config.get(
                "email_random_int_weights", DEFAULT_INTEGERS_IN_EMAILS_WEIGHTS
            )

            random_choice = random_choice_weight_dict(weights)
            return random_int_val.get(random_choice)
        return random_int

    def _init_email_provider_type(self) -> str:
        """
        randomly select a provider type
        out of work, public and custom
        """
        weights = self.email_config.get(
            "email_provider_type_weights", DEFAULT_EMAIL_PROVIDER_TYPE_WEIGHTS
        )
        return random_choice_weight_dict(weights)

    def _init_format(self) -> str:
        format_types = {"work": WORK_FORMATS, "public": PUBLIC_FORMATS}

        formats = format_types.get(self.email_type, CUSTOM_FORMATS)
        return np.random.choice(list(formats))

    def _init_domain(self) -> str:
        """
        returns a relevant domain name
        for the email address based on email type
        """
        if self.email_type == "public":
            return self._init_public_domain()
        if self.email_type == "work":
            return self._init_work_domain()
        return self._init_custom_domain()

    def _init_public_domain(self) -> str:
        weights = self.email_config.get(
            "email_public_domain_weights", DEFAULT_PUBLIC_DOMAIN_WEIGHTS
        )
        return random_choice_weight_dict(weights)

    def _init_work_domain(self) -> str:
        return self.kwargs.get("company_domain", "workplaceholder.com")

    @classmethod
    def _init_custom_domain(cls) -> str:
        # TODO Placeholder not counting family domain
        digits = FAKE.format('random_digit_not_null')
        main_domain = "".join(FAKE.format('random_letters', length=digits))
        tld = get_top_level_domain()
        return main_domain + tld

    def _init_match_dict(self) -> Dict:
        output_dict = {
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "FirstNameCapital": self.first_name[0],
            "LastNameCapital": self.last_name[0],
            "randomint": self._init_rand_int(),
            "domain": self._init_domain(),
            "pseudonym": self._init_pseudonym(),
        }
        return output_dict

    @lowercase
    def _init_email(self, email_address: str = None) -> str:
        """
        Assign or generate an email address
        Returns:
            str: email address
        """
        if email_address and isinstance(email_address, str):
            if validate_email(email_address):
                return email_address
            raise ValueError("email_address is not a valid email address")
        if email_address:
            raise TypeError("email_address kwarg should be an instance of str")
        return self.format.format(**self.match_dict)

    @classmethod
    @lowercase
    def _init_first_name(cls, first_name: str = None) -> str:
        """
        Assign or generate a first name
        Returns:
            str: first name
        """
        if first_name and isinstance(first_name, str):
            return first_name
        if first_name:
            raise TypeError("first_name kwarg should be an instance of str")
        return FAKE.format('first_name')

    @classmethod
    @lowercase
    def _init_last_name(cls, last_name: str = None) -> str:
        """
        Assign or generate a last name
        Returns:
            str: last name
        """
        if last_name and isinstance(last_name, str):
            return last_name
        if last_name:
            raise TypeError("last_name kwarg should be an instance of str")
        return FAKE.format('last_name')
