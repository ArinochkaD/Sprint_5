import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util.credentials_generator import CredentialsGenerator
from util.constants import Urls
from util.locators import GeneralLocators
from util.locators import SignInLocators
from util.locators import RegistrationLocators

class TestsRegistration:
    def test_successful_registration(self, driver):
        credentials = CredentialsGenerator.generate()
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 10)
        personal_cabinet = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
        personal_cabinet.click()
        registration = wait.until(expected_conditions.element_to_be_clickable(SignInLocators.REGISRATION_TEXT))
        registration.click()
        name = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_TEXTFIELD))
        name.send_keys(credentials.name)
        email = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_TEXTFIELD))
        email.send_keys(credentials.email)
        password = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASS_TEXTFIELD))
        password.send_keys(credentials.password)
        registaration_button = wait.until(expected_conditions.element_to_be_clickable(RegistrationLocators.REGISRATION_BUTTON))
        registaration_button.click()
        login_button = wait.until(expected_conditions.element_to_be_clickable(SignInLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    @pytest.mark.parametrize('wrong_pass', ['0', '12', '123', '1234', '12345'])
    def test_unsuccessful_registration(self, wrong_pass, driver):
        credentials = CredentialsGenerator.generate()
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 10)
        personal_cabinet = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
        personal_cabinet.click()
        registration = wait.until(expected_conditions.element_to_be_clickable(SignInLocators.REGISRATION_TEXT))
        registration.click()
        name = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.NAME_TEXTFIELD))
        name.send_keys(credentials.name)
        email = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.EMAIL_TEXTFIELD))
        email.send_keys(credentials.email)
        password = wait.until(expected_conditions.visibility_of_element_located(RegistrationLocators.PASS_TEXTFIELD))
        password.send_keys(wrong_pass)
        registaration_button = wait.until(expected_conditions.element_to_be_clickable(RegistrationLocators.REGISRATION_BUTTON))
        registaration_button.click()
        error_text = wait.until(expected_conditions.element_to_be_clickable(RegistrationLocators.ERROR_REGISTRATION_PASSWORD))
        assert error_text.is_displayed()
