from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util import constants

# Тестируем выход из аккаунта в личном кабинете.
class TestLogout:
    # Используем фикстуру для готовой авторизации.
    def test_logout(self, authed_user):
        wait = WebDriverWait(authed_user, 100)

        personal_cabinet_button = wait.until(expected_conditions.element_to_be_clickable(constants.PERSONAL_CABINET_BUTTON))

        personal_cabinet_button.click()

        logout_button = wait.until(expected_conditions.element_to_be_clickable(constants.LOGOUT_BUTTON))

        logout_button.click()

        # Ищем форму авторизации.
        auth_form = wait.until(expected_conditions.visibility_of_element_located(constants.AUTH_FORM))

        assert auth_form.is_displayed()
