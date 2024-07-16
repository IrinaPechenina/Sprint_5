import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestPersonalAccount:

    def test_switch_personal_account_success(self, driver):
        driver.get(data.HOME_PAGE_URL)
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()

        # Ожидание загрузки страницы входа
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON))

        if driver.find_element(*TestLocators.ENTER_BUTTON):
            print('Работает переход по клику на «Личный кабинет»!')
