import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#JSM_dev1999
#Info de twitter
ACCOUNT_USERNAME = "JSM_dev1999"
ACCOUNT_PASSWORD = "" 
SIMILAR_ACCOUNT = "cheddnoir"

#Link a utilizar
LINK_INSTAGRAM_LOGIN = "https://www.instagram.com/accounts/login/"
LINK_INSTAGRAM_FIND = "https://www.instagram.com/cheddnoir/followers/"

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SERVICE = Service(CHROME_DRIVER_PATH)

class InstaFollower:
    def __init__(self, service_arg):
        self.driver = webdriver.Chrome(service=service_arg)

    def login(self):
        self.driver.get(LINK_INSTAGRAM_LOGIN) 
        time.sleep(2)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(ACCOUNT_USERNAME)
        username_input.send_keys(Keys.RETURN)
        time.sleep(2)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)

    def find_followers(self):
        self.driver.get(LINK_INSTAGRAM_FIND) 
        time.sleep(2)

        follower_link = self.driver.find_element(By.CSS_SELECTOR, 'li.xl565be a.x1i10hfl')
        follower_link.click()
        time.sleep(2)
    
    def follow(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(2)

        div_element = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_element)
            time.sleep(2)
            
        self.buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')
        
        print(f"Found {len(self.buttons)} buttons")
        time.sleep(2)

        for button in self.buttons:
            button.click()
            time.sleep(1)

        time.sleep(400)


bot = InstaFollower(SERVICE)
bot.login()
#bot.find_followers()
bot.follow()


