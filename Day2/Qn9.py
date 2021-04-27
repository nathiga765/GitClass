# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\py37\Driver\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.irctc.co.in/")
# driver.maximize_window()
# row=int(input("Enter a Row:"))
# for i in range(1,row+1):
#      for j in range(1,i+1):
#        print(j, end="  ")
#      print()
string = input("enter a string:")
if(string == string[::-1]):
    print("it is a palindrome ")
else:
    print("it is not a palindrome")