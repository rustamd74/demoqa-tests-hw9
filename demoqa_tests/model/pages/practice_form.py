from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls.radio_button import Radiobutton
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.dropdown import Dropdown
from demoqa_tests.model.controls.date_picker import Datepicker
from demoqa_tests.utils import file_path


class Practice_form:
    def __init__(self, user):
        self.user = user

    def open_page(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)

        return self

    def full_name(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)

        return self

    def full_contact(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.phone_number)

        return self

    def select_gender(self, user):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_value(user.gender)

        return self

    def date_birthday(self, user):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.select_date(user.birthday)

        return self

    def subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()

        return self

    def set_hobbies(self, user):
        set_hobbies = Checkbox(browser.element('[for="hobbies-checkbox-3"]'))
        set_hobbies.select_hobbies(browser.all('[for^=hobbies-checkbox]'), user.hobbies)

        return self

    def scrool_page(self):
        browser.element('#state').perform(command.js.scroll_into_view)

    def insert_picture(self):
        relative_path = 'resources/python_label.png'
        path = file_path.create_path('#uploadPicture', relative_path)
        browser.element('#uploadPicture', path)

        return self

    def full_address(self, user):
        browser.element('#currentAddress').type(user.current_address)

        return self

    def select_state(self, user):
        dropdown = Dropdown('#state')
        dropdown.select(user.state)

        return self

    def select_city(self, user):
        dropdown = Dropdown('#city')
        dropdown.select(user.city)

        return self

    def submit(self):
        browser.element('#submit').press_enter()

    def fill_form(self, user):
        self.full_name(user)\
            .full_contact(user)\
            .select_gender(user)\
            .date_birthday(user)\
            .subject(user)\
            .insert_picture()\
            .set_hobbies(user)\
            .full_address(user)\
            .select_state(user)\
            .select_city(user)
        self.submit()

    @classmethod
    def assert_registration_student(cls, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.phone_number,
                             user.birthday, user.subject, user.hobbies, user.picture, user.current_address,
                             f'{user.state} {user.city}'))
