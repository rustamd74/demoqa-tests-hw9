from selene import command, have
from selene.support.shared import browser
from demoqa_tests.model.controls import Radiobutton, Datepicker, Checkbox, Dropdown
from demoqa_tests.model.data.user import User
from demoqa_tests.utils import file_path


class Practice_form:
    def __init__(self, user):
        self.user = user

    def open_page(self):
        browser.open('/automation-practice-form')

        return self

    def full_name(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)

        return self

    def full_contact(self):
        browser.element('#userEmail').type(self.user.email)
        browser.element('#userNumber').type(self.user.phone_number)

        return self

    def select_gender(self):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_value(self.user.gender)

        return self

    def date_birthday(self):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.select_date(self.user.birthday)

        return self

    def subject(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

        return self

    def set_hobbies(self):
        set_hobbies = Checkbox(browser.element('[for="hobbies-checkbox-3"]')).perform(command.js.scroll_into_view)
        set_hobbies.select_hobbies(browser.all('[for^=hobbies-checkbox]'), self.user.hobbies)

        return self

    def insert_picture(self):
        relative_path = 'resources/python_label.png'
        path = file_path.create_path(relative_path)
        browser.element('#uploadPicture', path)

        return self

    def full_address(self):
        browser.element('#currentAddress').type(self.user.current_address)

        return self

    def select_state(self):
        dropdown = Dropdown('#state')
        dropdown.select(self.user.state)

        return self

    def select_city(self):
        dropdown = Dropdown('#city')
        dropdown.select(self.user.city)

        return self

    def submit(self):
        browser.element('#submit').press_enter()

        return self

    def fill_form(self):
        self.full_name()
        self.full_contact()
        self.select_gender()
        self.date_birthday()
        self.subject()
        self.insert_picture()
        self.set_hobbies()
        self.full_address()
        self.select_state()
        self.select_city()
        self.submit()

    def assert_registration_student(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.phone_number,
                             user.birthday, user.subject, user.hobbies, user.picture, user.current_address,
                             f'{user.state} {user.city}'))
