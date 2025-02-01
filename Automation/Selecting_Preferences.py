from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime, timedelta
#If you encounter an 'unable to import' issue, just ignore it and run the code

'''
#NOTE: This is temporarily commented out as the code is meant to be imported into another file
#Get the absolute path to the chromedriver.exe, because just defining the path to get it to work in a remote repo doesn't work cause we don't know which file will run [future proofing]
script_dir = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(script_dir, '../drivers/chromedriver.exe')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.get('https://www.nlb.gov.sg/seatbooking/')
'''

#Putting all the code in a giant function so I can call it from Login.py
def Selecting_Preferences(driver):
    '''
    Start of code to automate selecting preferences for booking seats
    '''

    #This opens the form for the Library section of the code
    try:
        Library_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-46"))) 
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    Library_Form_Button.click()

    #This selects the library you want
    Library_Form_Button_Library_Choose = driver.find_element(By.XPATH, "//*[contains(text(), 'Bedok Public Library')]") #TODO: Put f-string
    driver.execute_script("arguments[0].scrollIntoView(true);", Library_Form_Button_Library_Choose)
    driver.execute_script("arguments[0].click();", Library_Form_Button_Library_Choose)
    #Please note that depending on how many options you click, the id's of each form choose will change
    #Had to use JavaScript as a div was in the way and Selenium can't run otherwise as a workaround

    #This opens the form for the Area section of the code
    try:
        Area_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-52")))
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    Area_Form_Button.click()

    #This selects the area you want
    Area_Form_Button_Area_Choose = driver.find_element(By.XPATH, """//*[contains(text(), "Teens' Fiction, Level 3")]""") #TODO: Put f-string
    driver.execute_script("arguments[0].scrollIntoView(true);", Area_Form_Button_Area_Choose)
    driver.execute_script("arguments[0].click();", Area_Form_Button_Area_Choose)

    #This opens the form for the Date section of the code
    try:
        Date_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-58")))
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    Date_Form_Button.click()

    Present_Day = datetime.now()
    Tomorrow = Present_Day + timedelta(1)

    try:
        Date_Form_Button_Date_Choose = driver.find_element(By.CLASS_NAME, 'v-btn.v-btn--active.v-btn--rounded.theme--light.primary') #TODO: Test to find out if it works to book next available day (currently set to book first available day)
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    driver.execute_script("arguments[0].scrollIntoView(true);", Date_Form_Button_Date_Choose)
    driver.execute_script("arguments[0].click();", Date_Form_Button_Date_Choose) 

    #I have yet to test it out as that would involve testing after 12 pm
    #I have yet to put the exception when the day is 31, not sur eif it will break or not

    #This opens the form for the Time section of the code
    try:
        Time_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-64")))
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    Time_Form_Button.click()

    #This selects the time you want
    Time_Form_Button_Time_Choose = driver.find_element(By.XPATH, "//*[contains(text(), '6:00 pm')]") #AM/PM has to be lower caps #TODO: Put f-string
    driver.execute_script("arguments[0].scrollIntoView(true);", Time_Form_Button_Time_Choose)
    driver.execute_script("arguments[0].click();", Time_Form_Button_Time_Choose)

    #This opens the form for the Duration section of the code
    try:
        Duration_Form_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input-70")))
    except TimeoutError:
        print("Error: TimeoutError")
        driver.quit()
    Duration_Form_Button.click()

    try:
        Duration_Form_Button_Duration_Choose_List = driver.find_elements(By.XPATH, "//*[contains(text(), '0:30')]")
        Duration_Form_Button_Duration_Choose = Duration_Form_Button_Duration_Choose_List[1]
    except IndexError:
        Duration_Form_Button_Duration_Choose = driver.find_element(By.XPATH, "//*[contains(text(), '0:30')]")
    #TODO: Add more comprehensive error catching
    print(Duration_Form_Button_Duration_Choose)
    driver.execute_script("arguments[0].scrollIntoView(true);", Duration_Form_Button_Duration_Choose)
    driver.execute_script("arguments[0].click();", Duration_Form_Button_Duration_Choose)
    #Depending on what duration the user chooses, there are 2 possible texts due to Time and Duration having the same text

    #TODO: Find a way to split up the booking of time slots
    #TODO: Find a way so that operating hours for different days are accounted for (PH, Weekends, etc)

    #This is the final button to move to choosing seats stage
    Check_Available_Slots = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Check available slots')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", Check_Available_Slots)
    Check_Available_Slots.click() #This is the final button to move to preferences stage

    #Clicking 'Book' in a new page
    Book_Button_First = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "v-icon.notranslate.v-icon--left.mdi.mdi-calendar-check.theme--dark")))
    driver.execute_script("arguments[0].scrollIntoView(true);", Book_Button_First)
    Book_Button_First.click()

    #Clicking 'Seats' in a new page
    Book_Button_Second = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "v-icon.notranslate.mdi.mdi-seat-passenger.theme--light")))
    driver.execute_script("arguments[0].scrollIntoView(true);", Book_Button_Second)
    driver.execute_script("arguments[0].click();", Book_Button_Second)

    #Choosing seats
    Choosing_Seats = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'S67')]"))) #TODO:Insert f-string here make sure 'S' is in caps
    driver.execute_script("arguments[0].scrollIntoView(true);", Choosing_Seats)
    driver.execute_script("arguments[0].click();", Choosing_Seats)

    #Confirm
    Confirm_Seats = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Confirm')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", Confirm_Seats)
    Confirm_Seats.click()

    #OPTIONAL TO RETURN TO STARTING POINT
    Return_To_Start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'New')]")))
    Return_To_Start.click()

