import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/es")

# Constantes
MY_EMAIL = "pythondevelopcode@gmail.com"
MY_PASSWORD = ""

# 1. Botón de iniciar sesión
button_element = driver.find_element(By.XPATH, '//a[@href="https://tinder.onelink.me/9K8a/3d4abb81"]')
button_element.click()
time.sleep(4)

button_elemen2t = driver.find_element(By.XPATH, value='//div[text()="Iniciar sesión con Facebook"]')
button_elemen2t.click()

time.sleep(4)
# Esperar hasta que el campo de entrada esté visible
input_email = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "email"))
)
input_email.send_keys(MY_EMAIL)
time.sleep(1)
input_pass = driver.find_element(By.NAME, value="pass")
input_pass.send_keys(MY_PASSWORD)

time.sleep(2)
button_enter = driver.find_element(By.NAME, "login")
button_enter.submit()

time.sleep(1000)
