from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Locator


class TestDesigner:
    def test_from_personal_cabinet_in_designer(self, driver, login_page, authorization_login, authorization_password,
                                               click_button_registration, button_personal_cabinet, button_designer):

        # Проверить, что переход в Конструктор произведен
        assert (WebDriverWait(driver, 3)
                .until(expected_conditions.visibility_of_element_located((By.XPATH, Locator.header_assemble_burger()))))

        driver.quit()
