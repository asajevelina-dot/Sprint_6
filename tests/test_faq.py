from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class TestFAQ:
    @pytest.mark.parametrize("index, expected_text", [
        (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (4, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (5, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (6, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
    ])
    def test_faq_question(self, driver, index, expected_text):
        wait = WebDriverWait(driver, 10)
        
        try:
            cookie = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie.click()
        except:
            pass
        
        question = wait.until(EC.presence_of_element_located((By.ID, f"accordion__heading-{index}")))
        driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()
        
        answer = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@id='accordion__panel-{index}']/p")))
        assert answer.text == expected_text
