import pytest
from selene import command, have
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 800
    browser.config.window_width = 1400

    yield
    browser.quit()
