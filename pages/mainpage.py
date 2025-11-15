from pages.basepage import BasePage
from locators import MainPageLocators as mpl

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://wallscloud.net/en'
        # page.goto(self.url, timeout=60000, wait_until="domcontentloaded")

    def open_main_page(self):
        self.navigate('')
        return self

    def select_menu_and_item(self, menu_selector, item_selector, retries=3):
        for i in range(retries):
            try:
                self.page.locator(menu_selector).click()
                self.page.locator(item_selector).click(timeout=10000)
                return self
            except:
                if i == retries - 1:
                    raise

    def change_language(self, lang_selector):
        current_lang = self.get_inner_text(mpl.HEADER['Language Button'])
        target_lang = lang_selector.split("'")[1]  # Извлекаем 'en', 'ru', 'ua' из селектора

        if current_lang == target_lang:
            return self

        self.page.click(mpl.HEADER['Language Button'])
        self.page.wait_for_selector(lang_selector, state='visible', timeout=30000)
        self.page.click(lang_selector, force=True)
        return self
