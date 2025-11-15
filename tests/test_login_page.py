from pages.authpage import AuthPage
from test_data.credentials import VALID_EMAIL, VALID_PASSWORD
import pytest
from faker import Faker

@pytest.mark.positive
def test_login_with_valid_data(page):
    page = AuthPage(page)
    page.open_login_page().fill_email(VALID_EMAIL) \
                          .fill_password(VALID_PASSWORD)
    page.submit_btn()

    assert page.get_current_url() == 'https://wallscloud.net/ru'

@pytest.mark.negative
@pytest.mark.parametrize('test_case, email, password', (
    (1, '', ''),
    (2, f'{Faker().name()}@@.test', '1234'),
    (3, Faker().email(), '1234')
), ids=('Empty fields', 'Invalid email', 'Unregistered user'))
def test_login_errors(page, email, password, test_case):
    page = AuthPage(page)
    page.open_login_page()

    page.fill_email(email).fill_password(password)
    page.submit_btn()

    match test_case:
        case 1:
            assert page.get_email_error() == 'Поле Email адрес обязательно.'
            assert page.get_password_error() == 'Поле Пароль обязательно.'
        case 2:
            assert page.get_email_error() == 'Поле Email адрес должно содержать правильный E-mail адрес.'
        case 3:
            assert page.get_alert() == 'Неверный email или пароль'

@pytest.mark.negative
def test_needed_confirmation(page):
    '''Mayby you need to register, reCAPCHA is preventing automatic registration!'''
    page = AuthPage(page)
    page.open_login_page().fill_email('test1234@example.com') \
                           .fill_password('12345')
    page.submit_btn()
    assert page.get_alert() == 'Извините, вам нужно подтвердить свой email  адрес, мы выслали Вам код активации. Если письмо не пришло пожалуйста нажмите здесь.'
    assert page.get_alert_href() == "https://wallscloud.net/ru/account/resend-activation"

def test_no_account_btn(page):
    page = AuthPage(page)
    page.open_login_page()

    assert page.get_no_account_btn_href() == "https://wallscloud.net/ru/account/signup"

    page.click_no_account_btn()
    assert page.get_current_url() == 'https://wallscloud.net/ru/account/signup'

def test_forgot_password_btn(page):
    page = AuthPage(page)
    page.open_login_page()

    assert page.get_forgot_pass_btn_href() == "https://wallscloud.net/ru/account/reset-password"

    page.click_forgot_pass()
    assert page.get_current_url() == "https://wallscloud.net/ru/account/reset-password"


def test_checkbox_remember_me(page):
    page = AuthPage(page)
    page.open_login_page()

    assert not page.is_remember_me_checked(), "Чекбокс должен быть не отмечен по умолчанию"

    page.check_remember_me()
    assert page.is_remember_me_checked(), "Чекбокс должен быть отмечен после check_remember_me()"

    page.uncheck_remember_me()
    assert not page.is_remember_me_checked(), "Чекбокс должен быть не отмечен после uncheck_remember_me()"

    page.check_remember_me()
    assert page.is_remember_me_checked(), "Чекбокс должен снова отметиться"

    page.uncheck_remember_me()
    assert not page.is_remember_me_checked(), "Чекбокс должен снова сняться"
