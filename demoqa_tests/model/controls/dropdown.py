from selene import have


class Dropdown:
    def __init__(self, element, elements):
        self.element = element
        self.elements = elements

    def select(self, by_text):
        self.element.click()
        self.elements.element_by(have.exact_text(by_text)).click()
