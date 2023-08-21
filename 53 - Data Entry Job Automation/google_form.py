import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleFormSubmitter:
    def __init__(self, data, lon):
        self.data = data
        self.lon = lon
        self.MY_EMAIL = "pythondevelopcode@gmail.com"
        self.MY_PASSWORD = ""
        self.CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
        self.GOOGLE_FORM_PATH = "https://docs.google.com/forms/d/e/1FAIpQLSf2emJ-qJDXXAzQL5jvvwqZoKGgeGdwP4FHAo_OzQsNXvlZlQ/viewform?usp=sf_link"
        self.service = Service(self.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 10)
        
    def submit_form(self):
        for i in range(self.lon):
            self.driver.get(self.GOOGLE_FORM_PATH)
            time.sleep(2)

            list_container = self.driver.find_element(By.XPATH, '//div[@class="o3Dpx"]')
            list_items = list_container.find_elements(By.XPATH, './/div[@class="Qr7Oae"]')

            input_element = list_items[0].find_element(By.XPATH, './/input[@class="whsOnd zHQkBf"]')
            input_element.clear()
            input_element.send_keys(self.data['prices'][i])

            input_element = list_items[1].find_element(By.XPATH, './/input[@class="whsOnd zHQkBf"]')
            input_element.clear()
            input_element.send_keys(self.data['addresses'][i])

            input_element = list_items[2].find_element(By.XPATH, './/input[@class="whsOnd zHQkBf"]')
            input_element.clear()
            input_element.send_keys(self.data['urls'][i])

            time.sleep(2)

            button = self.driver.find_element(By.XPATH, '//span[@class="NPEfkd RveJvd snByac"]')
            button.click()
            
            time.sleep(2)
            self.driver.refresh()

        self.driver.quit()


            

