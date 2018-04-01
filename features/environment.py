# environment.py
# Projekt ITS - Behavior-driven development
# Author: Jan Koci
# Date: 31.3.2018
# Brief: file to setup BDD features
from selenium import webdriver

# creates a selenium web driver and goes to the Customers webpage
def before_all(context):
    context.browser = webdriver.Chrome(executable_path="./chromedriver")
    context.browser.get('http://mys01.fit.vutbr.cz:8028/admin/')
    context.browser.find_element_by_xpath('//*[@id="input-username"]').send_keys("admin")
    context.browser.find_element_by_xpath('//*[@id="input-password"]').send_keys("admin")
    context.browser.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[3]/button').click()
    context.browser.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div[3]/div/div[3]/a').click()

# closes the web driver
def after_all(context):
    context.browser.quit()
