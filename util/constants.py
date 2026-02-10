from selenium.webdriver.common.by import By

STELLAR_BURGERS = 'https://stellarburgers.education-services.ru/'

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
