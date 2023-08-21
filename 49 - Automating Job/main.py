import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
PHONE = ""
ENLACE = "https://www.linkedin.com/jobs/search/?currentJobId=3616837314&distance=25.0&f_AL=true&f_WT=2&geoId=105057336&keywords=Python%20Developer"

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(ENLACE)
time.sleep(2)
# 0. Logearse 

def sign_up():
    button = driver.find_element(by=By.CSS_SELECTOR, value=".cta-modal__primary-btn.btn-md.btn-primary.inline-block.w-full.mt-3")
    button.click()
    time.sleep(2)

    input_name = driver.find_element(By.NAME, "session_key")
    input_name.send_keys(ACCOUNT_EMAIL)

    input_password = driver.find_element(By.NAME, "session_password")
    input_password.send_keys(ACCOUNT_PASSWORD)
    time.sleep(2)

    button2 = driver.find_element(by=By.CSS_SELECTOR, value=".btn__primary--large.from__button--floating")
    button2.submit()
    time.sleep(5)

def form():
    time.sleep(5)
    button3 = driver.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Easy Apply to Backend Developer (Nodejs and Ruby on Rails) at Applaudo"]')
    button3.click()
    time.sleep(2)

    input_number = driver.find_element(by=By.ID, value='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3616837314-1907077533479924862-phoneNumber-nationalNumber')
    input_number.send_keys(PHONE)

sign_up()
form()