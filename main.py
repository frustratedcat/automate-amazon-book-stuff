from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import creds

driver = webdriver.Firefox()
driver.get("https://wwww.amazon.com")

def implicitly_wait(time):
  driver.implicitly_wait(time)

def click_account_list(time):
  implicitly_wait(time)
  account_list = driver.find_element(By.ID, "nav-link-accountList").click()

def input_select(var, type, name, file):
  implicitly_wait(5)
  var = driver.find_element(type, name)

  if file:
    var.send_keys(file + Keys.ENTER)
  else:
    var.send_keys(Keys.ENTER)

click_account_list(20)
input_select('input_email', By.ID, 'ap_email', creds.username)
input_select('input_password', By.ID, 'ap_password', creds.password)
click_account_list(100)
input_select('content_library', By.LINK_TEXT, 'Content Library', None)
