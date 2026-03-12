from playwright.sync_api import Page, sync_playwright
import datetime, os
import pytest



@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(
        headless=False,
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
        ignore_https_errors=True,
        extra_http_headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", # Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
    )

    yield context

    context.close()

@pytest.fixture(scope='function')
def page(context):
    page = context.new_page()

    yield page


os.makedirs("screenshots", exist_ok=True)


@pytest.fixture
def auto_screenshot(page: Page, request):
    """Фикстура для автоскриншотов"""
    yield page

    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        screenshot_path = f"screenshots/{test_name}_{timestamp}.png"

        try:
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"\n📸 Скриншот падения: {screenshot_path}")
        except Exception as e:
            print(f"\n❌ Не удалось создать скриншот: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     if report.when == "call" and report.failed:
#         if "page" in item.funcargs:
#             page = item.funcargs["page"]
#             allure.attach(
#                 page.screenshot(),
#                 name="падение теста",
#                 attachment_type=allure.attachment_type.PNG
#             )