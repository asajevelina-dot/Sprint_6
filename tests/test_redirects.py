import allure
import pytest
from pages.main_page import MainPage
from utils.test_data import Urls


@allure.epic("Яндекс.Самокат")
@allure.feature("Переходы по логотипам")
class TestRedirects:
    
    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.description("При клике на логотип Самоката должен происходить редирект на главную страницу")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        main_page.click_order_button("top")
        main_page.click_scooter_logo()
        
        assert driver.current_url == Urls.MAIN_PAGE, "Не произошёл редирект на главную страницу"
    
    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса должна открыться страница Дзена в новом окне")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        original_window = driver.current_window_handle
        main_page.click_yandex_logo()
        
        main_page.wait_for_new_window(2)
        main_page.switch_to_window(-1)
        
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex" in current_url, f"Открылась не страница Дзена, а {current_url}"
        
        main_page.close_current_window()
        main_page.switch_to_window(0)