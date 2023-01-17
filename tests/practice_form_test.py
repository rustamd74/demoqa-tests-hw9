from datetime import date

from selene.support.shared import browser

from demoqa_tests.model.data.user import Gender, User, Subject, Hobbies, State, City
from demoqa_tests.model.pages import practice_form


def test_student_registration():
    test_student = User(first_name='John', last_name='Doe', email='johndoe@gmail.com', phone_number='2223331110',
                        current_address='221b, Baker street', birthday=date(2004, 3, 4), subject=[Subject.],
                        hobbies=[Hobbies.], gender=Gender.Male, picture='python_label.png', state='Uttar Pradesh',
                        city='Lucknow')

    practice_form.Practice_form.open_page(test_student)
    practice_form.Practice_form.submit()

    practice_form.Practice_form.assert_registration_student(test_student)
