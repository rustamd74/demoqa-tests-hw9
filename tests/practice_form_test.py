from demoqa_tests.model.data.user import user_test
from demoqa_tests.model.pages.practice_form import Practice_form


def test_student_registration():
    automation_form = Practice_form(user_test)
    automation_form.open_page()
    automation_form.fill_form()

    automation_form.assert_registration_student()
