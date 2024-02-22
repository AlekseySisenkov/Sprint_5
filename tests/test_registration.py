from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Locator
from data import New


class TestRegistration:
    def test_registration_valid(self, driver, registration_page):

        # Найти поле "Имя" и заполнить его
        driver.find_element(*Locator.INPUT_NAME).send_keys("test")

        # Найти поле "Email" и заполнить его
        driver.find_element(*Locator.INPUT_EMAIL).send_keys(New().generate_login())

        # Найти поле "Пароль" и заполнить его
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys(New().generate_password())

        # Найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locator.BUTTON_REGISTRATION).click()

        # Проверить, что произошел переход на страницу авторизации
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Восстановить пароль")))

    def test_registration_invalid_password(self, driver, registration_page):

        # Найти поле "Пароль" и заполнить его некорректным паролем
        driver.find_element(*Locator.INPUT_PASSWORD).send_keys("pass")

        # Найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*Locator.BUTTON_REGISTRATION).click()

        # Проверить, что возникло сообщение о некорректном пароле
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locator.MESSAGE_INVALID_PASSWORD)))
