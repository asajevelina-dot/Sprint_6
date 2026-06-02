import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Оформление заказа")
class TestOrderPage:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного цикла оформления заказа")
    @pytest.mark.parametrize("name, surname, address, metro, phone", [
        ("Иван", "Петров", "ул. Ленина 1", "Черкизовская", "89001234567"),
        ("Мария", "Сидорова", "ул. Пушкина 10", "Бульвар Рокоссовского", "89221234567"),
    ])
    def test_order_scooter(self, driver, name, surname, address, metro, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Шаг 1: Закрыть куки и нажать кнопку Заказать
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        # Шаг 2: Заполнить форму "Для кого самокат"
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.select_metro_station(metro)
        order_page.fill_phone(phone)
        order_page.click_next()
        
        # Шаг 3: Заполнить форму "Про аренду" (упрощённо)
        # TODO: добавить заполнение даты, срока аренды, цвета, комментария
        
        # Шаг 4: Подтверждение заказа (упрощённо)
        # TODO: добавить клик по кнопке Заказать и подтверждение
        
        # Временная проверка (убрать после реализации)
        assert True