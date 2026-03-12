import time

from pages.basepage import BasePage
from locators import MainPageLocators as mpl
import allure

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://wallscloud.net/en'

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.navigate('')
        return self


    def select_menu_and_item(self, menu_name, item_name, item_selector):
        menu_selector = mpl.HEADER[menu_name]
        dropdown_selector = mpl.MENU_DROPDOWNS[menu_name]

        header = self.page.locator("#header")

        with allure.step(f"Открыть меню {menu_name}"):
            # Принудительно закрываем любое открытое меню
            header.click(position={"x": 10, "y": 10})
            self.page.wait_for_timeout(300)

            menu = header.locator(menu_selector)
            menu.wait_for(state="visible", timeout=20000)
            menu.click()

            dropdown_menu = self.page.locator(dropdown_selector)
            dropdown_menu.wait_for(state="visible", timeout=20000)

            self.page.wait_for_timeout(200)

        with allure.step(f"Выбрать {item_name}"):
            menu_item = dropdown_menu.locator(item_selector)
            menu_item.wait_for(state="visible", timeout=20000)
            menu_item.click()

        return self



    def change_language(self, lang_selector):
        current_lang = self.get_inner_text(mpl.HEADER['Language Button'])
        target_lang = lang_selector.split("'")[1]  # Извлекаем 'en', 'ru', 'ua' из селектора

        if current_lang == target_lang:
            return self

        with allure.step("Нажать кнопку выбора языка"):
            self.click_selector(mpl.HEADER['Language Button'])

        with allure.step(f"Выбрать язык {target_lang}"):
            self.click_selector(lang_selector)
        return self

    @allure.step("Ввести текст в поле поиска")
    def fill_search_text(self, text):
        self.fill(mpl.HEADER['Search Bar'], text)
        return self

    @allure.step("Выполнить поиск")
    def search_button_click(self):
        self.click_selector(mpl.HEADER['Search Button'])
        return self
