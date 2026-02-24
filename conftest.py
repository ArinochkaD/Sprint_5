import pytest
import sys
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util import constants

# Добавляем текущую директорию в sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def authed_user():
    credentials = constants.get_test_credentials()

    driver = webdriver.Chrome()
    driver.get(constants.STELLAR_BURGERS)

    wait = WebDriverWait(driver, 100)

    enter_button = wait.until(expected_conditions.element_to_be_clickable(constants.PERSONAL_CABINET_BUTTON))
        
    enter_button.click()

    email = wait.until(expected_conditions.visibility_of_element_located(constants.EMAIL_TEXTFIELD))

    email.send_keys(credentials.email)

    password = wait.until(expected_conditions.visibility_of_element_located(constants.PASS_TEXTFIELD))

    password.send_keys(credentials.password)

    login_button = wait.until(expected_conditions.element_to_be_clickable(constants.LOGIN_BUTTON))

    login_button.click()

    yield driver

    driver.quit()
