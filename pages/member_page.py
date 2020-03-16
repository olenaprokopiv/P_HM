from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from p_hm.pages.base_page import Page
from time import sleep

class MemberPage(Page):

   EMAIL_INPUT = (By.ID, 'modal-signin-email')
   PASSWORD_INPUT = (By.ID, 'modal-signin-password')
   MONTH_INPUT = (By.ID, 'modal-signin-month')
   DAY_INPUT = (By.ID, 'modal-signin-day')
   YEAR_INPUT = (By.ID, 'modal-signin-year')
   CHECKBOX_LOCATOR = (By.XPATH, "//input[@type='checkbox'][@id='modal-create-account-fashion-news']")
   SUBMIT_LOCATOR=(By.XPATH, "//button[@type='submit'][@class='button large js-submit-join']")
   MEMBER_MENU_LOCATOR = (By.XPATH, "//button[@class='button large secondary']")

   def click_member_menu_item(self):
       self.click(*self.MEMBER_MENU_LOCATOR)

   def input_email(self, text_email: str):
       print('text email = ', text_email)
       self.input(text_email, *self.EMAIL_INPUT)

   def input_password(self, text_password: str):
       print('text password = ', text_password)
       self.input(text_password, *self.PASSWORD_INPUT)

   def input_date(self, text_date: str):
       print('text date = ', text_date)
       parts = text_date.split('/')
       print('parts =', parts )
       month_str = parts[0]
       day_str = parts[1]
       year_str = parts[2]
       self.input(month_str, *self.MONTH_INPUT)
       self.input(day_str, *self.DAY_INPUT)
       self.input(year_str, *self.YEAR_INPUT)

   def click_checkbox_button(self):
       self.click(*self.CHECKBOX_LOCATOR)

   def click_submit_button(self):
       self.click(*self.SUBMIT_LOCATOR)
       sleep(2)