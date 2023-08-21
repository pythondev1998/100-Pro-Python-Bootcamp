import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#JSM_dev1999
#Info de twitter
ACCOUNT_EMAIL = "pythoncodebrian@gmail.com"
ACCOUNT_EMAIL_TWO = "pythondevelopcode@gmail.com"
ACCOUNT_PASSWORD = "" 
ACCOUNT_PHONE = "PythonT66455264"

#Link a utilizar
LINK_SPEEDTEST = "https://www.speedtest.net/es"
LINK_TWITTER = "https://twitter.com/i/flow/login"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

#Const
PROMISED_DOWN = 10
PROMISED_UP = 0.5
SERVICE = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=SERVICE)


#Abrir speed test
#Luego de 45s tomar los valores
#abrir y logearse en twitter
#postear la info tomada


class InternetSpeedTwitterBot:
    def __init__(self, service_arg):
        
        self.driver = webdriver.Chrome(service=service_arg)
        self.down = 0 
        self.up = 0 

    def get_internet_speed(self):
            self.driver.get(LINK_SPEEDTEST) 
            time.sleep(2)

            go_button = self.driver.find_element(By.CLASS_NAME, "start-button")
            go_button.click()

            time.sleep(45)

            download_speed_element = self.driver.find_element(By.CLASS_NAME, "download-speed")  # Find the download speed element
            upload_speed_element = self.driver.find_element(By.CLASS_NAME, "upload-speed")  # Find the upload speed element

            self.down = download_speed_element.text
            self.up = upload_speed_element.text 

            print(f"Download Speed: {self.down}")
            print(f"Upload Speed: {self.up}")

    def tweet_at_provider(self):
        self.driver.get(LINK_TWITTER) 
        time.sleep(4)

        email_input = self.driver.find_element(By.CSS_SELECTOR, "div.css-901oao input")
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)

        phone_input = self.driver.find_element(By.NAME, "text")
        phone_input.clear()
        phone_input.send_keys(ACCOUNT_PHONE)
        phone_input.send_keys(Keys.RETURN)
        time.sleep(2)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(10)
        
        self.driver.get("https://twitter.com/compose/tweet") 
        time.sleep(4)

        tweet_input = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_input.send_keys(tweet)
        tweet_button = self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButton"]')
        tweet_button.click()
       
        time.sleep(50)

bot = InternetSpeedTwitterBot(SERVICE)
bot.get_internet_speed()
bot.tweet_at_provider()

