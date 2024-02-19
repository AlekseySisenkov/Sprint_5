import secrets

import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Ref
from data import Locator
from data import New


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='function')
def main_page(driver):
    return driver.get(Ref.main_page())


@pytest.fixture(scope='function')
def registration_page(driver):
    return driver.get(Ref.registration_page())


@pytest.fixture(scope='function')
def forgot_password_page(driver):
    return driver.get(Ref.forgot_password_page())


@pytest.fixture(scope='function')
def login_page(driver):
    return driver.get(Ref.login_page())


@pytest.fixture(scope='function')
def authorization_login(driver):
    return driver.find_element(By.XPATH, Locator.name_and_email()).send_keys("alekseysisenkov5000@gmail.com")


@pytest.fixture(scope='function')
def authorization_password(driver):
    return driver.find_element(By.XPATH, Locator.email_and_pass()).send_keys("password")


@pytest.fixture(scope='function')
def click_button_registration(driver):
    return driver.find_element(By.XPATH, Locator.button_registration()).click()


@pytest.fixture(scope='function')
def delay_input(driver):
    return WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located((By.XPATH, Locator.button_input())))


@pytest.fixture(scope='function')
def click_button_input(driver):
    return driver.find_element(By.XPATH, Locator.button_input()).click()


@pytest.fixture(scope='function')
def button_personal_cabinet(driver):
    return driver.find_element(By.XPATH, Locator.button_personal_cabinet()).click()


@pytest.fixture(scope='function')
def button_in(driver):
    return driver.find_element(By.XPATH, Locator.button_in()).click()


@pytest.fixture(scope='function')
def button_designer(driver):
    return driver.find_element(By.XPATH, Locator.button_designer()).click()


@pytest.fixture(scope='function')
def delay_personal_cabinet(driver):
    return WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                           Locator.field_login())))
