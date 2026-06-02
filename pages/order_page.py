import allure
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    
    @allure.step("Заполнить поле Имя: {name}")
    def fill_name(self, name):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
    
    @allure.step("Заполнить поле Фамилия: {surname}")
    def fill_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
    
    @allure.step("Заполнить поле Адрес: {address}")
    def fill_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
    
    @allure.step("Заполнить поле Телефон: {phone}")
    def fill_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Нажать кнопку Далее")
    def click_next(self):
        self.click_js(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        # Кликаем по полю ввода метро
        self.click_js(OrderPageLocators.METRO_INPUT)
        time.sleep(2)  # Ждём появления выпадающего списка
        
        # Ищем и кликаем по нужной станции (универсальный поиск)
        try:
            station_locator = (By.XPATH, f"//button[contains(text(), '{station_name}')]")
            self.click_js(station_locator)
        except:
            # Альтернативный локатор
            station_locator = (By.XPATH, f"//div[contains(text(), '{station_name}')]")
            self.click_js(station_locator)
        time.sleep(0.5)
    
    # Методы для проверки ошибок
    def is_name_error_displayed(self):
        return self.find_element(OrderPageLocators.NAME_ERROR).is_displayed()
    
    def is_surname_error_displayed(self):
        return self.find_element(OrderPageLocators.SURNAME_ERROR).is_displayed()
    
    def is_address_error_displayed(self):
        return self.find_element(OrderPageLocators.ADDRESS_ERROR).is_displayed()
    
    def is_phone_error_displayed(self):
        return self.find_element(OrderPageLocators.PHONE_ERROR).is_displayed()
    
    def is_metro_error_displayed(self):
        return self.find_element(OrderPageLocators.METRO_ERROR).is_displayed()