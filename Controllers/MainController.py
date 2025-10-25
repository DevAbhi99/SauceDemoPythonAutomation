from Pages.MainPages import MainPages


class MainController:
    def __init__(self, driver):
        self.driver=driver
        self.page=MainPages(self.driver)

    def addToCartClick(self):
        return self.page.addToCartElement().click()

    def cartClick(self):
        return self.page.cartElement().click()

    def checkoutClick(self):
        return self.page.checkoutElement().click()

    def firstNameFill(self, firstname):
        return self.page.firstNameElement().send_keys(firstname)

    def lastNameFill(self, lastname):
        return self.page.lastNameElement().send_keys(lastname)

    def postalCodeFill(self, postalcode):
        return self.page.postalCodeElement().send_keys(postalcode)
    
    def continueClick(self):
        return self.page.continueElement().click()

    def finishClick(self):
        return self.page.finishElement().click()