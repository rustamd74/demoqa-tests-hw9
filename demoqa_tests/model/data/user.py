import datetime
from enum import Enum
from dataclasses import dataclass
from typing import List


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Subject(Enum):
    pass


class Hobbies(Enum):
    pass


class State(Enum):


class City(Enum):
    pass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    current_address: str
    birthday: datetime.date
    subject: List[Subject]
    hobbies: List[Hobbies]
    picture: str
    gender: Gender
    state: State
    city: City
