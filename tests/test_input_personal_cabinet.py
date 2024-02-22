from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestPersonalCabinet:
    def test_input_personal_cabinet(self, driver, authorization):
        # Найти и кликнуть по кнопке "Личный кабинет"
        driver.find_element(*Locator.BUTTON_PERSONAL_CABINET).click()

        # Проверить, что вход в личный кабинет произведен
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH,
                                                                                               Locator.FIELD_LOGIN)))
