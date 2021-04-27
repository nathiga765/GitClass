from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.swiggy.com/")
driver.maximize_window()
loc = driver.find_element(By.NAME, "location")
loc.send_keys("Neelangarai")