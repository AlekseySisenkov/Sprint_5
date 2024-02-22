from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestDesigner:
    def test_from_personal_cabinet_in_designer(self, driver, authorization, button_personal_cabinet):
        # Найти и кликнуть по кнопке "Конструктор"
        driver.find_element(*Locator.BUTTON_DESIGNER).click()

        # Проверить, что переход в Конструктор произведен
        assert (WebDriverWait(driver, 3)
                .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.HEADER_ASSEMBLE_BURGER))))
