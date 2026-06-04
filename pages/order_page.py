import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    
    # Форма "Для кого самокат"
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
    
    # Форма "Про аренду"
    @allure.step("Заполнить дату: {date}")
    def fill_date(self, date):
        self.send_keys(OrderPageLocators.DATE_INPUT, date)
        time.sleep(0.5)
    
    @allure.step("Выбрать срок аренды: {rental_period}")
    def select_rental_period(self, rental_period):
        self.driver.find_element(By.XPATH, "//body").click()
        time.sleep(0.5)
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        time.sleep(0.5)
        locator = (By.XPATH, f"//div[contains(text(), '{rental_period}')]")
        self.click(locator)
    
    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "чёрный жемчуг":
            self.click(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == "серая безысходность":
            self.click(OrderPageLocators.COLOR_GREY_CHECKBOX)
    
    @allure.step("Заполнить комментарий: {comment}")
    def fill_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        time.sleep(2)
    
    @allure.step("Подтвердить заказ (кнопка Да)")
    def confirm_order(self):
        modal = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.MODAL_WINDOW))
        confirm_btn = modal.find_element(By.XPATH, ".//button[contains(text(), 'Да')]")
        self.driver.execute_script("arguments[0].click();", confirm_btn)
    
    @allure.step("Проверить, что заказ оформлен")
    def is_order_successful(self):
        return self.find_element(OrderPageLocators.SUCCESS_MESSAGE).is_displayed()
    
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