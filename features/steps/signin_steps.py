from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign in')
def Click_signin_menu(context):
    context.app.signin_page.click_signin_menu()
    sleep(2)

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


