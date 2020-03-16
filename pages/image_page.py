from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from p_hm.pages.base_page import Page
from time import sleep

class ImagePage(Page):

    SEARCH_INPUT_LOCATOR = (By.ID, 'main-search')
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[@class='menu__search_submit']")
    IMG_FIRST_ITEM = (By.XPATH, "//div[@class='section']//li[@class='product-item'][1]")
    IMG_SECOND_ITEM = (By.XPATH, "//div[@class='section']//li[@class='product-item'][4]")

    def open(self):
        self.open_page('https://www2.hm.com/en_us/index.html')

    def open_skirts(self):
        self.open_page('https://www2.hm.com/en_us/productpage.0851400008.html')

    def search_product(self, text: str):
        print('text = ', text)
        self.input(text, *self.SEARCH_INPUT_LOCATOR)
        self.click(*self.SEARCH_BUTTON_LOCATOR)

    def click_first_item(self):
        self.click(*self.IMG_FIRST_ITEM)

    def click_second_item(self):
        self.click(*self.IMG_SECOND_ITEM)


