import keyboard as keyboard
# from selenium import webdriver
from selenium.webdriver import ActionChains
import keyboard
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
txt_username = driver.find_element(By.ID, "email")
txt_username.send_keys("2345678")
txt_password = driver.find_element(By.ID, "pass")
txt_password.send_keys("Hello@123")




