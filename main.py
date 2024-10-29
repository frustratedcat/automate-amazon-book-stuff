from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import creds

driver = webdriver.Firefox()
driver.get("https://wwww.amazon.com")

def implicitly_wait(time):
  driver.implicitly_wait(time)

def click_select(time, var, type, name):
  implicitly_wait(time)
  var = driver.find_element(type, name).click()

def input_select(time, var, type, name, file):
  implicitly_wait(time)
  var = driver.find_element(type, name)
  if file:
    var.send_keys(file + Keys.ENTER)
  else:
    var.send_keys(Keys.ENTER)

click_select(20, 'account_list', By.ID, 'nav-link-accountList')
input_select(5, 'input_email', By.ID, 'ap_email', creds.username)
input_select(5, 'input_password', By.ID, 'ap_password', creds.password)
click_select(100, 'account_list', By.ID, 'nav-link-accountList')
input_select(5, 'content_library', By.LINK_TEXT, 'Content Library', None)
click_select(5, 'books', By.ID, 'content-ownership-books')

click_select(20, 'drop_down', By.ID, 'dd_title')
click_select(20, 'transfer_click', By.XPATH, '//div[contains(@id, "DOWNLOAD_AND_TRANSFER")]')
click_select(20, 'click_device', By.XPATH, '//span[contains(@id, "download_and_transfer_list")]')
click_select(20, 'click_download', By.XPATH, '//div[contains(@id, "DOWNLOAD_AND_TRANSFER_ACTION")]/span[text()="Download"]')
click_select(20, 'notification_close', By.ID, 'notification-close')
