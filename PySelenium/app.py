# Selenium is a pk created to create browsere automation
from selenium import webdriver
# after downloaded the driver, we need to put it in the PATH, and tell python the folder where is installed
driver = webdriver.Chrome('/bin/chromedriver')
#browser = webdriver.Chrome()
driver.get("https://github.com")
signin_link = driver.find_element_by_link_text("Sign in")
signin_link.click()

username_box = driver.find_element_by_id("login_field")
username_box.send_keys("Username")
password_box = driver.find_element_by_id("password")
password_box.send_keys("Password")
password_box.submit()

#assert "Grisofandango" in driver.page_source

profile_link = driver.find_elements_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "Username" in link_label

driver.quit
