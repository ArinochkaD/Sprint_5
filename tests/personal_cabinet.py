from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util import constants

# Тестируем переход в личный кабинет.
class TestPersonalCabinet:
    # Используем фикстуру authed_user (webdriver с авторизованным пользователем).
    def test_open_personal_cabinet(self, authed_user):
        wait = WebDriverWait(authed_user, 100)

        enter_button = wait.until(expected_conditions.element_to_be_clickable(constants.PERSONAL_CABINET_BUTTON))
        
        enter_button.click()

        save_button = wait.until(expected_conditions.element_to_be_clickable(constants.SAVE_BUTTON))

        assert save_button.is_displayed()
