from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=True,
        # slow_mo=100,  # Замедление в ms для визуализации
        args=["--no-sandbox", "--disable-dev-shm-usage"]
    )

    yield browser

    browser.close()
    playwright.stop()

@pytest.fixture(scope='function')
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )

    yield context

    context.close()

@pytest.fixture(scope='function')
def page(context):
    page = context.new_page()

    yield page
