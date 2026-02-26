from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.locators import GeneralLocators
from util.locators import PersonalCabinetLocators
from util.locators import SignInLocators

# Тестируем выход из аккаунта в личном кабинете.
class TestLogout:
    # Используем фикстуру для готовой авторизации.
    def test_logout(self, authed_user):
        wait = WebDriverWait(authed_user, 10)
        personal_cabinet_button = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
        personal_cabinet_button.click()
        logout_button = wait.until(expected_conditions.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BUTTON))
        logout_button.click()
        # Ищем форму авторизации.
        auth_form = wait.until(expected_conditions.visibility_of_element_located(SignInLocators.AUTH_FORM))
        assert auth_form.is_displayed()
