from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import creds
import os

# Clear Screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# Start up and connect
clear_screen()
print('Starting up\n')
driver = webdriver.Firefox()
driver.get("https://wwww.amazon.com")

# Click items
def click_select(time, type, name):
  driver.implicitly_wait(time)
  driver.find_element(type, name).click()

# Input items
def input_select(time, var, type, name, file):
  driver.implicitly_wait(time)
  var = driver.find_element(type, name)
  var.send_keys(file + Keys.ENTER) if file else var.send_keys(Keys.ENTER)

# Login function
def login():
  click_select(20, By.ID, 'nav-link-accountList')
  input_select(20, 'input_email', By.ID, 'ap_email', creds.get_username())
  input_select(20, 'input_password', By.ID, 'ap_password', creds.get_password())
  # Check for 2FA
  if driver.find_element(By.ID, 'auth-mfa-otpcode'):
    input_select(20, 'input_two_factor', By.ID, 'auth-mfa-otpcode', creds.get_two_factor())

# Navigation function
def nav_to_content_library():
  click_select(100, By.ID, 'nav-link-accountList')
  input_select(5, 'content_library', By.LINK_TEXT, 'Content Library', None)
  click_select(5, By.ID, 'content-ownership-books')

# Download items
def download_items():
  # Get pages and download items
  last_page = driver.find_element(By. XPATH, '//div[contains(@id, "pagination")]//a[last()]').text

  # Pages loop
  for num in range(0, int(last_page)):
    # Next Page
    click_select(20, By.XPATH, '//div[contains(@id, "pagination")]//a[contains(@id, "page-' + str(num + 1) + '")]')

    # Get total number of books on first page for looping
    all_books = driver.find_elements(By.XPATH, '//tr[contains(@class, "ListItem-module_row")]')

    # Loop items
    for i in range(len(all_books)):
      # Get title and author
      title = driver.find_element(By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@class, "digital_entity_title")]')
      author = driver.find_element(By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@class, "information_row")]')
      
      # Print title and author
      print(f'{title.text}, by {author.text}')

      print(f'''\
         _______________________________
        |                               \
        |                               |
        |                               |
        |                               |
        |         {title.text}          |
        |                               |
        |         {author.text}         |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        |                               |
        ---------------------------------
''')

      # Click dropdown
      click_select(20, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "dd_title")]')

      # Click transfer item
      click_select(20, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER")]')

      # Choose device
      click_select(20, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//span[contains(@id, "download_and_transfer_list")]')

      #Click download
      click_select(20, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER_ACTION")]/span[text()="Download"]')

      # Close the download notification
      click_select(20, By.ID, 'notification-close')

def main():
  # Log in
  clear_screen()
  login()
  clear_screen()

  # Navigate to content library
  nav_to_content_library()

  # Download items and end process
  download_items()

  # End process
  driver.quit()
  print('Finished')

if __name__ == '__main__':
  main()
