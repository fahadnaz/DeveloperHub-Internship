from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("admin123")

login_btn = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
login_btn.click()

print("Login Test Passed")

driver.quit()