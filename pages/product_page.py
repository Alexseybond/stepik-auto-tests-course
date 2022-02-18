from pages.base_page import BasePage
from pages.locators import ProductLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPages(BasePage):
    def should_be_cart_page(self):
        self.should_be_price_in_basket()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_cart_url(self):
        assert 'login' in self.browser.current_url, 'The referenced link does not contain "login"'

    def should_be_price_in_basket(self):
        result = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_FORM).text
        assert 'Log In' in result, 'Form does not contain "Log In"'

    def should_be_register_form(self):
        result = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM).text
        assert "Register" in result, 'Form does not contain "Register"'

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_LINK)
        login_link.click()

    def product_add_to_cart(self):
        login_link = self.browser.find_element(*BUTTON_ADD_TO_CART.LOGIN_LINK)
        login_link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")