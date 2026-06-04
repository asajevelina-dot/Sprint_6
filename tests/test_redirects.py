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
        
        # Переходим на страницу заказа
        main_page.click_order_button("top")
        
        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        
        # Проверяем, что вернулись на главную страницу
        assert main_page.get_current_url() == Urls.MAIN_PAGE, "Не произошёл редирект на главную страницу"
    
    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса должна открыться страница Дзена в новом окне")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        # Запоминаем текущее окно
        original_window = main_page.get_current_window_handle()
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ожидаем появления нового окна
        main_page.wait_for_new_window(2)
        
        # Переключаемся на новое окно
        main_page.switch_to_window(-1)
        
        # Проверяем, что открылась страница Дзена
        current_url = main_page.get_current_url()
        assert "dzen.ru" in current_url or "yandex" in current_url, f"Открылась не страница Дзена, а {current_url}"
        
        # Закрываем новое окно и возвращаемся обратно
        main_page.close_current_window()
        main_page.switch_to_window(0)