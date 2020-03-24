from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from features.logger import logger

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)
        self.alerts = Alert(self.driver)

    def open_page(self, url: str):
        logger.info(f'Opened page {url}')
        self.driver.get(url)

    def click(self, *locator):
        elem = self.driver.find_element(*locator)
        elem.click()

    def click_elem_idx(self, *locator, idx):
        elements = self.find_elements(*locator)
        elements[idx].click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def verify_element_text(self, expected_text: str, *locator):
        self.wait_for_element_appear(*locator)
        actual_text = self.driver.find_element(*locator).text
        actual_text_low = actual_text.lower()
        expected_text_low = expected_text.lower()
        assert expected_text_low in actual_text_low, f'Expected_text {expected_text}, but got {actual_text}'

    def hover_over_element(self, *locator):
        element = self.find_element(*locator)
        self.actions.move_to_element(element).perform()

    def hover_over_element_idx(self, *locator, idx):
        elements = self.find_elements(*locator)
        self.actions.move_to_element(elements[idx]).perform()

    def scroll_into_view(self, *locator):
        elem = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView()", elem)


