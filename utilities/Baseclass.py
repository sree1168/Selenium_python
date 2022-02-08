import inspect
import time

import pytest
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def Getlogger(self):
        logger = logging.getLogger(inspect.stack()[1][3])
        filehandler = logging.FileHandler('UTest_log.txt')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


    def verify_element_presence(self,value):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(value))

    def Selectdropdown_by_value(self,locator,value):
        sel = Select(locator)
        sel.select_by_value(value)

    def Selectdropdown_by_text(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def Scrolling_down(self,element):

        #self.driver.execute_script("window.scrollTo(0, 30)")
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def some_wait(self,time_millisecond):
        time.sleep(time_millisecond)

    def action_on_element(self,element):
        action = ActionChains(self.driver)
        action.move_to_element(element).click(element)
        action.perform()

