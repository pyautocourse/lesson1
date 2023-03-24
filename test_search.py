# test to check "One way to generate test cases automatically" in wikipedia
from selenium import webdriver
from selenium.webdriver.common.by import By

# open browser
driver = webdriver.Chrome()

# open wikipedia
driver.get("https://en.wikipedia.org/")
driver.implicitly_wait(5)

# enter Test automation in search field
search_field = driver.find_element(By.NAME, 'search')
search_field.send_keys("Test automation")

# click on search button
search_button = driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button')
search_button.click()

# verify "text" on search page
assert "One way to gene1rate test cases automatically" in driver.page_source