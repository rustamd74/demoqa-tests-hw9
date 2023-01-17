from selene import command, have
from selene.support.shared import browser
from demoqa_tests.model.controls import Radiobutton, Datepicker, Checkbox, Dropdown
from demoqa_tests.model.data.user import User
from demoqa_tests.utils import file_path


class Practice_form:
    def __init__(self, user):
        self.user=user

    def open_page(self):
        browser.open('/automation-practice-form')

    def full_name(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)

    def full_contact(self):
        browser.element('#userEmail').type(self.user.email)
        browser.element('#userNumber').type(self.user.phone_number)

    def select_gender(self):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_value(self.user.gender)

    def date_birthday(self):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.select_date(self.user.birthday)

    def subject(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()

    def set_hobbies(self):
        set_hobbies = Checkbox(browser.element('[for="hobbies-checkbox-3"]')).perform(command.js.scroll_into_view)
        set_hobbies.select_hobbies(browser.all('[for^=hobbies-checkbox]'), self.user.hobbies)

    def insert_picture(self):
        relative_path = 'resources/python_label.png'
        path = file_path.create_path(relative_path)
        browser.element('#uploadPicture', path)

    def full_address(self):
        browser.element('#currentAddress').type(self.user.current_address)

    def select_state(self):
        dropdown = Dropdown('#state')
        dropdown.select(self.user.state)

    def select_city(self):
        dropdown = Dropdown('#city')
        dropdown.select(self.user.city)

    def submit(self):
        browser.element('#submit').press_enter()

    def assert_registration_student(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.phone_number,
                             user.birthday, user.subject, user.hobbies, user.picture, user.current_address,
                             f'{user.state} {user.city}'))
