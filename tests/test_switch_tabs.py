from selenium.webdriver.common.by import By

from data import Locator


class TestSwitchTabs:
    def test_switch_tabs_bread(self, driver, login_page, authorization_login, authorization_password,
                               click_button_registration, button_designer):
        # Кликнуть по вкладке Соусы и проверить, что переход совершен, и переключиться обратно
        driver.find_element(By.XPATH, Locator.tab_sause()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_sause()).get_attribute('class')

        driver.find_element(By.XPATH, Locator.tab_bread()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_bread()).get_attribute('class')

        # Кликнуть по вкладке Начинки и проверить, что переход совершен, и переключиться обратно
        driver.find_element(By.XPATH, Locator.tab_stuffing()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_stuffing()).get_attribute('class')

        driver.find_element(By.XPATH, Locator.tab_bread()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_bread()).get_attribute('class')

        driver.quit()

    def test_switch_tabs_sause(self, driver, login_page, authorization_login, authorization_password,
                               click_button_registration, button_designer):
        # Кликнуть по вкладке Соусы и проверить, что переход совершен
        driver.find_element(By.XPATH, Locator.tab_sause()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_sause()).get_attribute('class')

        # Кликнуть по вкладке Начинки и проверить, что переход совершен, и переключиться обратно
        driver.find_element(By.XPATH, Locator.tab_stuffing()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_stuffing()).get_attribute('class')

        driver.find_element(By.XPATH, Locator.tab_sause()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_sause()).get_attribute('class')

        driver.quit()

    def test_switch_tabs_stuffing(self, driver, login_page, authorization_login, authorization_password,
                                  click_button_registration, button_designer):

        # Кликнуть по вкладке Начинки и проверить, что переход совершен
        driver.find_element(By.XPATH, Locator.tab_stuffing()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_stuffing()).get_attribute('class')

        # Кликнуть по вкладке Соусы и проверить, что переход совершен, и переключиться обратно
        driver.find_element(By.XPATH, Locator.tab_sause()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_sause()).get_attribute('class')

        driver.find_element(By.XPATH, Locator.tab_stuffing()).click()
        assert 'current' in driver.find_element(By.XPATH, Locator.allocation_stuffing()).get_attribute('class')

        driver.quit()
