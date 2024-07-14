import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestRegistration:

    def test_registration_name_email_password_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Irina')  # "Имя"
        rand_email = f"irina_pechenina_8_{random.randint(100, 999)}@yandex.ru"  # "Email"
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(rand_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('Umbrella')  # Пароль
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CONFIRM_REGISTRATION))
        driver.find_element(*TestLocators.CONFIRM_REGISTRATION).click()  # Кнопка "Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON))
        assert driver.find_element(*TestLocators.ENTER_BUTTON).text == 'Войти'
        print('Регистация пройдена успешно!')
        driver.quit()

    def test_registration_password_with_error(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Irina')  # "Имя"
        rand_email = f"irina_pechenina_8_{random.randint(100, 999)}@yandex.ru"  # "Email"
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(rand_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('Umbr')  # Пароль
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CONFIRM_REGISTRATION))
        driver.find_element(*TestLocators.CONFIRM_REGISTRATION).click()  # Кнопка "Зарегистрироваться"
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_ERROR_MESSAGE))
        assert driver.find_element(*TestLocators.REGISTRATION_ERROR_MESSAGE).text == 'Некорректный пароль'
        print('Найдена ошибка некорректного пароля')
        driver.quit()
