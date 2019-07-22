"""
Fake Basic Customer class object
-----------------------------
[TODO PLACEHOLDER]
"""
import datetime
from typing import Dict, Optional
from faker import Faker
from consistent_faker.classes import FakeEmail, FakeCompany, FakeBaseObject
from consistent_faker.utils import random_choice_non_normalized_weight_dict

FAKE = Faker()


class FakeBasicCustomer(FakeBaseObject):
    """
    Parameters
    -----------
    companies:      Optional[Dict[FakeCompany, float]], dictionary of companies
        of their likelyhood to be granted
    config:         Optional[Dict], configuration dictionary
    uid:            Optional[uuid.UUID], the assigned customer id
    gender:         Optional[str], the gender of the customer M/F
    first_name:     Optional[str], the first name of the Customer
    last_name:      Optional[str], The last name of the customer
    date_of_birth:  Optional[datetime.date], the customers' date of birth
    company:        Optional[FakeCompany], the company associated with the customeer
    email_address:  Optional[str], the email address assigned to thee customer
    home_phone:     Optional[str]. the customer's home phone number
    mobile_phone:   Optional[str], the customer's mobile phone number
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, companies: Optional[Dict[FakeCompany, float]] = None, **kwargs):
        FakeBaseObject.__init__(self, uid=kwargs.get("uid"))
        self.config = kwargs.get("config")
        self._gender = self._init_gender(gender=kwargs.get("gender"))
        self._first_name = self._init_first_name(first_name=kwargs.get("first_name"))
        self._last_name = self._init_last_name(last_name=kwargs.get("last_name"))
        self._date_of_birth = self._init_date_of_birth(
            date_of_birth=kwargs.get("date_of_birth")
        )
        self._company = self._init_company(
            company=kwargs.get("company"), companies=companies
        )

        self._email_address = self._init_email(
            email_address=kwargs.get("email_address")
        )
        self._home_phone = kwargs.get("home_phone", FAKE.format('phone_number'))
        self._mobile_phone = kwargs.get("mobile_phone", FAKE.format('phone_number'))

    def __repr__(self):
        repr_str = f"FakeCustomer(uid={self.uid}, gender={self.gender},"
        repr_str += f" first_name={self.first_name}, last_name={self.last_name})"
        return repr_str

    @property
    def gender(self) -> str:
        """
        str: the gender of the customer
        M: Male
        F: Female
        """
        return self._gender

    @property
    def first_name(self) -> str:
        """
        str: The first name of the customer
        examples: John, Bonnie, Brandy
        """
        return self._first_name

    @property
    def last_name(self) -> str:
        """
        str: The last name of the customer
        examples: Hunter, Smith, Beck
        """
        return self._last_name

    @property
    def date_of_birth(self) -> datetime.date:
        """
        datetime.date: The datee of birth of the customer
        """
        return self._date_of_birth

    @property
    def company(self) -> FakeCompany:
        """
        FakeCompany: The Fake Company Associated with the Customer
        examples: FakeCompany('Berger-Phillips'), FakeCompany('Gonzales-Patel')
        """
        return self._company

    @property
    def email_address(self) -> str:
        """
        str: The email address associated with the customer
        examples: john83@gmail.com, bautistaj@trujillomiller.co.uk
        """
        return self._email_address

    @property
    def home_phone(self) -> str:
        """
        str: The Customer's home phone number
        examples: 8593210701, (344)045-3752
        """
        return self._home_phone

    @property
    def mobile_phone(self) -> str:
        """
        str: The Customers' mobile phone's number
        examples: 8593210701, (344)045-3752
        """
        return self._mobile_phone

    def _init_first_name(self, first_name: str = None) -> str:
        """
        Assign or generates a gender appropriate first name

        Returns:
            str: Customer's first name
        """
        if first_name and isinstance(first_name, str):
            first_name_ = first_name
        elif first_name:
            raise TypeError("first_name kwarg should an instance of str")
        elif self.gender == "F":
            first_name_ = FAKE.format('first_name_female')
        else:
            first_name_ = FAKE.format('first_name_male')
        return first_name_

    def _init_last_name(self, last_name: str = None) -> str:
        """
        Assign or generate a gender appropriate last name

        Returns:
            str: Customer's last name
        """
        if last_name and isinstance(last_name, str):
            last_name_ = last_name
        elif last_name:
            raise TypeError("last_name kwarg should be a an instance of str")
        elif self.gender == "F":
            last_name_ = FAKE.format('last_name_female')
        else:
            last_name_ = FAKE.format('last_name_male')
        return last_name_

    def _init_email(self, email_address: str = None) -> str:
        """
        Generates an email address that is highly probable to be consistent
        with the customer's first, last name, date of birth and company

        Returns:
            str: email address
        """
        if email_address and isinstance(email_address, str):
            return email_address
        if email_address:
            raise TypeError("email_address kwarg should be an instance of str ")
        fake_email = str(
            FakeEmail(
                self.first_name,
                self.last_name,
                date_of_birth=self.date_of_birth,
                company_domain=self.company.get_company_domain(),
                config=self.config,
            )
        )
        return fake_email

    @classmethod
    def _init_date_of_birth(cls, date_of_birth: datetime.date = None) -> datetime.date:
        """
        Assign or generate a date of birth
        Return:
            datetime.date: date of birth
        """
        if date_of_birth and isinstance(date_of_birth, datetime.date):
            return date_of_birth
        if date_of_birth:
            raise TypeError(
                "date_of_birth kwarg should be an instance of datetime.date"
            )
        return FAKE.format('date_of_birth')

    @classmethod
    def _init_gender(cls, gender: str = None) -> str:
        """
        Assign or generate a a gender for the Fake Customer
        Return:
            str: gender, M/F
        """
        if gender and isinstance(gender, str):
            if gender in {"M", "F"}:
                return gender
            raise ValueError("Not a recognized Value for gender, ie: M/F")
        if gender:
            raise TypeError("gender kwarg should be an instance of str")
        return FAKE.format('simple_profile').get('sex')

    def _init_company(
            self, company: FakeCompany = None, companies: Dict[FakeCompany, float] = None
    ) -> FakeCompany:
        """
        Assign or generate a company to be associated with the Customer

        Returns:
            FakeCompany: The associated company for the customer
        """
        if company and isinstance(company, FakeCompany):
            # If a company information is provvided
            company_out = company
        elif company:
            raise TypeError("Company kwarg should be an instance of FakeCompany")
        else:
            if companies:
                # Pick one at random from the companies provided
                if (
                        not isinstance(companies, dict)
                        or not isinstance(list(companies.keys())[0], FakeCompany)
                        or not isinstance(list(companies.values())[0], float)
                ):
                    raise TypeError(
                        "Companies kwargs needs to be a Weighted Dict of {FakeCompany: float} "
                    )
                company_out = random_choice_non_normalized_weight_dict(companies)
            else:
                # Generate one
                company_out = FakeCompany(config=self.config)
        return company_out
