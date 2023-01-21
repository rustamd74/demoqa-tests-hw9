from typing import List

from selene import have


class Checkbox:
    def __init__(self, element):
        self.element = element

    def select_hobbies(self, hobbies: List):
        for value in hobbies:
            self.element.element_by(have.exact_text(value.name)).click()
