import datetime
from typing import List

from selene import have, command
from selene.support.by import name
from selene.support.shared import browser
from demoqa_tests.model.controls.radio_button import Radiobutton
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.date_picker import Datepicker
from demoqa_tests.model.data.user import Gender, State, City, User
from demoqa_tests.utils.file_path import create_path


class Practice_form:

    def open_page(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
            command.js.remove)
        if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
            ads.perform(command.js.remove)
        return self

    def first_name(self, first_name: str):
        browser.element('#firstName').type(first_name)
        return self

    def last_name(self, last_name: str):
        browser.element('#lastName').type(last_name)
        return self

    def full_contact(self, email: str, phone: str):
        browser.element('#userEmail').type(email)
        browser.element('#userNumber').type(phone)
        return self

    def select_gender(self, student_gender: Gender):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_value(student_gender.value)
        return self

    def date_birthday(self, birthday: datetime.date):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.select_date(birthday)
        return self

    def subject(self, subject: List):
        for elem in subject:
            browser.element('#subjectsInput').type(elem.value).press_enter()
        return self

    def set_hobbies(self, hobbies: List):
        set_hobbies = Checkbox(browser.all('[for^="hobbies-checkbox"]'))
        set_hobbies.select_hobbies(hobbies)
        return self

    def scrool_page(self):
        browser.element('#state').perform(command.js.scroll_into_view)

    def insert_picture(self, file: str):
        create_path('#uploadPicture', file)
        # browser.element('#uploadPicture').set_value(path)

        return self

    def full_address(self, address):
        browser.element('#currentAddress').set_value(address)
        return self

    def select_state(self, state: State):
        dropdown = Dropdown(browser.element('#state'), browser.all('[id^=react-select][id*=option]'))
        dropdown.select(state.value)
        return self

    def select_city(self, city: City):
        dropdown = Dropdown(browser.element('#city'), browser.all('[id^=react-select][id*=option]'))
        dropdown.select(city.value)
        return self

    def submit(self):
        browser.element('#submit').press_enter()

    def fill_form(self, student: User):
        self.first_name(student.first_name)
        self.last_name(student.last_name)
        self.full_contact(student.email, student.phone_number)
        self.select_gender(student.gender)
        self.date_birthday(student.birthday)
        self.subject(student.subject)
        self.set_hobbies(student.hobbies)
        self.scrool_page()
        self.insert_picture(student.picture)
        self.full_address(student.address)
        self.select_state(student.state)
        self.select_city(student.city)
        self.submit()

    @classmethod
    def assert_registration_student(cls, student):
        browser.element('.table').all('td').even.should(
            have.texts(
                f'{student.first_name} {student.last_name}',
                student.email,
                student.gender,
                student.phone_number,
                student.birthday,
                ', '.join(subject._name_ for subject in student.subject),
                ', '.join(hobbies._name_ for hobbies in student.hobbies),
                student.picture.split('/')[-1],
                student.address,
                f'{student.state} {student.city}'))
