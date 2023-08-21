from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
"""
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
"""
"""
driver.get("https://www.python.org/")
link = driver.find_element(by=By.XPATH, value="/html/body/div[1]/footer/div[2]/div/ul/li[3]/a")
print(link.text)
"""

"""
driver.get("https://www.python.org/")
doc_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.text)
"""

"""
driver.get("https://www.python.org/")
event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)
"""


driver.quit()
