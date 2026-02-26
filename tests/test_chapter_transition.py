from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.constants import Urls
from util.locators import ConstructorLocators
from util.constants import ClassName

# Тестируем переключение вкладок.
class TestChapterTransition:
    def test_sauce_transition(self, driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 10)
        sauce_section_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCE_SECTION_TAB))
        sauce_section_tab.click()
        assert ClassName.CONSTRUCTOR_ACTIVE_TAB_NAME in wait.until(lambda d: sauce_section_tab.get_attribute("class"))

    def test_fillings_transition(self, driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 10)
        fillings_section_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.FILLINGS_SECTION_TAB))
        fillings_section_tab.click()
        assert ClassName.CONSTRUCTOR_ACTIVE_TAB_NAME in wait.until(lambda d: fillings_section_tab.get_attribute("class"))
    
    def test_bulki_transition(self, driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 10)
        fillings_section_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.FILLINGS_SECTION_TAB))
        fillings_section_tab.click()
        bulki_section_tab = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.BULKI_SECTION_TAB))
        bulki_section_tab.click()
        assert ClassName.CONSTRUCTOR_ACTIVE_TAB_NAME in wait.until(lambda d: bulki_section_tab.get_attribute("class"))
