from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestOrder:
    @pytest.mark.parametrize("button_position, name, surname, address, metro, phone, date, rental_period, color, comment", [
        ("top", "Иван", "Петров", "ул. Ленина 1", "Черкизовская", "89001234567", "01.06.2026", "сутки", "чёрный жемчуг", "Позвонить за час"),
        ("bottom", "Мария", "Сидорова", "ул. Пушкина 10", "Бульвар Рокоссовского", "89221234567", "02.06.2026", "двое суток", "серая безысходность", "Домофон не работает"),
    ])
    def test_order_scooter(self, driver, button_position, name, surname, address, metro, phone, date, rental_period, color, comment):
        wait = WebDriverWait(driver, 15)
        
        try:
            cookie = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie.click()
        except:
            pass
        
        if button_position == "top":
            order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")))
            driver.execute_script("arguments[0].click();", order_button)
        else:
            order_buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]")
            driver.execute_script("arguments[0].click();", order_buttons[1])
        
        name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='* Имя']")))
        name_field.send_keys(name)
        
        surname_field = driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']")
        surname_field.send_keys(surname)
        
        address_field = driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        address_field.send_keys(address)
        
        metro_field = driver.find_element(By.XPATH, "//input[@placeholder='* Станция метро']")
        metro_field.click()
        metro_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{metro}']")))
        driver.execute_script("arguments[0].click();", metro_option)
        
        phone_field = driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        phone_field.send_keys(phone)
        
        next_button = driver.find_element(By.XPATH, "//button[text()='Далее']")
        driver.execute_script("arguments[0].click();", next_button)
        
        # Увеличиваем ожидание до 20 секунд
        wait = WebDriverWait(driver, 20)
        
        # Ждём появления поля "Когда привезти самокат"
        date_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='* Когда привезти самокат']")))
        date_field.send_keys(date)
        
        rental_field = driver.find_element(By.XPATH, "//div[text()='* Срок аренды']")
        driver.execute_script("arguments[0].click();", rental_field)
        
        rental_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{rental_period}']")))
        driver.execute_script("arguments[0].click();", rental_option)
        
        color_checkbox = driver.find_element(By.XPATH, f"//label[text()='{color}']")
        driver.execute_script("arguments[0].scrollIntoView();", color_checkbox)
        driver.execute_script("arguments[0].click();", color_checkbox)
        
        comment_field = driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']")
        comment_field.send_keys(comment)
        
        order_button_final = driver.find_element(By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
        driver.execute_script("arguments[0].click();", order_button_final)
        
        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']")))
        driver.execute_script("arguments[0].click();", confirm_button)
        
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")))
        assert success_message.is_displayed()