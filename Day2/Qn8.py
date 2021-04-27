from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.instagram.com/accounts/login/?hl=en) login page ")
driver.maximize_window()
txt_user = driver.find_element(By.XPATH,"//input[@type='text']")
txt_user.send_keys("23456789")
txt_pass = driver.find_element(By.NAME, "password")
txt_pass.send_keys("pavi@123")
not entering these inputs