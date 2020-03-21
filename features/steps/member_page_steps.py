from behave import given, when, then

@when('Click on member menu item')
def click_member_menu_item(context):
    context.app.member_page.click_member_menu_item()

@when('Input email {search_text}')
def input_email(context, search_text):
    print('search_text = ', search_text)
    context.app.member_page.input_email(search_text)

@when('Input password {search_text}')
def input_password(context, search_text):
    print('search_text = ', search_text)
    context.app.member_page.input_password(search_text)

@when('Input date of birth {date_text}')
def input_date(context, date_text):
    print('search_text = ', date_text)
    context.app.member_page.input_date(date_text)

@when('Click on the checkbox')
def click_checkbox_button(context):
    context.app.member_page.click_checkbox_button()

@when('Click on the BECOME A MEMBER')
def click_submit_button(context):
    context.app.member_page.click_submit_button()