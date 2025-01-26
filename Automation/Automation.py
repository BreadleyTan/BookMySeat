from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
If you encounter an 'unable to import' issue, just ignore it and run the code
'''

service = Service('../drivers/chromedriver.exe')
drivers = webdriver.Chrome(service=service)

drivers.get('https://www.google.com')

