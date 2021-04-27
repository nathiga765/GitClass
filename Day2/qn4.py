from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
driver.get("https://infinity.icicibank.com/corp/Login.jsp")
driver.maximize_window()
due to security reason the site will not allow the right click