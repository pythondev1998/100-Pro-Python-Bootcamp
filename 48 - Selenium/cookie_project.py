import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")

def lang_select():
    lang_select_button = driver.find_element(By.ID, "langSelect-EN")
    lang_select_button.click()    

def click_cookie():
      big_cookie_button = driver.find_element(By.ID, "bigCookie")
      big_cookie_button.click()

def score_res():
    cookie_score = driver.find_element(By.ID, "cookies")
    value = cookie_score.text.split()[0]
    return value

#Items de la tienda
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes
"""
while True:
    #Dar click
    click_cookie()

    if time.time() > timeout:

   
    
    #Temporizador revisa cada cinco segundo lo siguiente
        #Si value es mayor al producto entonces 
        #Compramelo
        #Continua

#Son dos mejoras. Hacer una lista de ellos all elements
#Son cuatro productos. Hacer una lista de ellos all elements
#Verificar si mi value es mayor a algun elemento
#Si es asi entonces tomar ese elemento y darle click
#Este programa recorrar durante cinco minutos por lo que necesitamos un timer de 5

"""
