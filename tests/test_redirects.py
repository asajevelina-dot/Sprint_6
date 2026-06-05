import allure
import pytest
from pages.main_page import MainPage
from utils.test_data import Urls


@allure.epic("Яндекс.Самокат")
@allure.feature("Переходы по логотипам")
class TestRedirects:
    
    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        main_page.click_order_button("top")
        main_page.click_scooter_logo()
        
        assert main_page.get_current_url() == Urls.MAIN_PAGE
    
    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        original_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        
        main_page.wait_for_new_window(2)
        main_page.switch_to_window(-1)
        
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex" in current_url
        
        main_page.close_current_window()
        main_page.switch_to_window(0)