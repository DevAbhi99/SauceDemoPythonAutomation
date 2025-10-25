from Pages.LogoutPages import LogoutPages


class LogoutController:

    def __init__(self, driver):
        self.driver=driver
        self.page=LogoutPages(self.driver)

    def openMenuClick(self):
        return self.page.openMenuElement().click()

    def logoutBtnClick(self):
        return self.page.logoutBtnElement().click()