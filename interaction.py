import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'D:\!Install!\!Drivers!\chromedriver.exe'
service = Service(chrome_driver_path)
browser = webdriver.Chrome(service=service)


browser.get('https://secure-retreat-92358.herokuapp.com')
first_name_input_field = browser.find_element(By.NAME, 'fName')
first_name_input_field.send_keys('Ivan')
last_name_input_field = browser.find_element(By.NAME, 'lName')
last_name_input_field.send_keys('Sl')
email_input_field = browser.find_element(By.NAME, 'email')
email_input_field.send_keys('sjkdfjxcvvnmz1234812xjkscyy182@gmail.com')
sign_up_button = browser.find_element(By.TAG_NAME, 'button')
sign_up_button.click()

# browser.quit()


