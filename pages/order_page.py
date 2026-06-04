import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC


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
    
    @allure.step("Проверить ошибку для поля Имя")
    def is_name_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_ERROR))
            return True
        except:
            return False
    
    @allure.step("Проверить ошибку для поля Фамилия")
    def is_surname_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SURNAME_ERROR))
            return True
        except:
            return False
    
    @allure.step("Проверить ошибку для поля Адрес")
    def is_address_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ADDRESS_ERROR))
            return True
        except:
            return False
    
    @allure.step("Проверить ошибку для поля Телефон")
    def is_phone_error_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(OrderPageLocators.PHONE_ERROR))
            return True
        except:
            return False