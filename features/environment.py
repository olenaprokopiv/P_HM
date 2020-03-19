from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from app.application import Application
from features.logger import *
from selenium.webdriver.support.events import EventFiringWebDriver

def browser_init(context):
    """
    :param context: Behave context
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    # BrowserStack
    # desired_capabilities = {
    #     "os": "OS X",
    #     "os_version": "Catalina",
    #     "browser": "Safari",
    #     "browser_version": "13.0",
    #     "resolution": "1600x1200",
    #     "name": "Bstack-[Python] Sample Test"
    # }
    # desired_capabilities = {
    #      "os": "Windows",
    #      "os_version": "10",
    #      "browser": "Chrome",
    #      "browser_version": "80",
    #      "resolution": "1600x1200",
    #      "name": "Bstack-[Python] Sample Test Chrome 1"
    #  }

    # url = f"http://olenaprokopiv1:or57XMmLLtXoCzq5oWtn@hub-cloud.browserstack.com/wd/hub"
    # context.driver = webdriver.Remote(url, desired_capabilities = desired_capabilities)
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options=chrome_options), MyListner())

    context.driver.maximize_window()
    context.driver.implicitly_wait(2)
    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 2)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

def before_step(context, step):
    print('\nStep step: ', step)

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)

def after_scenario(context,feature):
    context.driver.delete_all_cookies()
    context.driver.quit()