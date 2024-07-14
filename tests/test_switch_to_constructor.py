import random
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestConstructorSwitch:
    def test_switch_constructor_div_success(self):
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
            expected_conditions.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(rand_email)  # "Email"
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('Umbrella')  # Пароль
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        assert driver.find_element(*TestLocators.MAKE_BURGER).text == 'Соберите бургер'
        print('Вход в конструктор бургеров из личного кабинета по клику на Конструктор')
        driver.quit()

    def test_logo_button_switch_constructor_div_success(self):
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
            expected_conditions.element_to_be_clickable(TestLocators.ENTER_BUTTON))
        driver.find_element(*TestLocators.ENTER_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT).send_keys(rand_email)  # "Email"
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys('Umbrella')  # Пароль
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.LOGO_BUTTON_PERSONAL_ACCOUNT_PAGE).click()
        assert driver.find_element(*TestLocators.MAKE_BURGER).text == 'Соберите бургер'
        print('Вход в конструктор бургеров из личного кабинета по кнопке Stellar Burgers')
        driver.quit()
