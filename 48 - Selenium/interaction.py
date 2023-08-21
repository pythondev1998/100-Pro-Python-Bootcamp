import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

"""
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
#article_count.click()

#all_portals = driver.find_element(by=By.LINK_TEXT, value="Wikipedia")

search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
input("Presiona Enter para cerrar el navegador...")
#driver.quit()
"""
driver.get("https://www.facebook.com/%20sign%20up")
search = driver.find_element(By.NAME, "email")
search.send_keys("brian@gmail.com")
search = driver.find_element(By.NAME, "pass")
search.send_keys("1234")

article_count = driver.find_element(by=By.CSS_SELECTOR, value='#loginbutton')
article_count.click()

time.sleep(10)