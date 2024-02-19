from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestPersonalCabinet:
    def test_input_personal_cabinet(self, driver, login_page, authorization_login, authorization_password,
                                    click_button_registration, button_personal_cabinet, delay_personal_cabinet):

        # Проверить, что вход в личный кабинет произведен
        assert "alekseysisenkov5000@gmail.com" in driver.find_element(By.XPATH,
                                                                      Locator.field_login()).get_attribute('value')

        driver.quit()
