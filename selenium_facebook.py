# log in your facebook and post

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.facebook.com/' 
driver.get(url) 

elements = driver.find_element_by_id('email')
user_name = "*************"  #replace your email address
elements.send_keys(user_name)
elements = driver.find_element_by_id('pass')
password = "*******" #replace your password
elements.send_keys(password)


c = driver.find_element_by_id("loginbutton")
c.click()


# post messager=================================
driver.get("....................") #replace your personal page web
post_box=driver.find_element_by_class_name(" _5yk1")
post_box.click()
post_box=driver.find_element_by_class_name(" _5yk2")
post_box.send_keys("Test Post by Selenium!!")


post_it=driver.find_elements_by_tag_name("button")
post_it[5].click()

