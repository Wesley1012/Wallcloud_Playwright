from pages.mainpage import MainPage
from locators import MainPageLocators as mpl
from faker import Faker
import pytest


class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = MainPage(page)
        self.page.open_main_page()

    '''Тесты каждого пункта меню категорий'''
    @pytest.mark.parametrize("categori_name, categori_item", mpl.CATEGORIES.items(), ids=tuple(mpl.CATEGORIES.keys()))
    def test_categories_items(self, categori_name, categori_item):
        self.page.select_menu_and_item(mpl.HEADER['Categories List'], categori_item)
        assert self.page.get_current_url() == f"https://wallscloud.net/en/category/{categori_name.lower()}"

    '''Тесты каждого пункта меню разрешений'''
    @pytest.mark.parametrize("resolution_name, resolution_item", mpl.RESOLUTIONS.items(), ids=mpl.RESOLUTION_IDS)
    def test_resolution_items(self, resolution_name, resolution_item):
        self.page.select_menu_and_item(mpl.HEADER['Resolutions List'], resolution_item)
        assert self.page.get_current_url() == f'https://wallscloud.net/en/resolution/{resolution_name.lower()}'

    '''Тесты каждого пункта меню топ'''
    @pytest.mark.parametrize("top_name, top_item", mpl.TOP_LIST.items(), ids=tuple(mpl.TOP_LIST.keys()))
    def test_top_items(self, top_name, top_item):
        self.page.select_menu_and_item(mpl.HEADER['Top List'], top_item)
        assert self.page.get_current_url() == f'https://wallscloud.net/en/wallpapers/{top_name.lower()}'

    '''Тесты каждого пункта меню 'Ещё' '''
    @pytest.mark.parametrize("more_name, more_item", mpl.MORE_LIST.items(), ids=tuple(mpl.MORE_LIST.keys()))
    def test_more_items(self, more_name, more_item):
        self.page.select_menu_and_item(mpl.HEADER['More List'], more_item)

        if more_name == 'Android_App':
            assert self.page.get_current_url() == 'https://wallscloud.net/en'
        else:
            assert self.page.get_current_url() == f'https://wallscloud.net/en/{more_name.lower()}'

    '''Проверка поля поиска'''
    def test_search_bar(self):
        text = Faker().word()

        self.page.fill(mpl.HEADER['Search Bar'], text)
        assert self.page.is_element_visible(mpl.HEADER['Search Button'])

        self.page.click(mpl.HEADER['Search Button'])
        assert self.page.get_current_url() == f'https://wallscloud.net/en/search?q={text}&sort=&color='

    '''Проверка кнопки поиска по цвету'''
    @pytest.mark.parametrize('color_name, color_locator', mpl.COLORS.items(), ids=tuple(mpl.COLORS.keys()))
    def test_color_search(self, color_name, color_locator):
        self.page.select_menu_and_item(mpl.HEADER['Color Search'], color_locator)

        # Проверка того что цвет совпадает с выбранной кнопкой
        assert self.page.get_text(mpl.COLOR_VALUE) == color_name.split(' ')[1]

        self.page.click(mpl.HEADER['Search Button'])

        # Проверка того то значение цвета в параметрах строки передаётся правильно
        assert self.page.get_current_url() == f'https://wallscloud.net/en/search?q=&sort=color&color={color_name.split(" #")[1]}'

    '''Проверка кнопки смены языка'''
    @pytest.mark.parametrize('lang_name, lang_selector', mpl.LANGUAGE_SELECTORS.items(),
                             ids=tuple(mpl.LANGUAGE_SELECTORS.keys()))
    def test_language_switch(self, lang_name, lang_selector):
        self.page.change_language(lang_selector)

        assert self.page.get_inner_text(mpl.HEADER['Language Button']) == lang_name
        assert self.page.get_current_url() == f'https://wallscloud.net/{lang_name.lower()}'

        match lang_name:
            case "EN":
                assert self.page.get_text(mpl.HEADER['Login Button']) == 'Guest'
            case "RU":
                assert self.page.get_text(mpl.HEADER['Login Button']) == 'Гость'
            case "UA":
                assert self.page.get_text(mpl.HEADER['Login Button']) == 'Гість'

    '''Тесты кнопок login и sing up'''
    @pytest.mark.parametrize('item_name, item_selector', mpl.LOGIN_ITEMS.items(), ids=tuple(mpl.LOGIN_ITEMS.keys()))
    def test_login_button(self, item_name, item_selector):
        self.page.select_menu_and_item(mpl.HEADER['Login Button'], item_selector)
        assert self.page.get_current_url() == f"https://wallscloud.net/en/account/{item_name}"


