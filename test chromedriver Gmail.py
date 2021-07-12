from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "milemarceticedu@gmail.com"
password = "mmed1245"
driver = webdriver.Chrome(executable_path="c:\selenium browser drivers\chromedriver")
driver.get("http:\\www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()


