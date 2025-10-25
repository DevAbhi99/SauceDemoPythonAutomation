from Locators.LogoutLocators import LogoutLocators
from selenium.webdriver.common.by import By


class LogoutPages:

    def __init__(self, driver):
        self.driver=driver
        self.locator=LogoutLocators()

    

    def openMenuElement(self):
        return self.driver.find_element(By.XPATH, self.locator.menuLocator)

    def logoutBtnElement(self):
        return self.driver.find_element(By.XPATH, self.locator.logutBtnLocator)

