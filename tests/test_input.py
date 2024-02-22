from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestInput:
    def test_input_account(self, driver, main_page):
        # Найти и кликнуть по кнопке "Войти в аккаунт"
        driver.find_element(*Locator.BUTTON_INPUT_ACCOUNT).click()

        # Авторизоваться
        driver.find_element(*Locator.INPUT_EMAIL).send_keys("alekseysisenkov5000@gmail.com")
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys("password")
        driver.find_element(*Locator.BUTTON_INPUT).click()

        # Проверить, что авторизация произошла
        assert WebDriverWait(driver, 3).until(expected_conditions.
                                              visibility_of_element_located((By.XPATH, Locator.BUTTON_PLACE_ORDER)))

    def test_input_personal_cabinet(self, driver, main_page):
        # Найти и кликнуть по кнопке "Личный кабинет"
        driver.find_element(*Locator.BUTTON_PERSONAL_CABINET).click()

        # Авторизоваться
        driver.find_element(*Locator.INPUT_EMAIL).send_keys("alekseysisenkov5000@gmail.com")
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys("password")
        driver.find_element(*Locator.BUTTON_INPUT).click()

        # Проверить, что авторизация произошла
        assert WebDriverWait(driver, 3).until(expected_conditions.
                                              visibility_of_element_located((By.XPATH, Locator.BUTTON_PLACE_ORDER)))

    def test_input_form_registration(self, driver, registration_page):
        # Найти и кликнуть по кнопке "Войти"
        driver.find_element(*Locator.REF_INPUT).click()

        # Авторизоваться
        driver.find_element(*Locator.INPUT_EMAIL).send_keys("alekseysisenkov5000@gmail.com")
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys("password")
        driver.find_element(*Locator.BUTTON_INPUT).click()

        # Проверить, что авторизация произошла
        assert WebDriverWait(driver, 3).until(expected_conditions.
                                              visibility_of_element_located((By.XPATH, Locator.BUTTON_PLACE_ORDER)))

    def test_input_password_recovery(self, driver, forgot_password_page):
        # Найти и кликнуть по кнопке "Войти"
        driver.find_element(*Locator.REF_INPUT).click()

        # Авторизоваться
        driver.find_element(*Locator.INPUT_EMAIL).send_keys("alekseysisenkov5000@gmail.com")
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys("password")
        driver.find_element(*Locator.BUTTON_INPUT).click()

        # Проверить, что авторизация произошла
        assert WebDriverWait(driver, 3).until(expected_conditions.
                                              visibility_of_element_located((By.XPATH, Locator.BUTTON_PLACE_ORDER)))
