import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик через JavaScript: {locator}")
    def click_js(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Обычный клик: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст: {text} в поле {locator}")
    def send_keys(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)

    @allure.step("Прокрутить к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Прокрутить страницу вниз")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить текущую вкладку")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Получить все вкладки")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на вкладку по индексу")
    def switch_to_window(self, index=-1):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    @allure.step("Закрыть текущую вкладку")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text