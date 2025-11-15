from pages.basepage import BasePage


class AuthPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://wallscloud.net/ru/account"

    EMAIL = "#user_email"
    NAME = "#user_name"
    PASSWORD = "input[name='user_password']"
    RE_PASSWORD = "input[name='re_user_password']"
    CAPCHA = "div.recaptcha-checkbox-border"
    SUBMIT_BTN = "button[type='submit']"

    EMAIL_ERROR = ".form-group.has-error:has(#user_email) .help-block"
    NAME_ERROR = ".form-group.has-error:has(#user_name) .help-block"
    PASSWORD_ERROR = ".form-group.has-error:has(input[name='user_password']) .help-block"
    RE_PASSWORD_ERROR = ".form-group.has-error:has(input[name='re_user_password']) .help-block"
    INFO_ALERT = ".alert"

    NO_ACCOUNT_BTN = 'a[href="https://wallscloud.net/ru/account/signup"]'
    FORGOT_PASS_BTN = 'a[href="https://wallscloud.net/ru/account/reset-password"]'
    REMEMBER_CHECKBOX = '#login-remember'


    def open_login_page(self):
        self.navigate("/login")
        return self

    def open_signup_page(self):
        self.navigate("/signup")
        return self

    def fill_email(self, text=''):
        self.page.fill(self.EMAIL, text)
        return self

    def fill_name(self, text=''):
        self.page.fill(self.NAME, text)
        return self

    def fill_password(self, text=''):
        self.page.fill(self.PASSWORD, text)
        return self

    def fill_re_password(self, text=''):
        self.page.fill(self.RE_PASSWORD, text)
        return self

    def submit_btn(self):
        self.page.click(self.SUBMIT_BTN)
        return self

    def click_recaptcha(self):
        try:
            recaptcha_frame = self.page.frame_locator("iframe[title*='reCAPTCHA']")
            recaptcha_frame.locator("#recaptcha-anchor").click()
            return self

        except Exception as e:
            print(f"Log_info: reCAPTCHA v2 with challenge don't complete, needed manual input")

            return self

    def click_forgot_pass(self):
        self.page.click(self.FORGOT_PASS_BTN)
        return self

    def click_no_account_btn(self):
        self.page.click(self.NO_ACCOUNT_BTN)
        return self

    def get_email_error(self):
        return self.get_text(self.EMAIL_ERROR).strip()

    def get_name_error(self):
        return self.get_text(self.NAME_ERROR).strip()

    def get_password_error(self):
        return self.get_text(self.PASSWORD_ERROR).strip()

    def get_re_password_error(self):
        return self.get_text(self.RE_PASSWORD_ERROR).strip()

    def get_error_count(self):
        return self.page.locator(".form-group.has-error").count()

    def get_alert(self):
        return self.get_text(self.INFO_ALERT).strip()

    def get_alert_href(self):
        return self.page.get_attribute(".alert-danger a", "href")

    def get_forgot_pass_btn_href(self):
        return self.page.get_attribute(self.FORGOT_PASS_BTN, "href")

    def get_no_account_btn_href(self):
        return self.page.get_attribute(self.NO_ACCOUNT_BTN, "href")

    def check_remember_me(self):
        if not self.page.is_checked(self.REMEMBER_CHECKBOX):
            self.page.check(self.REMEMBER_CHECKBOX)
        return self

    def uncheck_remember_me(self):
        if self.page.is_checked(self.REMEMBER_CHECKBOX):
            self.page.uncheck(self.REMEMBER_CHECKBOX)
        return self

    def is_remember_me_checked(self):
        return self.page.is_checked(self.REMEMBER_CHECKBOX)