import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Кликнуть через JavaScript")
    def click_js(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст: {text}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текущую вкладку")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на вкладку по индексу")
    def switch_to_window(self, index=-1):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    @allure.step("Закрыть текущую вкладку")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Ожидать появления нового окна")
    def wait_for_new_window(self, expected_count=2):
        self.wait.until(EC.number_of_windows_to_be(expected_count))

    @allure.step("Кликнуть по пустому месту")
    def click_body(self):
        self.click(BasePageLocators.BODY)

    @allure.step("Прокрутить страницу вниз")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)