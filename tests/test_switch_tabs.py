from selenium.webdriver.common.by import By

from data import Locator


class TestSwitchTabs:
    def test_switch_tabs_bread(self, driver, authorization, button_designer):
        # Кликнуть по вкладке Соусы и проверить, что переход совершен, и переключиться обратно
        driver.find_element(*Locator.TAB_SAUSE).click()
        assert 'current' in driver.find_element(*Locator.TAB_SAUSE).get_attribute('class')

        driver.find_element(*Locator.TAB_BREAD).click()
        assert 'current' in driver.find_element(*Locator.TAB_BREAD).get_attribute('class')

        # Кликнуть по вкладке Начинки и проверить, что переход совершен, и переключиться обратно
        driver.find_element(*Locator.TAB_STUFFING).click()
        assert 'current' in driver.find_element(*Locator.TAB_STUFFING).get_attribute('class')

        driver.find_element(*Locator.TAB_BREAD).click()
        assert 'current' in driver.find_element(*Locator.TAB_BREAD).get_attribute('class')

    def test_switch_tabs_sause(self, driver, authorization, button_designer):
        # Кликнуть по вкладке Соусы и проверить, что переход совершен
        driver.find_element(*Locator.TAB_SAUSE).click()
        assert 'current' in driver.find_element(*Locator.TAB_SAUSE).get_attribute('class')

        # Кликнуть по вкладке Начинки и проверить, что переход совершен, и переключиться обратно
        driver.find_element(*Locator.TAB_STUFFING).click()
        assert 'current' in driver.find_element(*Locator.TAB_STUFFING).get_attribute('class')

        driver.find_element(*Locator.TAB_SAUSE).click()
        assert 'current' in driver.find_element(*Locator.TAB_SAUSE).get_attribute('class')

    def test_switch_tabs_stuffing(self, driver, authorization, button_designer):

        # Кликнуть по вкладке Начинки и проверить, что переход совершен
        driver.find_element(*Locator.TAB_STUFFING).click()
        assert 'current' in driver.find_element(*Locator.TAB_STUFFING).get_attribute('class')

        # Кликнуть по вкладке Соусы и проверить, что переход совершен, и переключиться обратно
        driver.find_element(*Locator.TAB_SAUSE).click()
        assert 'current' in driver.find_element(*Locator.TAB_SAUSE).get_attribute('class')

        driver.find_element(*Locator.TAB_STUFFING).click()
        assert 'current' in driver.find_element(*Locator.TAB_STUFFING).get_attribute('class')
