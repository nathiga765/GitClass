from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.redbus.in/ ")
driver.maximize_window()
txt_src = driver.find_element_by_id("src")
txt_src.send_keys("Chennai")
txt_des = driver.find_element(By.ID, "dest")
txt_des.send_keys("Madurai")