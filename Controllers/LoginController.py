from Pages.LoginPages import LoginMainPages


class LoginMainController:
    def __init__(self, driver):
        self.driver=driver
        self.pages=LoginMainPages(self.driver)

    
    def usernameFill(self, username):
        return self.pages.usernameElement().send_keys(username)
    
    def passwordFill(self, password):
        return self.pages.passwordElement().send_keys(password)

    def loginClick(self):
        return self.pages.loginElement().click()
    

