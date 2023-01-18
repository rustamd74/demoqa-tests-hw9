import datetime
from enum import Enum
from dataclasses import dataclass
from typing import List


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


class Subject(Enum):
    Maths = 'Maths'
    Accounting = 'Accounting'
    Arts = 'Arts'
    Social_Studies = 'Social Studies'
    English = 'English'
    Chemistry = 'Chemistry'
    Physics = 'Physics'
    Computer_Science = 'Computer Science'
    Economics = 'Economics'
    History = 'History'
    Civics = 'Civics'
    Commerce = 'Commerce'
    Biology = 'Biology'
    Hindi = 'Hindi'


class Hobbies(Enum):
    Music = 1
    Reading = 2
    Sports = 3


class State(Enum):
    NCR = 'NCR'
    Uttar_Pradesh = 'Uttar Pradesh'
    Haryana = 'Haryana'
    Rajasthan = 'Rajasthan'


class City(Enum):
    Karnal = 'Karnal'
    Panipat = 'Panipat'
    Delhi = 'Delhi'
    Gurgaon = 'Gurgaon'
    Noida = 'Noida'
    Agra = 'Agra'
    Merrut = 'Merrut'
    Lucknow = 'Lucknow'
    Jaipur = 'Jaipur'
    Jaiselmer = 'Jaiselmer'


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


user_test = User(first_name='John', last_name='Doe', email='johndoe@gmail.com', phone_number='2223331110',
                 current_address='221b, Baker street', birthday=datetime.date(2004, 3, 4),
                 subject=[Subject.Computer_Science, Subject.Maths],
                 hobbies=[Hobbies.Sports, Hobbies.Music], gender=Gender.Male, picture='python_label.png',
                 state=State.Uttar_Pradesh,
                 city=City.Lucknow)
