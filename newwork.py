from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
import pandas as pd
import time
import csv

#initializing brave browser
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
options = webdriver.ChromeOptions()
options.binary_location = brave_path
# Store the website link in a variable
url = 'https://www.insiderbiz.in/company-list/?page=1'

# Initialize the Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Open the website link
driver.get(url)

# Maximize the window
driver.maximize_window()

# Define the CSV file path
csv_file_path = 'company_scraping.csv'

# Write the header row in the CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['CIN', 'Company_Name', 'ROC', 'Address'])

for k in range(10):
    # Locator for the first column of the table
    cins = driver.find_elements(By.XPATH, '//*[@id="WebGrid"]/tbody/tr/td[1]')

    # Locator for the second column of the table
    company_name = driver.find_elements(By.XPATH, '//*[@id="WebGrid"]/tbody/tr/td[2]')

    # Locator for the third column of the table
    roc = driver.find_elements(By.XPATH, '//*[@id="WebGrid"]/tbody/tr/td[3]')

    # Locator for the fourth column of the table
    address = driver.find_elements(By.XPATH, '//*[@id="WebGrid"]/tbody/tr/td[4]')
    time.sleep(6)

    # Scroll the window to load more data (if necessary)
    driver.execute_script("window.scrollBy(0,500)")

    # Write the data rows in the CSV file
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(cins)):
            writer.writerow([cins[i].text, company_name[i].text, roc[i].text, address[i].text])

    try:
        next_button = driver.find_element(By.XPATH, '//*[@id="WebGrid"]/tfoot/tr/td/a[6]')
    except NoSuchElementException:
        next_button = driver.find_element(By.XPATH, '//*[@id="WebGrid"]/tfoot/tr/td/a[5]')
    
    next_button.click()

driver.close()
