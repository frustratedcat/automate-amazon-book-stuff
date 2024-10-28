from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import creds

driver = webdriver.Firefox()

driver.get("https://wwww.amazon.com")

driver.implicitly_wait(5)
click_sign_in = driver.find_element(By.ID, "nav-link-accountList").click()

driver.implicitly_wait(5)
input_email = driver.find_element(By.ID, "ap_email")
input_email.send_keys(creds.username + Keys.ENTER)

driver.implicitly_wait(5)
input_password = driver.find_element(By.ID, "ap_password")
input_password.send_keys(creds.password + Keys.ENTER)
