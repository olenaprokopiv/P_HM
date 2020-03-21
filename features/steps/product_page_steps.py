from behave import given, when, then
from time import sleep

@when('Select size')
def click_select_size(context):
    context.app.product_page.click_select_size()

@when('Add {product} to the cart')
def click_add(context, product):
    context.app.product_page.click_add()

@then('Number of items in the cart more than zero')
def check_cart_item_number(context):
    sleep(2)
    context.app.product_page.check_cart_item_number()

@then('Number of items in the cart is {number}')
def check_cart_item_number(context, number):
    sleep(2)
    context.app.product_page.check_cart_item_number()

@when('Select item {number}')
def click_select_item(context, number):
    context.app.product_page.click_select_item_number()

@then('Menu will have {expected_items} items')
def get_elem_links_list(context, expected_items):
    context.app.product_page.get_elem_links_list(expected_items)

@when('Click black')
def click_black(context):
    context.app.product_page.click_black()