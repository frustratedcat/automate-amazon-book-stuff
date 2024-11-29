from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from getpass import getpass
import os

# Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Start up and connect
clear_screen()
print('Starting up. Please wait...\n')
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.page_load_strategy = 'eager'
driver = webdriver.Firefox(options=options)
driver.get("https://wwww.amazon.com")

# Get username
def get_username():
    username = input('Please enter your username\n>')
    return username.strip()

# Get password
def get_password():
    password = getpass('Please enter your password\n>')
    return password.strip()

# Get 2FA
def get_two_factor():
    two_factor = input('Please enter your 2FA\n>')
    return two_factor.strip()

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
    try:
        click_select(20, By.ID, 'nav-link-accountList')
        input_select(20, 'input_email', By.ID, 'ap_email', get_username())
        input_select(20, 'input_password', By.ID, 'ap_password', get_password())

        # Check for 2FA
        if driver.find_element(By.ID, 'auth-mfa-otpcode'):
            input_select(20, 'input_two_factor', By.ID, 'auth-mfa-otpcode', get_two_factor())

    except NoSuchElementException:
        print('There was a problem loading the page, please run the application again\n')

# Nav to content library
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

            try:
                # Get title and author
                title = driver.find_element(By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@class, "digital_entity_title")]')
                author = driver.find_element(By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@class, "information_row")]')

                # Print title and author
                print(f'{title.text}, by {author.text}')

                # Click dropdown
                click_select(5, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "dd_title")]')

                # Click transfer item
                click_select(5, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER")]')

                # Choose device
                click_select(5, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//span[contains(@id, "download_and_transfer_list")]')

                #Click download
                click_select(5, By.XPATH, '//tr[contains(@class, "ListItem-module_row")][' + str(i + 1) + ']//div[contains(@id, "DOWNLOAD_AND_TRANSFER_ACTION")]/span[text()="Download"]')

                # Close the download notification
                click_select(5, By.ID, 'notification-close')

            except NoSuchElementException:
                print('Skipping digital library loan...\n')
    print('--------\nFinished')


# Download the content library
def content_library_download():
    # Navigate to content library
    nav_to_content_library()
    # Download items and end process
    download_items()

# Nav to book list
def nav_to_book_list():
    click_select(100, By.ID, 'nav-link-accountList')
    click_select(5, By.XPATH, '//a[contains(@class, "ya-card__whole-card-link")]/div/div/div/div[2]/h2[contains(text(), "Your Lists")]')
    click_select(5, By.XPATH, '//span[@id="wl-list-entry-title-3D1X5QSJD5ZZN"]')

# Click Filter & Sort dropdown
def filter_for_price():
    click_select(5, By.ID, 'filter-and-sort')
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//span[@id="sort-price-asc-label"]')))
    click_select(5, By.XPATH, '//span[@id="sort-price-asc-label"]')

    # Get list of items
    driver.implicitly_wait(5)
    item_list = driver.find_elements(By.XPATH, '//li[contains(@class, "g-item-sortable")]')

    # Loop through items and get data
    clear_screen()
    print('Showing Cheapest Books\n----------------------')
    for i in range(1, len(item_list)):
        item_price_sign = driver.find_element(By.XPATH, '//li[contains(@class, "g-item-sortable")][' + str(i) + ']/span/div/div/div/div[2]/div[3]/div/div/div/div/div/div/div[contains(@class, "price-section")]/span/span[2]/span[1]')
        item_price_whole = driver.find_element(By.XPATH, '//li[contains(@class, "g-item-sortable")][' + str(i) + ']/span/div/div/div/div[2]/div[3]/div/div/div/div/div/div/div[contains(@class, "price-section")]/span/span[2]/span[2]')
        item_price_fraction = driver.find_element(By.XPATH, '//li[contains(@class, "g-item-sortable")][' + str(i) + ']/span/div/div/div/div[2]/div[3]/div/div/div/div/div/div/div[contains(@class, "price-section")]/span/span[2]/span[3]')
            
        item_price = item_price_sign.text + item_price_whole.text + item_price_fraction.text
        item_title = driver.find_element(By.XPATH, '//li[contains(@class, "g-item-sortable")][' + str(i) + ']/span/div/div/div/div[2]/div[3]/div/div/div/div/div[2]/h2/a')
        item_author = driver.find_element(By.XPATH, '//li[contains(@class, "g-item-sortable")][' + str(i) + ']/span/div/div/div/div[2]/div[3]/div/div/div/div/div[2]/span')

        print(f'Price: {item_price} | Author: {item_author.text} | Title: {item_title.text}')
    print('--------\nFinished')


# Get book list prices
def get_book_list_prices():
    print('Gathering data...')
    # Navigate to book list
    nav_to_book_list()
    # Print list from prce low to high
    filter_for_price()

def main():
    try:
        # Log in
        clear_screen()
        login()
        clear_screen()

        get_choice = input('Would you like to?\n1: Download Book Library\n2: Check Book List Prices\n(Type "1" or "2")> ')
        try:
            if get_choice == "1":
                clear_screen()
                content_library_download()
            else:
                clear_screen()
                get_book_list_prices()
        except ValueError:
            print('Invalid input...')

    finally:
        # End process
        driver.quit()

if __name__ == '__main__':
    main()
