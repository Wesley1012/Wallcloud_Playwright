# Wallcloud UI Automation

[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat&logo=Playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

Automated test suite for Wallcloud web application using Playwright and Pytest.

📁 Project Structure
<pre>
Wallcloud_PW/
├── pages/                 # Page Object Model (POM)
│   ├── basepage.py       # Base page class
│   ├── authpage.py       # Authentication page
│   └── mainpage.py       # Main page
├── tests/                # Test scenarios
│   ├── test_login_page.py
│   ├── test_signup_page.py
│   └── test_main_page.py
├── conftest.py           # Pytest fixtures
├── locators.py           # Element locators
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Python dependencies
└── .gitignore
</pre>

Installation
Clone the repository:

git clone https://github.com/Wesley1012/Walldoud_Playwright.git
cd Walldoud_PW

Create virtual environment:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac

.venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt
playwright install

Running Tests

python3 -m pytest -v tests/
