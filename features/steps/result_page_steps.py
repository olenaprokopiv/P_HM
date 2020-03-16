from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TOOL_BAR_TEXT = (By.CSS_SELECTOR, '.section h1')

@then('Search results for {product} is shown')
def verify_header_result(context, product):
    result_text = context.driver.find_element(*TOOL_BAR_TEXT).text
    context.app.result_page.verify_header_result(product)