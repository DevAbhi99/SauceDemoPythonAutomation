from Locators.LoginTestLocators import LoginLocators
from selenium.webdriver.common.by import By

class LoginMainPages:

    def __init__(self, driver):
        self.driver=driver
        self.locator=LoginLocators()

    
    def usernameElement(self):
        return self.driver.find_element(By.XPATH, self.locator.usernameLocator)

    def passwordElement(self):
        return self.driver.find_element(By.XPATH, self.locator.passwordLocator)

    def loginElement(self):
        return self.driver.find_element(By.XPATH, self.locator.loginBtnLocator)

    