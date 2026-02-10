import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util.credentials_generator import generate_credentials
from util import constants

class TestsRegistration:
    def test_successful_registration(self):
        credentials = generate_credentials()

        driver = webdriver.Chrome()
        driver.get(constants.STELLAR_BURGERS)

        wait = WebDriverWait(driver, 100)

        personal_cabinet = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        
        personal_cabinet.click()

        registration = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))

        registration.click()

        name = wait.until(expected_conditions.visibility_of_element_located(constants.NAME_TEXTFIELD))

        name.send_keys(credentials.name)

        email = wait.until(expected_conditions.visibility_of_element_located(constants.EMAIL_TEXTFIELD))

        email.send_keys(credentials.email)

        password = wait.until(expected_conditions.visibility_of_element_located(constants.PASS_TEXTFIELD))

        password.send_keys(credentials.password)

        registaration_button = wait.until(expected_conditions.element_to_be_clickable(constants.REGISRATION_BUTTON))

        registaration_button.click()

        login_button = wait.until(expected_conditions.element_to_be_clickable(constants.LOGIN_BUTTON))

        assert login_button.is_displayed()

        driver.quit()

    @pytest.mark.parametrize('wrong_pass', ['0', '12', '123', '1234', '12345'])
    def test_unsuccessful_registration(self, wrong_pass):
        credentials = generate_credentials()

        driver = webdriver.Chrome()
        driver.get(constants.STELLAR_BURGERS)

        wait = WebDriverWait(driver, 100)

        personal_cabinet = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
        
        personal_cabinet.click()

        registration = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться")))

        registration.click()

        name = wait.until(expected_conditions.visibility_of_element_located(constants.NAME_TEXTFIELD))

        name.send_keys(credentials.name)

        email = wait.until(expected_conditions.visibility_of_element_located(constants.EMAIL_TEXTFIELD))

        email.send_keys(credentials.email)

        password = wait.until(expected_conditions.visibility_of_element_located(constants.PASS_TEXTFIELD))

        password.send_keys(wrong_pass)

        registaration_button = wait.until(expected_conditions.element_to_be_clickable(constants.REGISRATION_BUTTON))

        registaration_button.click()

        error_text = wait.until(expected_conditions.element_to_be_clickable(constants.ERROR_REGISTRATION_PASSWORD))

        assert error_text.is_displayed()

        driver.quit()
