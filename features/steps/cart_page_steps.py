from behave import given, when, then

@when('Click cart button')
def click_cart_button(context):
    context.app.cart_page.click_cart_button()

@then('Verify cart title {cart_title}')
def verify_cart_title(context, cart_title):
    context.app.cart_page.verify_cart_title(cart_title)

@when('Click remove item')
def click_remove_item(context):
    context.app.cart_page.click_remove_item()
