#yalnızca ilk çıkan takipçileri alıyo çünkü websitesinde sidebar ile aşağı indikçe yeni takipçi yüklenmiyor.
#İnstanın web versiyonunda tüm takipçileri görmenin bi yolu yok şimdilik. Onun yerine arama kısmına bir şey yazdırılıp ona göre takipçi aranabilir. En fazla bunu ekleyebilirim.
#Ayrıca bir şekilde css selector'u çalıştıramadım. Versiyon uyumsuzluğunu çözünce o yöntemle de kod yazabiliriz.
from InstaLoginInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
    
    def LogIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        usernameXpath = self.browser.find_element("xpath", "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordXpath = self.browser.find_element("xpath", "//*[@id='loginForm']/div/div[2]/div/label/input")
        usernameXpath.send_keys(self.username)
        passwordXpath.send_keys(self.password)
        passwordXpath.send_keys(Keys.ENTER)
        time.sleep(2)
        
    
    def openFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}/followers")
        time.sleep(5)

        elementor = 1
        while elementor < 9:
    
            elements = self.browser.find_element("xpath", f"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{elementor}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span").text
            elementor += 1
            print(elements)                               
      

insta = Instagram(username,password)
insta.LogIn()
insta.openFollowers()

