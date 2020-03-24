from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SigninPage(Page):

    MEMBER_MENU_LOCATOR = (By.XPATH, "//div[@class='remodal-content']//button[@class='button large secondary']")
    EMAIL_SIGNN_INPUT = (By.ID, 'modal-txt-signin-email' )
    PASSWORD_SIGNIN_INPUT = (By.ID, 'modal-txt-signin-password' )
    SUBMIT_SIGNIN_LOCATOR = (By.XPATH, "//button[@type='submit'][text()='Sign in']")
    TEXT_SIGNIN_LOCATOR = (By.XPATH, "//div[@id='app']//h2")
    MY_ACCOUNT_LOCATOR = (By.XPATH, "//a[contains(text(),'My Account') and @class='menu__myhm']")

    def click_member_menu_item(self):
        self.click(*self.MEMBER_MENU_LOCATOR)

    def input_email(self, text_email: str):
        print('text email = ', text_email)
        self.input(text_email, *self.EMAIL_SIGNN_INPUT)

    def input_password(self, text_password: str):
        print('text password = ', text_password)
        self.input(text_password, *self.PASSWORD_SIGNIN_INPUT)

    def click_submit_signin_button(self):
        self.wait_for_element_click(*self.SUBMIT_SIGNIN_LOCATOR)

    def click_my_account_button(self, *locator):
        self.wait_for_element_click(*self.MY_ACCOUNT_LOCATOR)

    def verify_header_result(self, expected_text: str):
        self.verify_element_text(expected_text, *self.TEXT_SIGNIN_LOCATOR)
