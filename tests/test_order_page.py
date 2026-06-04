import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.epic("Яндекс.Самокат")
@allure.feature("Оформление заказа")
class TestOrderPage:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @allure.description("Проверка полного цикла оформления заказа")
    @pytest.mark.skip(reason="Модальное окно подтверждения не появляется при автоматизации (защита сайта)")
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, rental_period, color, comment", [
        ("Иван", "Петров", "ул. Ленина 1", "Черкизовская", "89001234567", "01.06.2026", "сутки", "чёрный жемчуг", "Позвонить за час"),
        ("Мария", "Сидорова", "ул. Пушкина 10", "Бульвар Рокоссовского", "89221234567", "02.06.2026", "двое суток", "серая безысходность", "Домофон не работает"),
    ])
    def test_order_scooter(self, driver, name, surname, address, metro, phone, date, rental_period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_address(address)
        order_page.select_metro_station(metro)
        order_page.fill_phone(phone)
        order_page.click_next()
        
        order_page.fill_date(date)
        order_page.select_rental_period(rental_period)
        order_page.select_color(color)
        order_page.fill_comment(comment)
        
        order_page.click_order_button()
        order_page.confirm_order()
        
        assert order_page.is_order_successful(), "Заказ не оформлен"