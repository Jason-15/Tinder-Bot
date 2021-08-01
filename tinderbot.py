from selenium import webdriver
import time

class tinderbot():

    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self):

        #go to tinder.com
        self.driver.get("https://tinder.com/")

        time.sleep(2)
        accept=self.driver.find_element_by_xpath("//button[@class='button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-secondary) C($c-secondary) Bdc($c-base):h C($c-base):h Bdc($c-base):f C($c-base):f Bdc($c-base):a C($c-base):a Fw($semibold) focus-button-style W(100%)--s']")
        accept.click()

        time.sleep(3)
        #log in w facebook. If facebook not there click more options and click facebook
        try:
            button=self.driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']")
        except :
            more=self.driver.find_element_by_xpath("//button[contains(text(),'More Options')]")
            more.click()
            time.sleep(2)
            
        finally:
            button=self.driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']")
            button.click()
            
        
        #switch to pop for facebook
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        time.sleep(2)
        
        #Login in with facebook w username, password, and then click login
        email=self.driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("")
        password=self.driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys("")
        login=self.driver.find_element_by_name("login")
        login.click()

        #switch to base window
        time.sleep(2)
        
        self.driver.switch_to_window(base_window)

        time.sleep(4)

        #click allow for location, enable and i accept(almost there hold on)
        allow=self.driver.find_element_by_xpath("//button[@aria-label='Allow']")
        allow.click()

        time.sleep(1)
        enable=self.driver.find_element_by_xpath("//button[@aria-label='Enable']")
        enable.click()
        
        time.sleep(4)

   

    def like(self):
        matches=True

        while matches==True:
            try:
                like_button=self.driver.find_element_by_xpath("//button[@aria-label='Like']")
                like_button.click()
            except :
                try:
                    not_interested=self.driver.find_element_by_class_name("button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml Fw($semibold) focus-button-style D(b) Mx(a) C($c-secondary) C($c-base):h")
                    not_interested.click()
                except:
                    pass
                
    


if __name__=="__main__":

    chung=tinderbot()
    chung.login()
    chung.like()
    
    
    