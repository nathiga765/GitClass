from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
# driver.implicitly_wait(10)
driver.maximize_window()
txt_src = driver.find_element(By.ID,"twotabsearchtextbox")
txt_src.send_keys("iphone",Keys.ENTER)
mobile= driver.find_element(By.XPATH,"//span[text()='New Apple iPhone 12 Mini (64GB) - Green']")
mobile.click()
par_id = driver.current_window_handle
# print(par_id)
all_window_id = driver.window_handles
# print(all_window_id)
for each_window_id in all_window_id:
    if par_id != each_window_id:
        driver.switch_to.window(each_window_id)
cart = driver.find_element(By.ID, "add-to-cart-button")
cart.click()
cancel = driver.find_element(By.ID, "attach-close_sideSheet-link")
cancel.click()
driver.switch_to.window(all_window_id[0])
driver.back()
txt_src = driver.find_element(By.ID,"twotabsearchtextbox")
txt_src.send_keys("samsung",Keys.ENTER)
samsung = driver.find_element(By.XPATH, "//span[text()='Samsung Galaxy M51 (Electric Blue, 6GB RAM, 128GB Storage)']")
samsung.click()
par_id = driver.current_window_handle
# print(par_id)
all_window_id = driver.window_handles
# print(all_window_id)
for each_window_id in all_window_id:
    if par_id != each_window_id:
        driver.switch_to.window(each_window_id)
cart = driver.find_element(By.ID, "add-to-cart-button")
cart.click()

# t = driver.find_element(By.XPATH, "//span[text()='₹ 90,099.00']")
# k = t.text
# print(k)
cancel = driver.find_element(By.ID, "attach-close_sideSheet-link")
cancel.click()
driver.switch_to.window(all_window_id[0])
driver.back()
txt_src = driver.find_element(By.ID,"twotabsearchtextbox")
txt_src.send_keys("watch",Keys.ENTER)
watch = driver.find_element(By.XPATH, "//span[text()='Carlson Raulen']")
watch.click()
par_id = driver.current_window_handle
# print(par_id)
all_window_id = driver.window_handles
# print(all_window_id)
for each_window_id in all_window_id:
    if par_id != each_window_id:
        driver.switch_to.window(each_window_id)
cart = driver.find_element(By.ID, "add-to-cart-button")
cart.click()
cancel = driver.find_element(By.ID, "attach-close_sideSheet-link")
cancel.click()
driver.switch_to.window(all_window_id[0])
driver.back()
txt_src = driver.find_element(By.ID,"twotabsearchtextbox")
txt_src.send_keys("earring",Keys.ENTER)
earing = driver.find_element(By.XPATH, "(//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'])[2]")
earing.click()
par_id = driver.current_window_handle
# print(par_id)
all_window_id = driver.window_handles
# print(all_window_id)
for each_window_id in all_window_id:
    if par_id != each_window_id:
        driver.switch_to.window(each_window_id)
cart = driver.find_element(By.ID, "add-to-cart-button")
cart.click()
cancel = driver.find_element(By.ID, "attach-close_sideSheet-link")
cancel.click()
driver.switch_to.window(all_window_id[0])
driver.back()
txt_src = driver.find_element(By.ID,"twotabsearchtextbox")
txt_src.send_keys("womens wallet",Keys.ENTER)
wallet = driver.find_element(By.XPATH, "(//span[text()='PALAY'])[1]")
wallet.click()
par_id = driver.current_window_handle
# print(par_id)
all_window_id = driver.window_handles
# print(all_window_id)
for each_window_id in all_window_id:
    if par_id != each_window_id:
        driver.switch_to.window(each_window_id)
cart = driver.find_element(By.ID, "add-to-cart-button")
cart.click()
t = driver.find_element(By.XPATH, "//span[text()='₹ 1,59,096.00']")
k = t.text
print(k)











