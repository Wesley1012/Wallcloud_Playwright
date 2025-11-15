from pages.authpage import AuthPage
import pytest
from faker import Faker


@pytest.mark.requires_captcha
def test_signup_with_valid_data(page):
    """This test with valid values needed manual passage reCAPCHA in contrast to tests with invalid values"""
    page = AuthPage(page)
    page.open_signup_page().fill_email(f"{Faker().email()}") \
        .fill_name("user123") \
        .fill_password("12345asd") \
        .fill_re_password("12345asd")

    page.click_recaptcha()
    page.submit_btn()

    assert page.get_error_count() == 0
    assert page.get_alert() == 'Докажите, что вы не робот.'


def test_singup_without_capcha(page):
    page = AuthPage(page)
    page.open_signup_page().fill_email("test@example.com") \
                           .fill_name("user123") \
                           .fill_password("12345asd") \
                           .fill_re_password("12345asd")
    page.submit_btn()
    assert page.get_alert() == 'Докажите, что вы не робот.'


@pytest.mark.parametrize("test_case, email, name, password, re_password", [
    (1, '', '', '', ''),
    (2, f"{Faker().name()}@@.test", 'user', '1234', 'asdf'),
    (3, Faker().email(), 'user', '12345', '12345')],
    ids=('Empty fields', 'Invalid email, password, re_password','Short name'))
def test_all_errors_message(page, email, name, password, re_password, test_case):
    page = AuthPage(page)
    page.open_signup_page().fill_email(email) \
                            .fill_name(name) \
                            .fill_password(password) \
                            .fill_re_password(re_password)
    page.click_recaptcha()
    page.submit_btn()

    match test_case:
        case 1:
            assert page.get_email_error() == 'Поле Email адрес обязательно.'
            assert page.get_name_error() == 'Поле Никнейм обязательно.'
            assert page.get_password_error() == 'Поле Пароль обязательно.'
            assert page.get_re_password_error() == 'Поле Повторите пароль обязательно.'
        case 2:
            assert page.get_email_error() == 'Поле Email адрес должно содержать правильный E-mail адрес.'
            assert page.get_password_error() == 'Длина поля Пароль должна быть по крайней мере 5 символов.'
            assert page.get_re_password_error() == 'Поле Повторите пароль не соответствует параметру Пароль.'
        case 3:
            assert page.get_alert() == 'Некорректный никнейм! Допустимы только символы: A-Z 0-9 _ (нижнее подчеркивание)'

