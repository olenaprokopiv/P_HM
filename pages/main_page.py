from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'main-search')
    SEARCH_ICON = (By.CSS_SELECTOR, ".menu__search_submit")
    SUGGESTION_ITEM = (By.CSS_SELECTOR, '#ui-id-1 li')

    def open(self):
        self.open_page('https://www2.hm.com/en_us/index.html')

    def search_product(self, text: str):
        print('text = ', text)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT))
        self.input(text, *self.SEARCH_INPUT)
        self.wait_for_element_click(*self.SEARCH_ICON)

    def input_text_search_box(self, text: str):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        ActionChains(self.driver).move_to_element(search_box).perform()
        self.wait_for_element_appear(*self.SEARCH_INPUT)
        self.input(text, *self.SEARCH_INPUT)

    def count_suggestions(self, expected_num: int):
        sugg_item_list = self.driver.find_elements(*self.SUGGESTION_ITEM)
        n_expected_items = int(expected_num)
        print("num suggestions = ",len(sugg_item_list))
        n_elem = len(sugg_item_list)
        if n_elem > 0:
            assert n_elem == n_expected_items, f'expected {n_expected_items}, but got {n_elem}'
        else:
            print('Menu elements are not found')

