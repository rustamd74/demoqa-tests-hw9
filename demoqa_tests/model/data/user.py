import datetime
from enum import Enum
from dataclasses import dataclass


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    current_address: str
    birthday: datetime.date
    subject: str
    hobbies: str
    picture: str
    gender: Gender
    state: str
    city: str
