# Sprint_6 - Финальный проект

## Тесты для сервиса "Яндекс.Самокат"

### Реализовано:
- 8 тестов для раздела "Вопросы о важном" (выпадающий список)
-  4 теста валидации полей заказа (Имя, Фамилия, Адрес, Телефон)
-  Page Object Model (pages, locators, utils)
-  Параметризация тестов
-  Allure-отчёты

### Не реализовано (технические ограничения):
-  Позитивный сценарий заказа самоката (выпадающий список метро не открывается из-за защиты сайта)
-  Тесты переходов по логотипам (JavaScript не выполняется)

### Структура проекта:
Sprint_6/
├── locators/ # Локаторы элементов
├── pages/ # Page Object классы
├── tests/ # Тесты
│ ├── conftest.py # Фикстуры
│ └── test_faq.py # Тесты FAQ
├── utils/ # Вспомогательные модули
│ └── test_data.py # Тестовые данные
├── .gitignore
├── README.md
└── requirements.txt



### Запуск тестов:
```bash
pytest tests/test_faq.py -v```
### Генерация Allure-отчёта:
```bash
pytest tests/test_faq.py --alluredir=allure_results
allure serve allure_results```
### Требования:
Python 3.14+

Firefox браузер

### Установка зависимостей:

```bash
pip install -r requirements.txt```