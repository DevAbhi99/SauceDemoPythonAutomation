from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Controllers.LoginTestControllers import LoginController
from Controllers.LogoutControllers import LogoutController
from Controllers.MainController import MainController
from Controllers.LoginController import LoginMainController
from Data.Credentials import Credentials
import pytest
import time

class Main:
    service=Service(executable_path='chromedriver.exe')

    opts=webdriver.ChromeOptions()
    
    # NUCLEAR OPTION - Run in Incognito (no password manager at all)
    opts.add_argument("--incognito")
    
    # Network settings
    opts.add_argument("--proxy-server='direct://'")
    opts.add_argument("--proxy-bypass-list=*")
    opts.add_argument("--disable-quic")
    
    # Disable ALL password manager features
    opts.add_argument("--disable-save-password-bubble")
    opts.add_argument("--disable-password-manager-reauthentication")
    opts.add_argument("--disable-blink-features=AutomationControlled")
    
    # Disable automation detection and popups
    opts.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    opts.add_experimental_option('useAutomationExtension', False)
    
    # Aggressive preferences to kill password manager
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings.popups": 0,
        "password_manager_enabled": False
    })
    
    opts.set_capability("acceptInsecureCerts", True)


    driver=webdriver.Chrome(service=service, options=opts)

    baseUrl='https://www.saucedemo.com/v1/index.html'
    
   

    def __init__(self):
        self.logincontrol=LoginController(self.driver)
        self.logoutcontrol=LogoutController(self.driver)
        self.maincontrol=MainController(self.driver)
        self.loginmaincontrol=LoginMainController(self.driver)
        self.credential=Credentials()
   
    def close_password_popup(self):
        """Close the annoying password breach popup if it appears"""
        try:
            # Wait a moment for popup to appear
            time.sleep(0.5)
            # Try to find and click OK button (if popup exists)
            self.driver.execute_script("""
                let okButton = document.querySelector('button[jsname="V67aGc"]');
                if (okButton) okButton.click();
            """)
        except:
            pass  # No popup, continue

    def loginTest(self):

        arr=self.credential.userData

        self.driver.get(self.baseUrl)

        self.driver.implicitly_wait(10)

         #For loop

        for i in range(0, len(arr)):
            self.logincontrol.usernameFill(arr[i]['username'])

            time.sleep(1)

            self.logincontrol.passwordFill(arr[i]['password'])

            time.sleep(1)

            self.logincontrol.loginClick()
            
            # Auto-close popup if it appears
            self.close_password_popup()

            self.driver.implicitly_wait(20)

            time.sleep(1)

            self.logoutcontrol.openMenuClick()

            time.sleep(1)

            self.logoutcontrol.logoutBtnClick()
    
    
    def checkoutFlow(self):

        self.driver.get(self.baseUrl)

        self.driver.implicitly_wait(10)

        self.loginmaincontrol.usernameFill('standard_user')

        time.sleep(1)

        self.loginmaincontrol.passwordFill('secret_sauce')

        time.sleep(1)

        self.loginmaincontrol.loginClick()

        self.driver.implicitly_wait(10)

        time.sleep(1)

        self.maincontrol.addToCartClick()

        time.sleep(1)

        self.maincontrol.cartClick()

        time.sleep(1)

        self.maincontrol.checkoutClick()

        time.sleep(1)

        self.maincontrol.firstNameFill('Karan')

        time.sleep(1)

        self.maincontrol.lastNameFill('Sharma')

        time.sleep(1)

        self.maincontrol.postalCodeFill('123456')

        time.sleep(1)

        self.maincontrol.continueClick()

        time.sleep(2)

        self.driver.save_screenshot('screenshots/confirmed.png')

        self.maincontrol.finishClick()

        time.sleep(2)

        self.driver.save_screenshot('screenshots/finalConfirmed.png')

        time.sleep(1)

        #logout

        self.logoutcontrol.openMenuClick()

        time.sleep(1)

        self.logoutcontrol.logoutBtnClick()



    
    



        


        

        


obj=Main()

#obj.loginTest()

obj.checkoutFlow()