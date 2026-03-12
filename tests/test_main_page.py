from pages.mainpage import MainPage
from locators import MainPageLocators as mpl
from faker import Faker
import allure
from allure_commons.types import Severity
import pytest


@allure.epic("Сайт выбора обоев для рабочего стола")
@allure.feature("Главная страница")
@allure.link("https://wallscloud.net", name="Сайт")
@allure.severity(allure.severity_level.NORMAL)
class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, page, auto_screenshot):
        self.page = MainPage(page)
        self.page.open_main_page()


    @allure.title("Пункт {categori_name} из меню категорий")
    @allure.severity(Severity.CRITICAL)
    @allure.tag("smoke", "categories", "navigation")
    @allure.description("""
        Проверка перехода в категорию обоев.
        Ожидается редирект на страницу категории с правильным URL.
    """)
    @pytest.mark.parametrize("categori_name, categori_item",
                             mpl.CATEGORIES.items(),
                             ids=tuple(mpl.CATEGORIES.keys()))
    def test_categories_items(self, categori_name, categori_item):
        self.page.select_menu_and_item('Categories List',
                                       categori_name,
                                       categori_item)
        with allure.step(f'Проверить переадресацию на страницу {categori_name}'):
            assert self.page.get_current_url() == f"https://wallscloud.net/en/category/{categori_name.lower()}"


    @allure.title("Пункт {resolution_name} из меню разрешений")
    @pytest.mark.parametrize("resolution_name, resolution_item",
                             mpl.RESOLUTIONS.items(),
                             ids=mpl.RESOLUTION_IDS)
    def test_resolution_items(self, resolution_name, resolution_item):
        self.page.select_menu_and_item('Resolutions List',
                                       resolution_name,
                                       resolution_item)
        with allure.step(f'Проверить переадресацию на страницу {resolution_name}'):
            assert self.page.get_current_url() == f'https://wallscloud.net/en/resolution/{resolution_name.lower()}'


    @allure.title("Пункт {top_name} из меню ТОПа")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("top_name, top_item",
                             mpl.TOP_LIST.items(),
                             ids=tuple(mpl.TOP_LIST.keys()))
    def test_top_items(self, top_name, top_item):
        self.page.select_menu_and_item('Top List',
                                       top_name,
                                       top_item)
        with allure.step(f'Проверить переадресацию на страницу {top_name}'):
            assert self.page.get_current_url() == f'https://wallscloud.net/en/wallpapers/{top_name.lower()}'


    @allure.title("Пункт {more_name} из меню 'Ещё'")
    @pytest.mark.parametrize("more_name, more_item",
                             mpl.MORE_LIST.items(),
                             ids=tuple(mpl.MORE_LIST.keys()))
    def test_more_items(self, more_name, more_item):
        self.page.select_menu_and_item('More List',
                                       more_name,
                                       more_item)
        with allure.step(f'Проверить переадресацию на страницу {more_name}'):
            if more_name == 'Android_App':
                assert self.page.get_current_url() == 'https://wallscloud.net/en'
            else:
                assert self.page.get_current_url() == f'https://wallscloud.net/en/{more_name.lower()}'


    @allure.title("Поиск изображения")
    def test_search_bar(self):
        text = Faker().word()

        self.page.fill_search_text(text)
        self.page.search_button_click()

        with allure.step("Проверить поиск по тексту: '{text}'"):
            assert self.page.is_element_visible(mpl.HEADER['Search Button'])
            assert self.page.get_current_url() == f'https://wallscloud.net/en/search?q={text}&sort=&color='


    @allure.title("Кнопки поиска по цвету {color_name}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('color_name, color_selector',
                             mpl.COLORS.items(),
                             ids=tuple(mpl.COLORS.keys()))
    def test_color_search(self, color_name, color_selector):
        self.page.select_menu_and_item('Color Search', color_name, color_selector)

        with allure.step("Проверить что цвет совпадает с выбранной кнопкой"):
            assert self.page.get_text(mpl.COLOR_VALUE) == color_name.split(' ')[1]

        self.page.search_button_click()

        with allure.step("Проверить URL с параметром цвета"):
            assert self.page.get_current_url() == f'https://wallscloud.net/en/search?q=&sort=color&color={color_name.split(" #")[1]}'


    @allure.title("Смены языка на {lang_name}")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('lang_name, lang_selector',
                             mpl.LANGUAGE_SELECTORS.items(),
                             ids=tuple(mpl.LANGUAGE_SELECTORS.keys()))
    def test_language_switch(self, lang_name, lang_selector):
        self.page.change_language(lang_selector)

        with allure.step(f"Проверить что url и текст кнопки меняется на {lang_name}"):
            assert self.page.get_inner_text(mpl.HEADER['Language Button']) == lang_name
            assert self.page.get_current_url() == f'https://wallscloud.net/{lang_name.lower()}'

        with allure.step('Проверить что текст кнопки логина меняет перевод'):
            match lang_name:
                case "EN":
                    assert self.page.get_text(mpl.HEADER['Login Button']) == 'Guest'
                case "RU":
                    assert self.page.get_text(mpl.HEADER['Login Button']) == 'Гость'
                case "UA":
                    assert self.page.get_text(mpl.HEADER['Login Button']) == 'Гість'


    @allure.title("Кнопоки login и sing up")
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize('item_name, item_selector', mpl.LOGIN_ITEMS.items(), ids=tuple(mpl.LOGIN_ITEMS.keys()))
    def test_login_button(self, item_name, item_selector):
        self.page.select_menu_and_item('Login Button', item_name, item_selector)

        with allure.step(f"Проверить переход на {item_name}"):
            assert self.page.get_current_url() == f"https://wallscloud.net/en/account/{item_name}"


