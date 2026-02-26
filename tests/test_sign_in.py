import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.constants import CredentialsData
from util.constants import Urls
from util.locators import GeneralLocators
from util.locators import SignInLocators
from util.locators import ConstructorLocators

class TestSignIn:
    # Метод проверки входа (авторизации).
    # Для оптимизации была использована параметризация с URL (ссылка на страницу) откуда начинается тест,
    # и соответствующей кнопкой по заданию.
    @pytest.mark.parametrize('enter_button, url', [
        (GeneralLocators.ENTER_IN_ACCOUNT_BUTTON, Urls.BASE_URL),
        (GeneralLocators.PERSONAL_CABINET_BUTTON, Urls.BASE_URL),
        (GeneralLocators.LOGIN_TEXT, Urls.REGISTER_URL),
        (GeneralLocators.LOGIN_TEXT, Urls.FOGOT_PASSWORD_URL),
    ])
    def test_sign_in(self, enter_button, url, driver):
        credentials = CredentialsData.get_test_credentials()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        enter_button = wait.until(expected_conditions.element_to_be_clickable(enter_button))
        enter_button.click()
        email = wait.until(expected_conditions.visibility_of_element_located(SignInLocators.EMAIL_TEXTFIELD))
        email.send_keys(credentials.email)
        password = wait.until(expected_conditions.visibility_of_element_located(SignInLocators.PASS_TEXTFIELD))
        password.send_keys(credentials.password)
        login_button = wait.until(expected_conditions.element_to_be_clickable(SignInLocators.LOGIN_BUTTON))
        login_button.click()
        order_button = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.PLACE_AN_ORDER_BUTTON))
        assert order_button.is_displayed()
