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
            self.scroll_to_bottom()
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
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_js(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_js(MainPageLocators.YANDEX_LOGO)