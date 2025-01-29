from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, timedelta
#If you encounter an 'unable to import' issue, just ignore it and run the code



import time



#Get the absolute path to the chromedriver.exe, because just defining the path to get it to work in a remote repo doesn't work cause we don't know which file will run [future proofing]
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, '../drivers/chromedriver.exe')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.nlb.gov.sg/seatbooking/')

'''
Start of code to automate sleecting preferences for booking seats
'''

#This opens the form for the Library section of the code
try:
    Library_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-46"))) #Put f-string and switch out with test variable here
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()
Library_Form_Button.click()

#This selects the library you want
Library_Form_Button_Library_Choose = driver.find_element(By.ID, "input-90") #Put f-string and switch out with test variable here
driver.execute_script("arguments[0].click();", Library_Form_Button_Library_Choose)
#Had to use JavaScript as a div was in the way and Selenium can't run otherwise

'''
Please note that depending on how many options you click, the id's of each form changes, making life exponentially more difficult
'''

#This opens the form for the Area section of the code
try:
    Area_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-52"))) #See Library_Form_Button
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()
Area_Form_Button.click()

#This selects the area you want
Area_Form_Button_Area_Choose = driver.find_element(By.ID, "input-146") #See Library_Form_Button_Library_Choose
driver.execute_script("arguments[0].click();", Area_Form_Button_Area_Choose) #See Library_Form_Button_Library_Choose

'''
try:
    Date_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-58"))) #See Library_Form_Button
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()


Present_Day = datetime.now()
Tomorrow = Present_Day + timedelta(1)

Date_Form_Button_Date_Choose = driver.find_element(By.NAME, str(Tomorrow.day))
'''

#I have yet to test it out as that would involve testing after 12 pm
#I have yet to put the exception when the day is 31, not sur eif it will break or not

try:
    Duration_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-70"))) #See Library_Form_Button
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()
Duration_Form_Button.click()


#TODO: Find a way to split up the booking of time slots

time.sleep(5)

#Area_Form_Button = driver.find_element(By.ID, "input-52") #This is the button that opens the form for the Area section of the code