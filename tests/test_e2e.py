import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from PageObjects.Second_page import SecondPage
from PageObjects.first_page import FirstPage
from PageObjects.third_page import ThirdPage

from utilities.Baseclass import BaseClass


class Testone(BaseClass):

    def test_e2e(self):

        log = self.Getlogger()
        log.info("Registering first user")
        first = FirstPage(self.driver)
        #first page
        first.register().click()
        print(self.driver.title)
        self.driver.implicitly_wait(10)
        first.firstname().send_keys("Sree")
        log.info("Entered firstname")
        first.lastname().send_keys("devi")
        log.info("Entered lastname")
        first.email().send_keys("Sree34334@gmail.com")
        log.info("Entered email")
        self.Selectdropdown_by_text(first.dob_month(), "December")
        self.Selectdropdown_by_value(first.dob_day(), "number:17")
        self.Selectdropdown_by_value(first.dob_year(), "number:1992")
        log.info("Entered DOB")
        self.Scrolling_down(first.next_button())
        log.info("going to next")
        self.verify_element_presence(first.Next_button)
        self.action_on_element(first.next_button())
        #first.next_button().click()
        log.info("clicked next")

        #second page
        second = SecondPage(self.driver)
        second.city_name().send_keys("palakkad")
        second.zip_num().send_keys("679503")
        Country= second.country_name()
        self.verify_element_presence(Country)
        print(Country)
        self.Scrolling_down(second.nextbutton())
        log.info("going to next")
        self.verify_element_presence(second.Next_button)
        self.action_on_element(second.nextbutton())



        #third page

        third= ThirdPage(self.driver)
        self.verify_element_presence(third.com)
        log.info("clicking OS")
        third.computer().click()
        third.computer_selection().click()

        third.version().click()
        third.version_selection().click()

        third.lang().click()
        language= third.lang_selection()
        self.action_on_element(language)
        #self.verify_element_presence(third.Select_language).click()

        self.action_on_element(third.Brand())
        #bran = third.Brand().click()
        #bran.send_keys("Orange")
        self.verify_element_presence(third.Select_brand)
        brand = third.Brand_selection()
        self.action_on_element(brand)

        third.model().click()
        third.model_selection().click()

        third.os().click()
        third.os_selection().click()

        third.next_button_third().click()

"""
        #page 4
        self.driver.find_element(By.NAME, "password").send_keys("Sreedevi@1168")
        self.driver.find_element(By.NAME, "confirmPassword").send_keys("Sreedevi@1168")

        checkbox1 = self.driver.find_element(By.CSS_SELECTOR,"span[class*='signup-consent__checkbox--highlight']").click()
        #print(checkbox1.is_selected())

        self.driver.find_element(By.CSS_SELECTOR,"main.registration section.col-md-8.col-lg-8.col-sm-12.col-xs-12:nth-child(3) div.container-fluid div.sign-up-form-container div.ui-view div:nth-child(1) form.form-group-box.user-form.ng-invalid.ng-invalid-required.ng-valid-minlength.ng-valid-maxlength.ng-valid-validation-match.ng-dirty.ng-valid-parse:nth-child(1) div.row.col-xs-12:nth-child(5) label.input-check-box.signup-consent > span.checkmark.signup-consent__checkbox.error:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR,"main.registration section.col-md-8.col-lg-8.col-sm-12.col-xs-12:nth-child(3) div.container-fluid div.sign-up-form-container div.ui-view div:nth-child(1) form.form-group-box.user-form.ng-invalid.ng-invalid-required.ng-valid-minlength.ng-valid-maxlength.ng-valid-validation-match.ng-dirty.ng-valid-parse:nth-child(1) div.row.col-xs-12:nth-child(6) label.input-check-box.signup-consent > span.checkmark.signup-consent__checkbox.error:nth-child(3)").click()

        element_last = self.driver.find_element(By.XPATH,"//a[@aria-label='Complete Setup']")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element_last)
        time.sleep(5)
        element_last.click()

        #success
        time.sleep(3)
        actual_msg = self.driver.find_element(By.XPATH, "//div[@class='image-box-header']/h1")
        Success_msg= "Welcome to the world's largest community of freelance software testers!"


        if actual_msg.text == Success_msg:
            print("Successful Registration")
        else:
            print("Registration failed")"""
