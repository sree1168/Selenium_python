
from selenium.webdriver.common.by import By

from utilities.Baseclass import BaseClass

class ThirdPage(BaseClass):

     def __init__(self,driver):
         self.driver = driver

     com = (By.XPATH,"//div[@name='osId']")
     com_sel= (By.XPATH, "//div[contains(text(),'Chrome OS')]")
     ver = (By.XPATH, "//span[@aria-label='Select a Version']")
     ver_sel = (By.XPATH, "//div[contains(text(),'Chrome OS 58')]")
     lan = (By.XPATH,"//div[@placeholder='Select OS language']")
     Select_language= (By.XPATH, "//div[contains(text(),'English')]")
     Brand_= (By.XPATH,"//div[@placeholder='Select Brand']")
     Select_brand= (By.XPATH, "//div[contains(text(),'Orange')]")
     model_= (By.XPATH, "//span[@aria-label='Select a Model']")
     mode_sel= (By.XPATH, "//div[contains(text(),'Rise 53')]")
     OS= (By.XPATH,"//div[@name='handsetOSId']")
     OS_sel= (By.XPATH, "//div[contains(text(),'Android 7.0')]")
     next_button = (By.XPATH,"//a[@aria-label='Next - final step']")



     def computer(self):
         return self.driver.find_element(*ThirdPage.com)

     def computer_selection(self):
        return  self.driver.find_element(*ThirdPage.com_sel)

     def version(self):
         return self.driver.find_element(*ThirdPage.ver)

     def version_selection(self):
         return self.driver.find_element(*ThirdPage.ver_sel)

     def lang(self):
         return self.driver.find_element(*ThirdPage.lan)

     def lang_selection(self):
         return self.driver.find_element(*ThirdPage.Select_language)

     def Brand(self):
         return self.driver.find_element(*ThirdPage.Brand_)

     def Brand_selection(self):
         return self.driver.find_element(*ThirdPage.Select_brand)

     def model(self):
         return self.driver.find_element(*ThirdPage.model_)

     def model_selection(self):
         return self.driver.find_element(*ThirdPage.mode_sel)

     def os(self):
         return self.driver.find_element(*ThirdPage.OS)

     def os_selection(self):
         return self.driver.find_element(*ThirdPage.OS_sel)

     def next_button_third(self):
         return self.driver.find_element(*ThirdPage.next_button)

