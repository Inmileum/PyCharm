

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  #importovana podesavanja hroma, da bi omogucili iskljucivanje notifikacija#
import time

option1 = Options()                             #metod za iskljucivajne notifikacija browsera
option1.add_argument("--disable-notifications")

user_name = "milemarceticedu@gmail.com"
password = "mmed1245"

driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver", chrome_options=option1)
driver.get("http://www.facebook.com")
element = driver.find_element_by_xpath("//*[@id='email']")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element = driver.find_element_by_name("login")
element.click()
time.sleep(10)
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]")
element.click()

