####################################################
# add_customer.py
# Projekt ITS - Behavior-driven development
# Author: Jan Koci
# Date: 31.3.2018
# Brief: implementation of test steps
#         defined in file 1add.feature
####################################################
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


# get the required panel page
@given('a web browser displays the "{panel_title}" panel')
def step_impl(context, panel_title):
    # find out in whitch panel we are
    panel = context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]').text
    # if we are not in the required panel
    if (panel != panel_title):
        # go to customer list panel
        context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/ul/li[2]/a').click()
        if (panel_title == "Add Customer"):
            context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()
        elif (panel_title == "Edit Customer"):
            customers_list = context.browser.find_element_by_xpath(
                '//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
            # when the Edit Customer panel is required
            # there has to be at least customer in the customer's list
            assert len(customers_list) >= 1 and customers_list[0].text != "No results!", (
                                                "Customer List is empty")
            edit_button = customers_list[0].find_elements_by_tag_name('a')[-1]
            edit_button.click()
        panel = context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]').text
    # assert we are in the required panel
    assert panel == panel_title, "Expected = {0}, Real = {1}".format(panel_title, panel)


# apply action
@when('the user clicks the "{button}" button')
def step_impl(context, button):
    if (button == "Add New"):
        context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()
    elif (button == "Save"):
        context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()
    elif (button == "Cancel"):
        context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/a').click()
    elif (button == "Add Address"):
        context.browser.find_element_by_xpath('//*[@id="address-add"]/a').click()
    elif (button == "Edit"):
        context.edit_button.click()
    elif (button == "Select all"):
        context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/thead/tr/td[1]/input').click()
    elif (button == "Delete"):
        context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()
        # when we click the delete button an alert shows up
        # and we have to accept it
        try:
            WebDriverWait(context.browser, 3).until(EC.alert_is_present())
            alert = context.browser.switch_to_alert()
            alert.accept()
        except TimeoutException:
            raise TimeoutException('Alert for delete confirmation not displayed in given time')
    else:
        # undefined
        exit(1)



# check action results
@then('the "{panel_title}" panel shows up')
def step_impl(context, panel_title):
    panel = context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/h3').text
    assert panel == panel_title, ("The title of opened panel is not {0}, "
            "it is {1}".format(panel_title, title.text))
###############################################################################

@given('the user types all obligates values')
@when('the user types all obligated values')
def step_impl(context):
    # send data specified in feature to the browser
    for row in context.table: # table has to have just one row !
        context.browser.find_element_by_xpath('//*[@id="input-firstname"]').send_keys(row['first_name'])
        context.browser.find_element_by_xpath('//*[@id="input-lastname"]').send_keys(row['last_name'])
        context.browser.find_element_by_xpath('//*[@id="input-email"]').send_keys(row['email'])
        context.browser.find_element_by_xpath('//*[@id="input-telephone"]').send_keys(row['telephone'])
        context.browser.find_element_by_xpath('//*[@id="input-password"]').send_keys(row['password'])
        context.browser.find_element_by_xpath('//*[@id="input-confirm"]').send_keys(row['confirm'])
        context.customer_name = row['first_name'] + ' ' + row['last_name']
        context.customer_email = row['email']


@then('the browser goes back to the Customer List panel')
def step_impl(context):
    # assert browser displays the Customer List panel
    panel = context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]').text
    assert panel == "Customer List", ("Expected = Customer List, Real = {0}\n"
                    "Customer already exists").format(panel)

@then('the added customer appears in the Customer List')
def step_impl(context):
    # find the added customer in the customers list
    context.browser.find_element_by_xpath('//*[@id="button-filter"]').click()
    customers_list = context.browser.find_element_by_xpath(
        '//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
    found = False
    for row in customers_list:
        tdata = row.find_elements_by_tag_name("td")
        if (tdata[1].text == context.customer_name):
            if (tdata[2].text == context.customer_email):
                found = True
                break
    assert found, "Added customer {0} not found in Customer List".format(customer_name)

###############################################################################

@when('the user does not enter the "{param}"')
def step_impl(context, param):
    # send all data from feature to browser except the {param}
    for row in context.table:
        if (param != "first name"):
            context.browser.find_element_by_xpath('//*[@id="input-lastname"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-lastname"]').send_keys(row['first_name'])
        if (param != "last name"):
            context.browser.find_element_by_xpath('//*[@id="input-lastname"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-lastname"]').send_keys(row['last_name'])
        if (param != "email"):
            context.browser.find_element_by_xpath('//*[@id="input-email"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-email"]').send_keys(row['email'])
        if (param != "telephone"):
            context.browser.find_element_by_xpath('//*[@id="input-telephone"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-telephone"]').send_keys(row['telephone'])
        if (param != "password"):
            context.browser.find_element_by_xpath('//*[@id="input-password"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-password"]').send_keys(row['password'])
        if (param != "confirm"):
            context.browser.find_element_by_xpath('//*[@id="input-confirm"]').clear()
            context.browser.find_element_by_xpath('//*[@id="input-confirm"]').send_keys(row['confirm'])

@then('a warning message is displayed')
def step_impl(context):
    # wait for the warning message to appear
    try:
        WebDriverWait(context.browser, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div[1]')))
    except TimeoutException:
        raise TimeoutException("Warning message not displayed in given time")
    else:
        assert context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]').is_displayed(),(
                                                "Warning message not displayed")


###############################################################################


@when('the user types all obligated values for additional address')
def step_impl(context):
    for row in context.table:
        Select(context.browser.find_element_by_xpath('//*[@id="input-country1"]')).select_by_visible_text(row['country'])
        context.browser.find_element_by_xpath('//*[@id="input-firstname1"]').send_keys(row['first_name'])
        context.browser.find_element_by_xpath('//*[@id="input-lastname1"]').send_keys(row['last_name'])
        context.browser.find_element_by_xpath('//*[@id="input-address-11"]').send_keys(row['address1'])
        context.browser.find_element_by_xpath('//*[@id="input-city1"]').send_keys(row['city'])
        # after we enter the city we have to wait for the region field to appear
        try:
            WebDriverWait(context.browser, 3).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="input-zone1"]/option[11]')))
        except TimeoutException:
            pass
        Select(context.browser.find_element_by_xpath('//*[@id="input-zone1"]')).select_by_visible_text(row['region'])
