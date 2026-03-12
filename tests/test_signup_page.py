import allure
import pytest
from faker import Faker
from pages.authpage import AuthPage
from test_data.credentials import VALID_EMAIL, VALID_PASSWORD


@allure.epic("Сайт выбора обоев для рабочего стола")
@allure.feature("Авторизация и регистрация")
@allure.story("Авторизация пользователя")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_method(self, page):
        self.page = AuthPage(page)
        self.page.open_login_page()


    @allure.title("Успешный вход с валидными данными")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.tag("smoke", "login", "positive")
    @pytest.mark.positive
    def test_login_with_valid_data(self):

        self.page.fill_email(VALID_EMAIL) \
            .fill_password(VALID_PASSWORD)
        self.page.submit_btn()

        with allure.step("Проверить редирект на главную страницу"):
            assert self.page.get_current_url() == 'https://wallscloud.net/ru'


    @allure.title("Ошибки валидации при входе: {test_case}")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("login", "validation", "negative")
    @pytest.mark.negative
    @pytest.mark.parametrize('test_case, email, password', (
            (1, '', ''),
            (2, f'{Faker().name()}@@.test', '1234'),
            (3, Faker().email(), '1234')
    ), ids=[
        'Пустые поля',
        'Невалидный email',
        'Незарегистрированный пользователь'
    ])
    def test_login_errors(self, test_case, email, password):

        with allure.step(f"Заполнить форму (кейс {test_case})"):
            self.page.fill_email(email).fill_password(password)
            self.page.submit_btn()

        with allure.step("Проверить сообщение об ошибке"):
            match test_case:
                case 1:
                    assert self.page.get_email_error() == 'Поле Email адрес обязательно.'
                    assert self.page.get_password_error() == 'Поле Пароль обязательно.'
                case 2:
                    assert self.page.get_email_error() == 'Поле Email адрес должно содержать правильный E-mail адрес.'
                case 3:
                    assert self.page.get_alert() == 'Неверный email или пароль'


    @allure.title("Вход с неподтверждённым email")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("login", "negative", "confirmation")
    @pytest.mark.negative
    def test_needed_confirmation(self):
        """
        Проверка входа пользователя с неподтверждённым email.
        Возможно, нужно предварительно зарегистрироваться, 
        так как reCAPTCHA мешает автоматической регистрации.
        """

        self.page.fill_email('test1234@example.com') \
            .fill_password('12345')
        self.page.submit_btn()

        with allure.step("Проверить сообщение о необходимости подтверждения email"):
            expected_alert = 'Извините, вам нужно подтвердить свой email  адрес, мы выслали Вам код активации. Если письмо не пришло пожалуйста нажмите здесь.'
            assert self.page.get_alert() == expected_alert

        with allure.step("Проверить ссылку на повторную отправку активации"):
            assert self.page.get_alert_href() == "https://wallscloud.net/ru/account/resend-activation"


    @allure.title("Проверка кнопки 'Нет аккаунта?'")
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("ui", "navigation", "links")
    def test_no_account_btn(self):

        with allure.step("Проверить href ссылки"):
            assert self.page.get_no_account_btn_href() == "https://wallscloud.net/ru/account/signup"

        with allure.step("Кликнуть по кнопке и проверить переход"):
            self.page.click_no_account_btn()
            assert self.page.get_current_url() == 'https://wallscloud.net/ru/account/signup'


    @allure.title("Проверка кнопки 'Забыли пароль?'")
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("ui", "navigation", "links")
    def test_forgot_password_btn(self):

        with allure.step("Проверить href ссылки"):
            assert self.page.get_forgot_pass_btn_href() == "https://wallscloud.net/ru/account/reset-password"

        with allure.step("Кликнуть по кнопке и проверить переход"):
            self.page.click_forgot_pass()
            assert self.page.get_current_url() == "https://wallscloud.net/ru/account/reset-password"


    @allure.title("Проверка чекбокса 'Запомнить меня'")
    @allure.severity(allure.severity_level.MINOR)
    @allure.tag("ui", "checkbox")
    def test_checkbox_remember_me(self):

        with allure.step("Проверить состояние по умолчанию"):
            assert not self.page.is_remember_me_checked(), "Чекбокс должен быть не отмечен по умолчанию"

        with allure.step("Отметить чекбокс"):
            self.page.check_remember_me()
            assert self.page.is_remember_me_checked(), "Чекбокс должен быть отмечен после check_remember_me()"

        with allure.step("Снять отметку с чекбокса"):
            self.page.uncheck_remember_me()
            assert not self.page.is_remember_me_checked(), "Чекбокс должен быть не отмечен после uncheck_remember_me()"

        with allure.step("Снова отметить чекбокс"):
            self.page.check_remember_me()
            assert self.page.is_remember_me_checked(), "Чекбокс должен снова отметиться"

        with allure.step("Снова снять отметку"):
            self.page.uncheck_remember_me()
            assert not self.page.is_remember_me_checked(), "Чекбокс должен снова сняться"