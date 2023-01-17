from selene.support.conditions import have


class Radiobutton:
    def __init__(self, element):
        self.element = element

    def select_value(self, text):
        self.element.element_by(have.value(text)).element('..').click()
