import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util import constants

class TestSignIn:
    @pytest.mark.parametrize('enter_button, endpoint', [
        (constants.ENTER_IN_ACCOUNT_BUTTON, constants.STELLAR_BURGERS),
        (constants.PERSONAL_CABINET_BUTTON, constants.STELLAR_BURGERS),
        (constants.LOGIN_TEXT, constants.REGISTER_ENDPOINT),
        (constants.LOGIN_TEXT, constants.FOGOT_PASSWORD_ENDPOINT),
    ])
    def test_personal_cabinet(self, enter_button, endpoint):
        credentials = constants.get_test_credentials()

        driver = webdriver.Chrome()
        driver.get(endpoint)

        wait = WebDriverWait(driver, 100)

        enter_button_element = wait.until(expected_conditions.element_to_be_clickable(enter_button))
        
        enter_button_element.click()

        email = wait.until(expected_conditions.visibility_of_element_located(constants.EMAIL_TEXTFIELD))

        email.send_keys(credentials.email)

        password = wait.until(expected_conditions.visibility_of_element_located(constants.PASS_TEXTFIELD))

        password.send_keys(credentials.password)

        login_button = wait.until(expected_conditions.element_to_be_clickable(constants.LOGIN_BUTTON))

        login_button.click()

        order_button = wait.until(expected_conditions.element_to_be_clickable(constants.PLACE_AN_ORDER_BUTTON))

        assert order_button.is_displayed()

        driver.quit()
