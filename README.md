# Wallcloud UI Automation

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=Playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org/)
[![Allure](https://img.shields.io/badge/Allure-DE5C43?style=flat&logo=allure&logoColor=white)](https://allurereport.org/)

Автоматические тесты для [wallscloud.net](https://wallscloud.net).  
Проверяем навигацию, поиск, регистрацию и авторизацию, чтобы сайт не ломался после каждого релиза.

## Возможности
- ! Page Object Model — чистая архитектура и переиспользование кода
- ! Параметризованные тесты — покрытие множества сценариев
- ! Allure отчёты — красивые и информативные отчёты с шагами, скриншотами и вложениями

## Структура проекта

Walldoud_PW/
├── pages/                 # Page Object Model — наши страницы
│   ├── basepage.py        # Базовая страница с общими методами
│   ├── authpage.py        # Всё про логин и регистрацию
│   └── mainpage.py        # Главная страница и менюшки
├── tests/                 # Сами тесты
│   ├── test_login_page.py
│   ├── test_signup_page.py
│   └── test_main_page.py
├── conftest.py            # Фикстуры для pytest
├── locators.py            # Селекторы в одном месте (чтобы не копаться по файлам)
├── pytest.ini             # Конфиг pytest
├── requirements.txt       # Что нужно поставить
└── .gitignore


## Установка

# Клонировать репозиторий:

git clone https://github.com/Wesley1012/Walldoud_Playwright.git
cd Walldoud_PW


# Создать виртуальное окружение:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac

.venv\Scripts\activate     # Windows


# Установить зависимости:

pip install -r requirements.txt
playwright install

sudo pacman -S jdk11-openjdk # Arch linux
sudo pacman -S allure 

brew install openjdk@11 # macOS
brew install allure 

winget install Microsoft.OpenJDK.11 # Windows (через winget)
scoop install allure # Windows (scoop)

# Запуск тестов

pytest

# Запуск с генерацией Allure отчёта(addopts уже прописан см. pytest.ini)

pytest --alluredir=allure-results
allure serve allure-results # или npx allure serve allure-results в моём случае

## Тестовые сценарии

# Главная страница (test_main_page.py)
- Навигация по меню категорий (33 категории)
- Выбор разрешений экрана (45+ разрешений)
- Поиск по цвету (16 цветов)
- Поиск по тексту
- Переключение языков (EN/RU/UA)
- Проверка меню "Топ" и "Ещё"

# Авторизация (test_login_page.py)
- Вход с валидными данными
- Проверка ошибок при невалидных данных
- Проверка ссылок "Забыли пароль?" и "Нет аккаунта?"
- Работа чекбокса "Запомнить меня"

# Регистрация (test_signup_page.py)
- Валидация полей формы
- Проверка капчи
- Сообщения об ошибках

📄 License
MIT License — free use and distribution. See LICENSE file for details.

