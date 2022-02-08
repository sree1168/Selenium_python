
from selenium.webdriver.common.by import By

from utilities.Baseclass import BaseClass


class FirstPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    Register = (By.XPATH,"//a[contains(text(),'Register')]")
    Firstname = (By.NAME, "firstName")
    Lastname = (By.NAME, "lastName")
    Email = (By.ID,"email")
    #Next_button = (By.CSS_SELECTOR,"div[class*='text-right'] a[class*=btn-blue]")
    Next_button = (By.XPATH,"//a[@ng-click='validateBasicInfoStep(userForm);']")
    DOB_MONTH = (By.ID,"birthMonth")
    DOB_DAY = (By.ID,"birthDay")
    DOB_YEAR = (By.ID,"birthYear")



    def register(self):
        return self.driver.find_element(*FirstPage.Register)

    def firstname(self):
        return self.driver.find_element(*FirstPage.Firstname)

    def lastname(self):
        return self.driver.find_element(*FirstPage.Lastname)

    def email(self):
        return self.driver.find_element(*FirstPage.Email)

    def dob_month(self):
        return self.driver.find_element(*FirstPage.DOB_MONTH)

    def dob_day(self):
        return self.driver.find_element(*FirstPage.DOB_DAY)

    def dob_year(self):
        return self.driver.find_element(*FirstPage.DOB_YEAR)


    def next_button(self):
        return self.driver.find_element(*FirstPage.Next_button)

