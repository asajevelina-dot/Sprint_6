import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    
    @allure.step("Закрыть куки")
    def accept_cookies(self):
        try:
            self.click_js(MainPageLocators.COOKIE_BUTTON)
        except:
            pass

    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self, position="top"):
        if position == "top":
            self.click_js(MainPageLocators.ORDER_BUTTON_TOP)
        else:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_js(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Открыть вопрос {index}")
    def open_question(self, index):
        locator = (MainPageLocators.QUESTION[0], MainPageLocators.QUESTION[1].format(index))
        question = self.wait.until(EC.presence_of_element_located(locator))
        self.scroll_to_element(question)
        self.click_js(locator)

    @allure.step("Получить текст ответа на вопрос {index}")
    def get_answer_text(self, index):
        locator = (MainPageLocators.ANSWER[0], MainPageLocators.ANSWER[1].format(index))
        answer = self.wait.until(EC.visibility_of_element_located(locator))
        return answer.text
    
    # НОВЫЕ МЕТОДЫ ДЛЯ ЛОГОТИПОВ
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_js(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_js(MainPageLocators.YANDEX_LOGO)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
    
    @allure.step("Закрыть текущее окно и вернуться обратно")
    def close_current_window_and_switch_back(self):
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])