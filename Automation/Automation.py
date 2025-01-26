from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

'''
If you encounter an 'unable to import' issue, just ignore it and run the code
'''

# Get the absolute path to the chromedriver.exe, because just defining the path to get it to work in a remote repo doesn't work cause we don't know which file will run [future proofing]
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, '../drivers/chromedriver.exe')

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.nlb.gov.sg/seatbooking/')

WebDriverWait(driver).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]")))
WebDriverWait(driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'my-2')))

Library_And_Area_Buttons = driver.find_elements(By.CLASS_NAME, 'my-2')
for button in Library_And_Area_Buttons:
    if button.text == 'Name': #For testing purposes, PLEASE change the name of the library with a variable 9IDK how to do that yet
        button.click()
        break




