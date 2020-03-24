from behave import given, when, then
from time import sleep


@when('Input signin email {search_text}')
def input_email(context, search_text):
    print('search_text = ', search_text)
    context.app.signin_page.input_email(search_text)

@when('Input signin password {search_text}')
def input_password(context, search_text):
    print('search_text = ', search_text)
    context.app.signin_page.input_password(search_text)

@when('Click on the SIGN IN')
def click_submit_signin_button(context):
    context.app.signin_page.click_submit_signin_button()

@when('Click on the My Account')
def click_my_account_button(context):
    context.app.signin_page.click_my_account_button()

@then('Results for {signin} is shown')
def verify_header_result(context, signin):
    context.app.signin_page.verify_header_result(signin)


