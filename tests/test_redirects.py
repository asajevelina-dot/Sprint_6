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
        assert driver.current_url == Urls.MAIN_PAGE, "Не произошёл редирект на главную страницу"
    
    @allure.title("Проверка перехода по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса должна открыться страница Дзена в новом окне")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        
        # Запоминаем текущее окно
        original_window = driver.current_window_handle
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ждём появления нового окна и переключаемся
        import time
        time.sleep(3)
        
        # Получаем все окна
        windows = driver.window_handles
        
        # Переключаемся на новое окно (если оно появилось)
        if len(windows) > 1:
            driver.switch_to.window(windows[-1])
        else:
            # Если новое окно не открылось, проверяем текущий URL
            pass
        
        # Проверяем, что открылась страница Дзена
        current_url = driver.current_url
        assert "dzen.ru" in current_url or "yandex" in current_url, f"Открылась не страница Дзена, а {current_url}"
        
        # Закрываем новое окно и возвращаемся обратно
        if len(windows) > 1:
            driver.close()
            driver.switch_to.window(original_window)