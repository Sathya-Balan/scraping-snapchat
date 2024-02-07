from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


# service = Service(executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service)#,options=options)

# # release the resources allocated by Selenium and shut down the browser
# driver.quit()

# driver = webdriver.Chrome()
# time.sleep(5)
# wait = WebDriverWait(driver, 5)
# driver.get("https://www.snapchat.com/explore/kane")

# time.sleep(10)

# from selenium import webdriver

# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome()

# Open the desired URL
# driver.get("https://www.snapchat.com/explore/kane")

# Get the current URL
# current_url = driver.current_url
# print(current_url)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# from selenium import webdriver
# driver = webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

ser = Service(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
driver = webdriver.Chrome(service=ser)

wait = WebDriverWait(driver, 10)

driver.get("https://www.snapchat.com/")

wait = WebDriverWait(driver, 10)

driver.quit()