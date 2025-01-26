from selenium import webdriver
from selenium.webdriver.chrome.service import Service #there is a error, but I don't know why it cannot seem to import
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #This is so that code won't trigger in case page doesn't load (internet connection lost or CAPTCHA)
from selenium.webdriver.support import expected_conditions as EC