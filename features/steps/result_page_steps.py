from behave import given, when, then
from time import sleep

@then('Search results for {product} is shown')
def verify_header_result(context, product):
    #sleep(2)
    context.app.result_page.verify_header_result(product)