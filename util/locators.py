from selenium.webdriver.common.by import By

class RegistrationLocators:
    """Локаторы страницы Регистрации"""
    NAME_TEXTFIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Текстфилд "Имя".
    EMAIL_TEXTFIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Текстфилд "Email".
    PASS_TEXTFIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Текстфилд "Пароль".
    REGISRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться".
    ERROR_REGISTRATION_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Текст-уведомление "Некорректный пароль".

class SignInLocators:
    """Локаторы страницы Авторизации"""
    EMAIL_TEXTFIELD = RegistrationLocators.EMAIL_TEXTFIELD # Текстфилд "Имя".
    PASS_TEXTFIELD = RegistrationLocators.PASS_TEXTFIELD # Текстфилд "Пароль".
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти".
    AUTH_FORM = (By.CLASS_NAME, "Auth_login__3hAey") # Форма авторизации.
    REGISRATION_TEXT = (By.LINK_TEXT, "Зарегистрироваться") # Кнопка с текстом "Зарегистрироваться".

class PersonalCabinetLocators:
    """Локаторы страницы Личного кабинета"""
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']") # Кнопка "Сохранить".
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход".

class GeneralLocators:
    """Общие локаторы"""
    PERSONAL_CABINET_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Кнопка с текстом "Личный Кабинет".
    ENTER_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт".
    LOGIN_TEXT = (By.LINK_TEXT, "Войти") # Кнопка с текстом "Войти".
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка с текстом "Конструктор" для перехода в "Конструктор".
    LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Кнопка-логотип "stellar burgers" для перехода в "Конструктор".

class ConstructorLocators:
    """Локаторы страницы Конструктора"""
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ".
    BULKI_SECTION_TAB = (By.XPATH, "//span[text()='Булки']/..") # Таб перехода в раздел "Булки".
    SAUCE_SECTION_TAB = (By.XPATH, "//span[text()='Соусы']/..") # Таб перехода в раздел "Соусы".
    FILLINGS_SECTION_TAB = (By.XPATH, "//span[text()='Начинки']/..") # Таб перехода в раздел "Начинки".
