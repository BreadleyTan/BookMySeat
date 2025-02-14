import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#If you encounter an 'unable to import' issue, just ignore it and run the code
import Selecting_Preferences


#Get the absolute path to the chromedriver.exe, because just defining the path to get it to work in a remote repo doesn't work cause we don't know which file will run [future proofing]
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, '../drivers/chromedriver.exe')

# Set Chrome options to enable headless mode, basically running the script without opening a browser window
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU acceleration
chrome_options.add_argument("--window-size=1920,1080")  # Optional: Set window size

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.nlb.gov.sg/seatbooking/') #Code starts from this landing page so integrating it into code will be easier

#First, before we log in to the correct account, we need to get to the login page, and logoout if it is logged in
try:
    Logout_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "v-icon.notranslate.v-icon--link.mdi.mdi-login-variant.theme--dark")))
    Logout_Button.click() 
except NoSuchElementException: #Means the current seat booking page is logged in as a user
    Account_Button = driver.find_elements(By.XPATH, "//*[contains(text(), 'Account')]")
    Account_Button[0].click() #Goes to the account page, the only way to log out
    Logout_Button = driver.find_element(By.CLASS_NAME, "v-icon.notranslate.mdi.mdi-logout-variant.theme--dark")
    driver.execute_script("arguments[0].click();", Logout_Button)

#Filling in user info
try:
    Username_Field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "username")))
    Username_Field.send_keys(Username + Keys.ENTER) #TODO: Change variable
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()
try:
    Username_Field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password")))
    Username_Field.send_keys(Password + Keys.ENTER) #TODO: Change variable
except TimeoutError:
    print("Error: TimeoutError")
    driver.quit()


Selecting_Preferences.Selecting_Preferences(driver)
#NOTE: If you wanna allow for switching out of choosing seat preferences, please remember to add mroe variables in the line above
