from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open H&M Skirts page')
def open_hm(context):
    context.app.image_page.open_skirts()

@when('Click image of the {number} item')
def click_first_item(context, number):
    context.app.image_page.click_first_item()

@then('Click item of the {number}')
def click_second_item(context, number):
    context.app.image_page.click_second_item()
