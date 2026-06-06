import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.test_data import OrderTestData


@allure.epic("Яндекс.Самокат")
@allure.feature("Оформление заказа")
class TestOrderPage:
    
    @allure.title("Позитивный сценарий заказа самоката")
    @pytest.mark.parametrize("order", OrderTestData.orders)
    def test_order_scooter(self, driver, order):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.accept_cookies()
        main_page.click_order_button("top")
        
        order_page.fill_name(order["name"])
        order_page.fill_surname(order["surname"])
        order_page.fill_address(order["address"])
        order_page.select_metro_station(order["metro"])
        order_page.fill_phone(order["phone"])
        order_page.click_next()
        
        order_page.fill_date(order["date"])
        order_page.select_rental_period(order["rental_period"])
        order_page.select_color(order["color"])
        order_page.fill_comment(order["comment"])
        
        order_page.click_order_button()
        order_page.confirm_order()
        
        assert order_page.is_order_successful(), "Заказ не оформлен"