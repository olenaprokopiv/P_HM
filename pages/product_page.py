from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from p_hm.pages.base_page import Page
from time import sleep

class ProductPage(Page):

    SELECT_SIZE_LOCATOR = (By.XPATH, "//*[@id='picker-1']/button")
    CHOOSE_SIZE_LOCATOR = (By.XPATH, '//*[@id="picker-1"]/ul/li[3]/div/button')
    ADD_TO_CART_LOCATOR = (By.XPATH, "//button[@data-added-text='Item added']")
    COUNT_ITEM_LOCATOR = (By.XPATH, "//span[@class='shoppingbag-item-count']")
    SELECT_ITEM_LOCATOR = (By.XPATH, "//select[@class='Select-module_select__3ZfQR']")
    CHOOSE_ITEM_LOCATOR = (By.XPATH, "//div[@class='Field-module_childWrapper__tFcCt']//select//option[@value='2']")
    COLOR_SKIRTS_LOCATOR = (By.XPATH, "//ul[@class='group']//li")
    BLACK_CALOR_LOCATOR = (By.XPATH, "//ul[@class='group']//a[@title='Black']")

    def click_select_size(self):
        self.click(*self.SELECT_SIZE_LOCATOR)
        self.click(*self.CHOOSE_SIZE_LOCATOR)

    def click_add(self):
         self.click(*self.ADD_TO_CART_LOCATOR)
         sleep(2)

    def check_cart_item_number(self):
        sleep(2)
        #wait = WebDriverWait(self.driver, 5)
        #wait.until(EC.presence_of_element_located(self.COUNT_ITEM_LOCATOR))
        #wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='shoppingbag-item-count']")))
        elem = self.driver.find_element(*self.COUNT_ITEM_LOCATOR)
        print('Item number in the shopping bag = ',elem.text)
        strnum = elem.text
        n = int(strnum)

        assert n > 0

    def click_select_item_number(self):
        self.click(*self.SELECT_ITEM_LOCATOR)
        self.click(*self.CHOOSE_ITEM_LOCATOR)

    def get_elem_links_list(self, expected_items):
        elem_links_list = self.driver.find_elements(*self.COLOR_SKIRTS_LOCATOR)
        expected_items = int(expected_items)
        print(len(elem_links_list))
        if len(elem_links_list) > 0:
            assert len(elem_links_list) == expected_items, f'expected {expected_items}, but got {elem_links_list}'
        else:
            print('not found')

    def click_black(self):
         self.click(*self.BLACK_CALOR_LOCATOR)
         sleep(2)