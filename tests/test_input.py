from selenium.webdriver.common.by import By

from data import Locator


class TestInput:
    def test_input_account(self, driver, main_page, click_button_input,
                           authorization_login, authorization_password, click_button_registration, delay_input):

        # Проверить, что авторизация произошла
        assert driver.find_element(By.XPATH, Locator.button_input()).text == 'Оформить заказ'

        driver.quit()

    def test_input_personal_cabinet(self, driver, main_page, button_personal_cabinet, authorization_login,
                                    authorization_password, click_button_registration, delay_input):

        # Проверить, что авторизация произошла
        assert driver.find_element(By.XPATH, Locator.button_input()).text == 'Оформить заказ'

        driver.quit()

    def test_input_form_registration(self, driver, registration_page, button_in, authorization_login,
                                     authorization_password, click_button_registration, delay_input):

        # Проверить, что авторизация произошла
        assert driver.find_element(By.XPATH, Locator.button_input()).text == 'Оформить заказ'

        driver.quit()

    def test_input_password_recovery(self, driver, forgot_password_page, button_in, authorization_login,
                                     authorization_password, click_button_registration, delay_input):

        # Проверить, что авторизация произошла
        assert driver.find_element(By.XPATH, Locator.button_input()).text == 'Оформить заказ'

        driver.quit()
