import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestConstructor:

    def test_switch_bread_section_success(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*TestLocators.BREAD_HEADER).click()
        WebDriverWait(driver, 3).until(
                    expected_conditions.element_to_be_clickable(TestLocators.BREAD_SECTION))
        assert driver.find_element(*TestLocators.BREAD_HEADER).text == 'Булки'
        print('Булки найдены!')

    def test_switch_sauces_section_success(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*TestLocators.SAUCES_HEADER).click()
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        assert driver.find_element(*TestLocators.SAUCES_HEADER).text == 'Соусы'
        print('Соусы найдены!')

    def test_switch_fillings_section_success(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*TestLocators.FILLINGS_HEADER).click()
        driver.find_element(*TestLocators.FILLINGS_SECTION).click()
        assert driver.find_element(*TestLocators.FILLINGS_HEADER).text == 'Начинки'
        print('Начинки найдены!')
