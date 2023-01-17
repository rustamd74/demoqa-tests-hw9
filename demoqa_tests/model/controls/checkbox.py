from selene.support.conditions import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def select_hobbies(self, *by_texts):
        for value in by_texts:
            self.element.element_by(have.text(value)).click()
