class CredentialsData:
    @staticmethod
    def get_test_credentials():
        from util.credentials_generator import Credentials
        return Credentials('Arina', 'arinakhugaeva3637000@bk.ru', '123456')

class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru/'
    REGISTER_URL = BASE_URL + 'register'
    FOGOT_PASSWORD_URL = BASE_URL + 'forgot-password'

class Domains:
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

class ClassName:
    CONSTRUCTOR_ACTIVE_TAB_NAME = "tab_tab_type_current__2BEPc"