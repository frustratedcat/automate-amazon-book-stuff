from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
  var.send_keys(file + Keys.ENTER) if file else var.send_keys(Keys.ENTER)

def main():
  # Log in
  click_select(20, 'account_list', By.ID, 'nav-link-accountList')
  input_select(5, 'input_email', By.ID, 'ap_email', creds.username)
  input_select(5, 'input_password', By.ID, 'ap_password', creds.password)

  # Navigate to content library
  click_select(100, 'account_list', By.ID, 'nav-link-accountList')
  input_select(5, 'content_library', By.LINK_TEXT, 'Content Library', None)
  click_select(5, 'books', By.ID, 'content-ownership-books')

  # Get pages and download items
  last_page = driver.find_element(By. XPATH, '//div[contains(@id, "pagination")]//a[last()]').text

  # Pages loop
  for num in range(0, int(last_page)):
    # Next Page
    click_select(20, 'page', By.XPATH, '//div[contains(@id, "pagination")]//a[contains(@id, "page-' + str(num + 1) + '")]')

    all_books = driver.find_elements(By.XPATH, '//tr[contains(@class, "ListItem-module_row")]')
    # Download items loop
    for i in range(len(all_books)):
      click_select(20, 'drop_down', By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "dd_title")]')
      click_select(20, 'transfer_click', By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER")]')
      click_select(20, 'click_device', By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//span[contains(@id, "download_and_transfer_list")]')
      click_select(20, 'click_download', By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER_ACTION")]/span[text()="Download"]')
      click_select(20, 'notification_close', By.ID, 'notification-close')

if __name__ == '__main__':
  main()