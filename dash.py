from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

assert "OrangeHRM" in driver.title

print("Dashboard Test Passed")

driver.quit()