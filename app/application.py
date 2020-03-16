from p_hm.pages.main_page import MainPage
from p_hm.pages.result_page import ResultPage
from p_hm.pages.signin_page import SigninPage
from p_hm.pages.member_page import MemberPage
from p_hm.pages.cart_page import CartPage
from p_hm.pages.image_page import ImagePage
from p_hm.pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.result_page = ResultPage(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.member_page = MemberPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.image_page = ImagePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.saved_window = None

    def save_current_window(self):
        self.saved_window = self.driver.current_window_handle

    def switch_to_saved_window(self):
        self.driver.switch_to_window(self.saved_window)