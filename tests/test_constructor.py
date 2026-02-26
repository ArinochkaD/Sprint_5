import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from util.locators import GeneralLocators
from util.locators import ConstructorLocators

# Тестируем переход из личного кабинета в конструктор.
class TestConstructor:
    # Используем фикстуру authed_user (webdriver с авторизованным пользователем).
    # И используем параметризацию для проверки сразу двух кейсов перехода на экран
    # "Конструктор".
    @pytest.mark.parametrize('constructor_element', [
        GeneralLocators.CONSTRUCTOR_BUTTON,
        GeneralLocators.LOGO_BUTTON,
    ])
    def test_open_constructor(self, authed_user, constructor_element):
        wait = WebDriverWait(authed_user, 10)
        enter_button = wait.until(expected_conditions.element_to_be_clickable(GeneralLocators.PERSONAL_CABINET_BUTTON))
        enter_button.click()
        construction_button = wait.until(expected_conditions.element_to_be_clickable(constructor_element))
        construction_button.click()
        # Ищем кнопку "Оформить заказ" на экране "Конструктор".
        order_button = wait.until(expected_conditions.element_to_be_clickable(ConstructorLocators.PLACE_AN_ORDER_BUTTON))
        assert order_button.is_displayed()
