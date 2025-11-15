from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, url=None):
        self.url = url
        self.page = page

    def navigate(self, path: str = ""):
        full_url = f"{self.url}{path}"
        self.page.goto(full_url, timeout=60000, wait_until="domcontentloaded")
        return self

    def find_locator(self, selector, timeout= 30000):
        locator = self.page.locator(selector)
        locator.wait_for(state="attached", timeout=timeout)
        return locator

    def click(self, selector, timeout=30000):
        self.page.locator(selector).click(timeout=timeout, force=True)
        return self

    def fill(self, selector, text, timeout=30000):
        self.page.fill(selector, text, timeout=timeout)
        return self

    def get_text(self, selector) -> str:
        return self.page.text_content(selector)

    # Получить только внутренний текст элемента (без потомков)
    def get_inner_text(self, selector, timeout= 30000) -> str:
        return self.find_locator(selector, timeout).inner_text()

    def get_attribute(self, selector, attribute) -> str:
        return self.page.get_attribute(selector, attribute)

    def get_current_url(self) -> str:
        return self.page.url

    def is_element_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, state="visible", timeout=timeout)
            return True
        except:
            return False

    def is_element_present(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.wait_for_selector(selector, state="attached", timeout=timeout)
            return True
        except:
            return False