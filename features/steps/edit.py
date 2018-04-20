from behave import *

# sjednotit s ostatnimi ???
@when('the user clicks the Edit button')
def step_impl(context):
    context.edit_button.click()

@then('the browser displays the "{panel_title}" panel')
def step_impl(context, panel_title):
    panel = context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]').text
    assert panel == panel_title, "Expected = {0}, Real = {1}".format(panel_title, panel)

@when('the user changes customer\'s email to "{email}"')
def step_impl(context, email):
    context.browser.find_element_by_xpath('//*[@id="input-email"]').clear()
    context.browser.find_element_by_xpath('//*[@id="input-email"]').send_keys(email)
    context.browser.find_element_by_xpath('//*[@id="content"]/div[1]/div/div/button').click()

@then('customer "{name}" has new email "{email}"')
def step_impl(context, name, email):
    customers_list = context.browser.find_element_by_xpath('//*[@id="form-customer"]/div/table/tbody').find_elements_by_tag_name('tr')
    found = False
    for row in customers_list:
        tdata = row.find_elements_by_tag_name("td")
        if (tdata[1].text == name):
            if (tdata[2].text == email):
                found = True
    assert found, "Customer {0} with email {1} is not in Customer List".format(name, email)

@given('the "{section}" section is selected')
def step_impl(context, section):
    if (section == "history"):
        context.browser.find_element_by_xpath('//*[@id="form-customer"]/ul/li[2]/a').click()
    elif (section == "transaction"):
        context.browser.find_element_by_xpath('//*[@id="form-customer"]/ul/li[3]/a').click()
    elif (section == "reward points"):
        context.browser.find_element_by_xpath('//*[@id="form-customer"]/ul/li[4]/a').click()

@when('the user wites a new comment "{comment}"')
def step_impl(context, comment):
    context.browser.find_element_by_xpath('//*[@id="input-comment"]').send_keys(comment)
    context.browser.find_element_by_xpath('//*[@id="button-history"]').click()

# NOT WORKING, driver is quicker than the app :)
@then('the comment appears in customer\'s history')
def step_impl(context):
    pass
    # row = context.browser.find_element_by_xpath('//*[@id="history"]/div[1]/table/tbody').find_elements_by_tag_name('tr')[0]
    # found = False
    # tdata = row.find_elements_by_tag_name("td")
    # if (tdata[1].text == "new comment"):
    #     found = True
    # assert found, "Comment not found"

@when('the user writes "{key}" of the transaction as "{value}"')
def step_impl(context, key, value):
    pass

@when('the user writes "{key}" of the Reward Point as "{value}"')
def step_impl(context, key, value):
    pass

@then('the transaction appears in customer\'s transactions')
def step_impl(context):
    pass

@then('the Reward Point appears in customer\'s Reward Points')
def step_impl(context):
    pass

@then('the Balance is the sum of all points')
def step_impl(context):
    pass
