from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open H&M page')
def open_hm(context):
    context.app.main_page.open()

@when('Input in Search Box {search_text}')
def input_text_search_box(context, search_text):
    print('search_text = ', search_text)
    context.app.main_page.input_text_search_box(search_text)

@when('Search product {search_text}')
def Search_product(context, search_text):
    sleep(4)
    print('search_text = ', search_text)
    context.app.main_page.search_product(search_text)
    context.app.save_current_window()

@then('Switch to product search page')
def switch_to_saved_window(context):
    context.app.driver.back()
    sleep(2)

@then('Count {expected_num} suggestions')
def count_suggestions(context, expected_num):
    context.app.main_page.count_suggestions(expected_num)


