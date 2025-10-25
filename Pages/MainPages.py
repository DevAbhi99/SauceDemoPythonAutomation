from Locators.MainLocators import MainLocators
from selenium.webdriver.common.by import By  


class MainPages:
    def __init__(self, driver):
        self.driver=driver
        self.locator=MainLocators()


    def addToCartElement(self):
        return self.driver.find_element(By.XPATH, self.locator.addToCartLocator)

    def cartElement(self):
        return self.driver.find_element(By.XPATH, self.locator.cartLocator)

    def checkoutElement(self):
        return self.driver.find_element(By.XPATH, self.locator.checkoutLocator)

    def firstNameElement(self):
        return self.driver.find_element(By.XPATH, self.locator.firstNameLocator)

    def lastNameElement(self):
        return self.driver.find_element(By.XPATH, self.locator.lastNameLocator)

    def postalCodeElement(self):
        return self.driver.find_element(By.XPATH, self.locator.postalCodeLocator)

    def continueElement(self):
        return self.driver.find_element(By.XPATH, self.locator.continueLocator)

    def finishElement(self):
        return self.driver.find_element(By.XPATH, self.locator.finishLocator)

    
        
