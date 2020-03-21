from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep

class CartPage(Page):

   CART_LOCATOR = (By.XPATH, "//span[@class='minicart parbase']//a")
   TOOL_BAR_CART_TEXT = (By.XPATH, "//div[@class='CartItemsList--wrapper___2s_UW']//h2")
   REMOVE_ITEM_LOCATOR = (By.XPATH, "//li[@class='CartItem-module_item__2FmSw']//button[@aria-label='Remove']")

   def click_cart_button(self):
       sleep(2)
       self.wait_for_element_click(*self.CART_LOCATOR)
       #self.click(*self.CART_LOCATOR)

   def verify_cart_title(self, text_title: str):
       self.verify_element_text(text_title, *self.TOOL_BAR_CART_TEXT)
       print('text = ', text_title)

   def click_remove_item(self):
        self.click_elem_idx(*self.REMOVE_ITEM_LOCATOR, idx = 1)