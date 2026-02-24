from selenium.webdriver.common.by import By

def get_test_credentials():
    from util.credentials_generator import Credentials
    return Credentials('Arina', 'arinakhugaeva3637000@bk.ru', '123456')

STELLAR_BURGERS = 'https://stellarburgers.education-services.ru/'

REGISTER_URL = 'https://stellarburgers.education-services.ru/register'

FOGOT_PASSWORD_URL = 'https://stellarburgers.education-services.ru/forgot-password'

DOMAINS = [
    '@mail.ru',
    '@ya.ru',
    '@gmail.com',
    '@list.ru',
    '@bk.ru',
    '@yandex.ru',
    '@ritm.ru',
    '@bitm.ru',
    '@mts.ru',
    '@asd.ru',
]

NAME_TEXTFIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Текстфилд "Имя".

EMAIL_TEXTFIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Текстфилд "Email".

PASS_TEXTFIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") # Текстфилд "Пароль".

REGISRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться".

LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']") # Кнопка "Войти".

SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']") # Кнопка "Сохранить".

ERROR_REGISTRATION_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']") # Текст-уведомление "Некорректный пароль".

ENTER_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт".

PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ".

PERSONAL_CABINET_BUTTON = (By.LINK_TEXT, "Личный Кабинет") # Кнопка с текстом "Личный Кабинет".

LOGIN_TEXT = (By.LINK_TEXT, "Войти") # Кнопка с текстом "Войти".

REGISRATION_TEXT = (By.LINK_TEXT, "Зарегистрироваться") # Кнопка с текстом "Зарегистрироваться".

CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']") # Кнопка с текстом "Конструктор" для перехода в "Конструктор".

LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2") # Кнопка-логотип "stellar burgers" для перехода в "Конструктор".

LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход".

AUTH_FORM = (By.CLASS_NAME, "Auth_login__3hAey") # Форма авторизации.

BULKI_SECTION_BUTTON = (By.XPATH, "//span[text()='Булки']/..") # Кнопка перехода в раздел "Булки".

SAUCE_SECTION_BUTTON = (By.XPATH, "//span[text()='Соусы']/..") # Кнопка перехода в раздел "Соусы".

FILLINGS_SECTION_BUTTON = (By.XPATH, "//span[text()='Начинки']/..") # Кнопка перехода в раздел "Начинки".
