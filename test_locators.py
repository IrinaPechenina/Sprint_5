from selenium.webdriver.common.by import By


class TestLocators:
    # Форма регистрации
    NAME_FIELD = By.XPATH, '(.//input[@type="text"])[1]'  # Поле ввода "Имя"
    EMAIL_FIELD = By.XPATH, '(.//input[@type="text"])[2]'  # Поле ввода "Email"
    PASSWORD_FIELD = By.XPATH, './/input[@type="password"]'  # Поле ввода "Пароль"
    CONFIRM_REGISTRATION = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка 'Зарегистрироваться'
    REGISTRATION_ERROR_MESSAGE = By.XPATH, './/p[text()="Некорректный пароль"]'  # ошибка некорретного пароля

    # Вход
    LOGIN_ACCOUNT_BUTTON_MAIN_PAGE = By.XPATH, './/button[text()="Войти в аккаунт"]'  # кнопка «Войти в аккаунт» на
    # главной
    ENTER_LINK = By.XPATH, './/a[text()="Войти"]'  # ссылка на страницу входа
    ENTER_BUTTON = By.XPATH, './/button[text()="Войти"]'  # кнопка "Войти" после успешн регистрации
    REGISTRATION_LINK = By.XPATH, './/a[text() = "Зарегистрироваться"]'  # ссылка на форму регистрации
    PASSWORD_RECOVERY_BUTTON = By.XPATH, '//a[text()="Восстановить пароль"]'  # Восстановить пароль

    EMAIL_INPUT = By.XPATH, './/input[@name="name"]'  # Поле ввода Email в личном кабинете
    PASSWORD_INPUT = By.XPATH, './/input[@type="password"]'  # Поле ввода пароля в личном кабинете

    # переход по клику на «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE = By.XPATH, '//*[text()="Личный Кабинет"]'  # кнопка «Личный кабинет»

    # Переход из личного кабинета в конструктор
    CONSTRUCTOR_BUTTON_PERSONAL_ACCOUNT_PAGE = By.XPATH, './/p[text()="Конструктор"]'  # по клику на «Конструктор»
    LOGO_BUTTON_PERSONAL_ACCOUNT_PAGE = By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]'  # по клику на логотип
    # Stellar Burgers
    MAKE_BURGER = By.XPATH, './/h1[text()="Соберите бургер"]'  # заголовок раздела Конструктор

    # выход по кнопке «Выйти» в личном кабинете
    LOGOUT_BUTTON_PERSONAL_ACCOUNT = By.XPATH, './/button[text()="Выход"]'  # выход

    # Раздел «Конструктор»
    BREAD_SECTION = By.XPATH, './/span[@class="text text_type_main-default" and text()="Булки"]'  # «Булки»-раздел
    BREAD_HEADER = By.XPATH, '//h2[@class="text text_type_main-medium mb-6 mt-10" and text()="Булки"]'  # «Булки»-заголовок
    SAUCES_SECTION = By.XPATH, './/span[@class="text text_type_main-default" and text()="Соусы"]'  # «Соусы»-раздел
    SAUCES_HEADER = By.XPATH, './/h2[text()="Соусы"]'  # «Соусы»-заголовок
    FILLINGS_SECTION = By.XPATH, './/span[@class="text text_type_main-default" and text()="Начинки"]'  #
    # «Начинки»-раздел
    FILLINGS_HEADER = By.XPATH, './/h2[text()="Начинки"]'  # «Начинки»-заголовок
