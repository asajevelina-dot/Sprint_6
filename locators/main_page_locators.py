from selenium.webdriver.common.by import By

class MainPageLocators:
    # Существующие локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(text(), 'Заказать')]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(text(), 'Заказать')]")
    
    QUESTION = (By.ID, "accordion__heading-{}")
    ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
    
    # НОВЫЕ ЛОКАТОРЫ ДЛЯ ЛОГОТИПОВ
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")