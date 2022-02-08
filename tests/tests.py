import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.utest.com/articles/best-websites-to-practice-test-automation-using-selenium-webdriver")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
time.sleep(3)
driver.find_element(By.NAME, "firstName").send_keys("Sreedevi")
driver.find_element(By.NAME, "lastName").send_keys("Unnikrishnan")
driver.find_element(By.ID, "email").send_keys("sreedvi522168@gmail.com")
DOB_MONTH = Select(driver.find_element(By.ID, "birthMonth"))
DOB_MONTH.select_by_visible_text("December")
DOB_DAY = Select(driver.find_element(By.ID, "birthDay"))
DOB_DAY.select_by_value("number:17")
DOB_YEAR = Select(driver.find_element(By.ID, "birthYear"))
DOB_YEAR.select_by_value("number:1992")

# driver.execute_script("window.scrollTo(0, 30)")

element = driver.find_element(By.CSS_SELECTOR, "div[class*='text-right'] a[class*=btn-blue]")
driver.execute_script("return arguments[0].scrollIntoView(true);", element)
time.sleep(5)
element.click()