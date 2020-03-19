from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Search results for {product} is shown')
def verify_header_result(context, product):
    sleep(8)
    context.app.result_page.verify_header_result(product)