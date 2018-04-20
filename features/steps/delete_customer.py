from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

@given('it displays customer "{name}" with the mail "{email}"')
def step_impl(context, name, email):
    context.browser.find_element_by_xpath('//*[@id="button-filter"]').click()
    customers_list = context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
    found = False
    for row in customers_list:
        tdata = row.find_elements_by_tag_name("td")
        if (tdata[0].text == "No results!"):
            break
        if (tdata[1].text == name):
            if (tdata[2].text == email):
                context.customer_selector = tdata[0].find_element_by_tag_name("input")
                context.edit_button = tdata[-1].find_elements_by_tag_name('a')[-1]
                found = True
    assert found, "Customer {0} with email {1} is not in Customer List".format(name, email)

# Je zde potreba name a email promenne ?????????
# udelat z context.customer_selector dict podle jmena ???
@when('the user selects the customer "{name}" with the mail "{email}"')
def step_impl(context, name, email):
    context.customer_selector.click()

@when('the user clicks the Delete button')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()
    try:
        WebDriverWait(context.browser, 3).until(EC.alert_is_present())
        alert = context.browser.switch_to_alert()
        alert.accept()
    except TimeoutException:
        raise TimeoutException('Alert for delete confirmation not displayed in given time')

@then('the customer "{name}" with the mail "{email}" is no longer displayed')
def step_impl(context, name, email):
    context.browser.find_element_by_xpath('//*[@id="button-filter"]').click()
    customers_list = context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
    found = False
    for row in customers_list:
        tdata = row.find_elements_by_tag_name("td")
        if (tdata[0].text == "No results!"):
            break
        if (tdata[1].text == name):
            if (tdata[2].text == email):
                found = True
    assert not found, "Customer {0} with email {1} is still in Customer List".format(name, email)

###############################################################################

@when('the user clicks the Select all button')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/thead/tr/td[1]/input').click()

@then('the Customer List is empty')
def step_impl(context):
    context.browser.find_element_by_xpath('//*[@id="button-filter"]').click()
    customers_list = context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
    assert len(customers_list) == 1, "Customer List is not empty" # just header
    assert customers_list[0].text == "No results!", "Customer List is not empty"
