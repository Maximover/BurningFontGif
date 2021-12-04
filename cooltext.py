from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib
import time
#pip install selenium, webdriver_manager

desiredText = input("Text: ")
desiredFontSize = input("Font size: ")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://cooltext.com/Logo-Design-Burning")
    # XPath
    textInput = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/div[1]/div/form/div[1]/table/tbody/tr[1]/td[2]/textarea')
    imageHandle = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/center[1]/img[1]')
    fontInput = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td[2]/div[1]/div/form/div[1]/table/tbody/tr[3]/td[2]/input')
    textInput.send_keys(desiredText)
    fontInput.send_keys(Keys.CONTROL + 'a')
    fontInput.send_keys(desiredFontSize)
    time.sleep(5)
    imageLink = imageHandle.get_attribute("src")
    #default: save to desktop
    PATHTOSAVE = f"{os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')}\{desiredText}.gif".encode('unicode_escape')
    urllib.request.urlretrieve(imageLink, PATHTOSAVE)
    driver.quit()
    print(f'File {desiredText}.gif was created successfully')
except:
    print(f"An Error Ocurred")
    if driver: driver.quit()
