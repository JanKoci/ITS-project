from behave import *

@given('the Customer List contains {num:d} customer with "{key}" "{value}"')
@given('the Customer List contains {num:d} customers with "{key}" "{value}"')
def step_impl(context, num, key, value):
    pass

@when('the user filters the search using "{key}" "{value}"')
def step_impl(context, key, value):
    pass

@then('exactly {num:d} customers are displayed in the Customer List')
def step_impl(context, num):
    pass

@then('all displayed customers have "{key}" "{value}"')
def step_impl(context, key, value):
    pass

###### OPRAVIT VE FEATURE ????????????????
@when('the user filters the search using the Date Added "{date}"')
def step_impl(context, date):
    pass

@when('the user filters the search using the IP "{ip}"')
def step_impl(context, ip):
    pass
