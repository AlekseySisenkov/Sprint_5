from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestOutput:
    def test_output(self, driver, authorization, button_personal_cabinet):
        # Добавить ожидание загрузки кнопки "Выход"
        (WebDriverWait(driver, 5).
         until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.OUTPUT))))

        # Найти кнопку "Выход" и кликнуть по ней
        driver.find_element(*Locator.BUTTON_OUTPUT).click()

        # Проверить, что произошел переход на страницу авторизации
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Восстановить пароль")))
