from Pages.LoginTestPages import LoginPages


class LoginController:
    def __init__(self, driver):
        self.driver=driver
        self.page=LoginPages(self.driver)


    def usernameFill(self, username):
        self.page.usernameElement().send_keys(username)


    def passwordFill(self, password):
        self.page.passwordElement().send_keys(password)

    def loginClick(self):
        self.page.loginBtnElement().click()
        
