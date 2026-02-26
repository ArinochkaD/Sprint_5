import pytest
import sys
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.constants import Urls
from util.constants import CredentialsData
from util.locators import GeneralLocators
from util.locators import SignInLocators

# Добавляем текущую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def authed_user(driver):
    credentials = CredentialsData.get_test_credentials()
    driver.get(Urls.BASE_URL)
    wait = WebDriverWait(driver, 10)
    enter_button = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
    enter_button.click()
    email = wait.until(expected_conditions.visibility_of_element_located(SignInLocators.EMAIL_TEXTFIELD))
    email.send_keys(credentials.email)
    password = wait.until(expected_conditions.visibility_of_element_located(SignInLocators.PASS_TEXTFIELD))
    password.send_keys(credentials.password)
    login_button = wait.until(expected_conditions.element_to_be_clickable(SignInLocators.LOGIN_BUTTON))
    login_button.click()
    return driver
