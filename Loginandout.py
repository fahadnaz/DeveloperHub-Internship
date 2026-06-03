from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# LOGIN
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

# WAIT FOR DASHBOARD TO LOAD
wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'oxd-topbar-header-breadcrumb')]")))

# CLICK USER DROPDOWN (top-right)
user_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[@class='oxd-userdropdown-tab']"))
)
user_menu.click()

# CLICK LOGOUT
logout_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
)
logout_btn.click()

print("Logout Successful")

driver.quit()