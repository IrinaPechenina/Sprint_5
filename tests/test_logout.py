import random
import data
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestLogOut:
    def test_logout_from_personal_account_success(self, driver):
        driver.get(data.REG_URL)
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Marina')  # "Имя"
        rand_email = f"marina_pechenina_8_{random.randint(100, 999)}@yandex.ru"  # "Email"
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(rand_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('Umbrella_3')  # Пароль
        # Ожидание загрузки страницы регистрации
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CONFIRM_REGISTRATION))
        driver.find_element(*TestLocators.CONFIRM_REGISTRATION).click()  # Кнопка "Зарегистрироваться"
        # Ожидание загрузки страницы входа
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(rand_email)  # ввели "Email"
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('Umbrella_3')  # ввели Пароль
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON_PERSONAL_ACCOUNT))
        driver.find_element(*TestLocators.LOGOUT_BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_LINK))
        assert driver.find_element(*TestLocators.REGISTRATION_LINK).text == 'Зарегистрироваться'
        print('Произведен выход из личного кабинета')
