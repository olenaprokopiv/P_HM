from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from p_hm.pages.base_page import Page
from time import sleep

class ResultPage(Page):

    TOOL_BAR_TEXT = (By.CSS_SELECTOR, '.section h1')

    def verify_header_result(self, expected_text: str):
        self.verify_element_text(expected_text, *self.TOOL_BAR_TEXT)
