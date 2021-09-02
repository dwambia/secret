from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'admin'
passwordStr = 'abc123nv'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))

# fill in username and hit the next button

username = browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(passwordStr)

ACCESS_TOKEN="0NC6O0ThWq69BcWmrtbD2ev0UDivbG8OQ1Zs"

signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
