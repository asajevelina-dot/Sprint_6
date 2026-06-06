from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    
    @staticmethod
    def metro_station(station_name):
        return (By.XPATH, f"//li//div[contains(text(), '{station_name}')]")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    MODAL_CONFIRM_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[contains(text(), 'Да')]")
    
    NAME_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректное имя')]")
    SURNAME_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректную фамилию')]")
    ADDRESS_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректный адрес')]")
    PHONE_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректный номер')]")