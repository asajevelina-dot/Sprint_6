import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Валидация полей заказа")
class TestOrderValidation:
    
    @allure.title("Проверка валидации поля Имя")
    @pytest.mark.parametrize("invalid_name", [
        pytest.param("", id="пустое поле"),
        pytest.param("123", id="цифры"),
        pytest.param("@#$", id="спецсимволы"),
    ])
    def test_name_validation(self, driver, invalid_name):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_name(invalid_name)
        order_page.click_next()
        
        assert order_page.is_name_error_displayed()
    
    @allure.title("Проверка валидации поля Фамилия")
    @pytest.mark.parametrize("invalid_surname", [
        pytest.param("", id="пустое поле"),
        pytest.param("123", id="цифры"),
        pytest.param("@#$", id="спецсимволы"),
    ])
    def test_surname_validation(self, driver, invalid_surname):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_surname(invalid_surname)
        order_page.click_next()
        
        assert order_page.is_surname_error_displayed()
    
    @allure.title("Проверка валидации поля Адрес")
    def test_address_validation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_address("")
        order_page.click_next()
        
        # Тест падает, если ошибка не появляется — это ожидаемое поведение
        assert order_page.is_address_error_displayed()
    
    @allure.title("Проверка валидации поля Телефон")
    @pytest.mark.parametrize("invalid_phone", [
        pytest.param("", id="пустое поле"),
        pytest.param("123", id="слишком короткий"),
        pytest.param("abc", id="буквы"),
        pytest.param("8900", id="неполный номер"),
    ])
    def test_phone_validation(self, driver, invalid_phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_phone(invalid_phone)
        order_page.click_next()
        
        assert order_page.is_phone_error_displayed()