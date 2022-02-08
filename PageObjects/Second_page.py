
from selenium.webdriver.common.by import By

from utilities.Baseclass import BaseClass

class SecondPage(BaseClass):

     def __init__(self,driver):
         self.driver = driver

     city = (By.NAME,"city")
     zip = (By.XPATH, "//input[@id='zip']")
     country = (By.XPATH, "//span[contains(text(),'India')]")
     Next_button = (By.XPATH,"//span[contains(text(),'Next: Devices')]")

     def city_name(self):
         return self.driver.find_element(*SecondPage.city)

     def zip_num(self):
         return self.driver.find_element(*SecondPage.zip)

     def country_name(self):
         return self.driver.find_element(*SecondPage.country)

     def nextbutton(self):
         return self.driver.find_element(*SecondPage.Next_button)