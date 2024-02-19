from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestOutput:
    def test_output(self, driver, login_page, authorization_login, authorization_password,
                    click_button_registration, button_personal_cabinet, delay_personal_cabinet):

        # Найти кнопку "Выход" и кликнуть по ней
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, Locator.button_output()))
        driver.find_element(By.XPATH, Locator.button_output()).click()

        # Проверить, что произошел переход на страницу авторизации
        assert WebDriverWait(driver, 3).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "Восстановить пароль")))

        driver.quit()
