# Sprint_6 - Финальный проект

## Тесты для сервиса "Яндекс.Самокат"

### Реализовано:
- ✅ 8 тестов для раздела "Вопросы о важном" (выпадающий список)
- ✅ 2 теста позитивного сценария заказа самоката (с разными данными)
- ✅ 4 теста валидации полей заказа
- ✅ 2 теста переходов по логотипам (Самокат → главная, Яндекс → Дзен)
- ✅ Page Object Model (pages, locators, utils)
- ✅ Параметризация тестов
- ✅ Allure-отчёты

### Структура проекта:
Sprint_6/
├── locators/ # Локаторы элементов
├── pages/ # Page Object классы
├── tests/ # Тесты
│ ├── conftest.py # Фикстуры
│ ├── test_faq.py # Тесты FAQ
│ ├── test_order_page.py # Тесты заказа
│ ├── test_order_validation.py # Тесты валидации
│ └── test_redirects.py # Тесты логотипов
├── utils/ # Вспомогательные модули
│ └── test_data.py # Тестовые данные
├── .gitignore
├── README.md
└── requirements.txt

text

### Запуск всех тестов:
```bash
pytest tests/ -v
Запуск отдельных тестов:
bash
# Тесты FAQ
pytest tests/test_faq.py -v

# Тесты заказа
pytest tests/test_order_page.py -v

# Тесты валидации
pytest tests/test_order_validation.py -v

# Тесты логотипов
pytest tests/test_redirects.py -v
Генерация Allure-отчёта:
bash
pytest tests/ --alluredir=allure_results
allure serve allure_results
Требования:
Python 3.14+

Firefox браузер

Установка зависимостей:
bash
pip install -r requirements.txt