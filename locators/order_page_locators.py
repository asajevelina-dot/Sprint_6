from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Поля ввода
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    
    # Кнопки
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    
    # Станции метро (универсальный поиск)
    @staticmethod
    def metro_station(station_name):
        return (By.XPATH, f"//li//div[contains(text(), '{station_name}')]")
    
    # Сообщения об ошибках
    NAME_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректное имя')]")
    SURNAME_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректную фамилию')]")
    ADDRESS_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректный адрес')]")
    PHONE_ERROR = (By.XPATH, "//div[contains(@class, 'Input_ErrorMessage') and contains(text(), 'Введите корректный номер')]")