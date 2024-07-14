from selenium import webdriver
from test_locators import TestLocators


class TestLogIn:

    def test_login_account_main_page_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.LOGIN_ACCOUNT_BUTTON_MAIN_PAGE).click()
        assert driver.find_element(*TestLocators.ENTER_BUTTON).text == 'Войти'
        print('Работает вход по клику на «Войти в аккаунт»!')
        driver.quit()

    def test_login_personal_account_button_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        assert driver.find_element(*TestLocators.ENTER_BUTTON).text == 'Войти'
        print('Работает вход по клику на «Личный кабинет»!')
        driver.quit()

    def test_login_registration_form_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.REGISTRATION_LINK).click()
        driver.find_element(*TestLocators.ENTER_LINK).click()
        assert driver.find_element(*TestLocators.ENTER_BUTTON).text == 'Войти'
        print('Работает вход через кнопку в форме регистрации!')
        driver.quit()

    def test_login_password_recovery_form_success(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        driver.find_element(*TestLocators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*TestLocators.ENTER_LINK).click()
        assert driver.find_element(*TestLocators.ENTER_BUTTON).text == 'Войти'
        print('Работает вход через кнопку в форме восстановления пароля!')
        driver.quit()
