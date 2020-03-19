from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class SigninPage(Page):
    SIGNIN_MENU_LOCATOR = (By.XPATH, "//li[@class='menu__session__item']//a[contains(text(),'Sign in')]")
    MEMBER_MENU_LOCATOR = (By.XPATH, "//div[@class='remodal-content']//button[@class='button large secondary']")
    EMAIL_SIGNN_INPUT = (By.ID, 'modal-txt-signin-email' )
    PASSWORD_SIGNIN_INPUT = (By.ID, 'modal-txt-signin-password' )
    SUBMIT_SIGNIN_LOCATOR = (By.XPATH, "//div[@class='remodal-content']//button[@type='submit'][text()='Sign in']" )

    def click_signin_menu(self):
        self.click(*self.SIGNIN_MENU_LOCATOR)

    def click_member_menu_item(self):
        self.click(*self.MEMBER_MENU_LOCATOR)

    def input_email(self, text_email: str):
        print('text email = ', text_email)
        self.input(text_email, *self.EMAIL_SIGNN_INPUT)

    def input_password(self, text_password: str):
        print('text password = ', text_password)
        self.input(text_password, *self.PASSWORD_SIGNIN_INPUT)

    def click_submit_signin_button(self):
        self.click(*self.SUBMIT_SIGNIN_LOCATOR)
        sleep(2)