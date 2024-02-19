from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import Locator
from data import New


class TestRegistration:
    def test_registration_valid(self, driver, registration_page):

        # Найти поле "Имя" и заполнить его
        driver.find_element(By.XPATH, Locator.name_and_email()).send_keys("test")

        # Найти поле "Email" и заполнить его
        driver.find_element(By.XPATH, Locator.email_and_pass()).send_keys(New().generate_login())

        # Найти поле "Пароль" и заполнить его
        driver.find_element(By.XPATH, Locator.password()).send_keys(New().generate_password())

        # Найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(By.XPATH, Locator.button_registration()).click()

        # Проверить, что произошел переход на страницу авторизации
        assert WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Восстановить пароль")))

        driver.quit()

    def test_registration_invalid_password(self, driver, registration_page):

        # Найти поле "Пароль" и заполнить его некорректным паролем
        driver.find_element(By.XPATH, Locator.password()).send_keys("pass")

        # Найти кнопку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(By.XPATH, Locator.button_registration()).click()

        # Проверить, что возникло сообщение о некорректном пароле
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locator.message_invalid_password())))

        driver.quit()
