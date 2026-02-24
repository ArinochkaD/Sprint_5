from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util import constants

# Тестируем переключение вкладок.
class TestChapterTransition:
    def test_chapter_transition(self):
        driver = webdriver.Chrome()
        driver.get(constants.STELLAR_BURGERS)

        wait = WebDriverWait(driver, 100)

        sauce_section_button = wait.until(expected_conditions.element_to_be_clickable(constants.SAUCE_SECTION_BUTTON))

        sauce_section_button.click()

        assert sauce_section_button.is_enabled()

        fillings_section_button = wait.until(expected_conditions.element_to_be_clickable(constants.FILLINGS_SECTION_BUTTON))

        fillings_section_button.click()

        assert fillings_section_button.is_enabled()

        bulki_section_button = wait.until(expected_conditions.element_to_be_clickable(constants.BULKI_SECTION_BUTTON))

        bulki_section_button.click()

        assert bulki_section_button.is_enabled()

        driver.quit()
