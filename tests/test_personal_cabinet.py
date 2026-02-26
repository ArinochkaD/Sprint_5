from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.locators import GeneralLocators
from util.locators import PersonalCabinetLocators

# Тестируем переход в личный кабинет.
class TestPersonalCabinet:
    # Используем фикстуру authed_user (webdriver с авторизованным пользователем).
    def test_open_personal_cabinet(self, authed_user):
        wait = WebDriverWait(authed_user, 10)
        enter_button = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
        enter_button.click()
        assert wait.until(expected_conditions.element_to_be_clickable(PersonalCabinetLocators.SAVE_BUTTON)).is_displayed()
