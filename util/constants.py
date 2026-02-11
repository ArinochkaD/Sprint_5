from selenium.webdriver.common.by import By

def get_test_credentials():
    from util.credentials_generator import Credentials
    return Credentials('Arina', 'arinakkk@bk.ru', '123456')

STELLAR_BURGERS = 'https://stellarburgers.education-services.ru/'

REGISTER_ENDPOINT = 'https://stellarburgers.education-services.ru/register'

FOGOT_PASSWORD_ENDPOINT = 'https://stellarburgers.education-services.ru/forgot-password'

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

NAME_TEXTFIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

EMAIL_TEXTFIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

PASS_TEXTFIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

REGISRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")

ERROR_REGISTRATION_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")

ENTER_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

PERSONAL_CABINET_BUTTON = (By.LINK_TEXT, "Личный Кабинет")

LOGIN_TEXT = (By.LINK_TEXT, "Войти")

REGISRATION_TEXT = (By.LINK_TEXT, "Зарегистрироваться")
