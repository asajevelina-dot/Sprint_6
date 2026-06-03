import allure
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
        self.click(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Выбрать станцию метро: {station_name}")
    def select_metro_station(self, station_name):
        self.click(OrderPageLocators.METRO_INPUT)
        self.click(OrderPageLocators.metro_station(station_name))
    
    # Методы для проверки ошибок валидации
    @allure.step("Проверить ошибку для поля Имя")
    def is_name_error_displayed(self):
        return self.find_element(OrderPageLocators.NAME_ERROR).is_displayed()
    
    @allure.step("Проверить ошибку для поля Фамилия")
    def is_surname_error_displayed(self):
        return self.find_element(OrderPageLocators.SURNAME_ERROR).is_displayed()
    
    @allure.step("Проверить ошибку для поля Адрес")
    def is_address_error_displayed(self):
        return self.find_element(OrderPageLocators.ADDRESS_ERROR).is_displayed()
    
    @allure.step("Проверить ошибку для поля Телефон")
    def is_phone_error_displayed(self):
        return self.find_element(OrderPageLocators.PHONE_ERROR).is_displayed()