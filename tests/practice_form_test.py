import datetime

from demoqa_tests.model.data.user import User, State, City, Subject, Hobbies, Gender
from demoqa_tests.model.pages.practice_form import Practice_form


def test_student_registration():
    student = User(first_name='John',
                   last_name='Doe',
                   email='johndoe@gmail.com',
                   phone_number='2223331110',
                   current_address="221b, Baker street",
                   birthday=datetime.date(2004, 3, 4),
                   subject=[Subject.Computer_Science, Subject.Maths],
                   hobbies=[Hobbies.Sports, Hobbies.Music],
                   gender=Gender.Male,
                   picture='python_label.png',
                   state=State.Uttar_Pradesh,
                   city=City.Lucknow)
    automation_form = Practice_form()
    automation_form.open_page()
    automation_form.fill_form(student)

    automation_form.assert_registration_student(student)
