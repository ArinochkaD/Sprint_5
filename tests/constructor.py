import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from util import constants

# Тестируем переход из личного кабинета в конструктор.
class TestConstructor:
    # Используем фикстуру authed_user (webdriver с авторизованным пользователем).
    # И используем параметризацию для проверки сразу двух кейсов перехода на экран
    # "Конструктор".
    @pytest.mark.parametrize('constructor_element', [
        constants.CONSTRUCTOR_BUTTON,
        constants.LOGO_BUTTON,
    ])
    def test_open_constructor(self, authed_user, constructor_element):
        wait = WebDriverWait(authed_user, 100)

        enter_button = wait.until(expected_conditions.element_to_be_clickable(constants.PERSONAL_CABINET_BUTTON))

        enter_button.click()

        construction_button = wait.until(expected_conditions.element_to_be_clickable(constructor_element))

        construction_button.click()

        # Ищем кнопку "Оформить заказ" на экране "Конструктор".
        order_button = wait.until(expected_conditions.element_to_be_clickable(constants.PLACE_AN_ORDER_BUTTON))

        assert order_button.is_displayed()
