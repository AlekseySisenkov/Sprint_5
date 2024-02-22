import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import Locator
from data import Ref


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page(driver):
    driver.get(Ref.MAIN_PAGE)


@pytest.fixture(scope='function')
def registration_page(driver):
    driver.get(Ref.REGISTRATION_PAGE)


@pytest.fixture(scope='function')
def forgot_password_page(driver):
    driver.get(Ref.FORGOT_PASSWORD_PAGE)


@pytest.fixture(scope='function')
def authorization(driver):
    driver.get(Ref.LOGIN_PAGE)
    driver.find_element(*Locator.INPUT_EMAIL).send_keys("alekseysisenkov5000@gmail.com")
    driver.find_element(*Locator.INPUT_PASSWORD).send_keys("password")
    driver.find_element(*Locator.BUTTON_INPUT).click()


@pytest.fixture(scope='function')
def button_personal_cabinet(driver):
    driver.find_element(*Locator.BUTTON_PERSONAL_CABINET).click()


@pytest.fixture(scope='function')
def button_designer(driver):
    driver.find_element(*Locator.BUTTON_DESIGNER).click()
