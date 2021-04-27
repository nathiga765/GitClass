from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/ ")
driver.maximize_window()
customer_id = driver.find_element(By.XPATH, "//input[@type='text']")
customer_id.send_keys("pavithra")
name is not entering the webpage