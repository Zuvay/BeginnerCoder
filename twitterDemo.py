#find element kısmını her yerde çalıştırmadığım için biraz uzun yoldan dolaştım. Düzelticem
from twLoginInfo import username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
import time
class TwitterBot:
    def __init__(self, username): 
        self.browser = webdriver.Chrome()
        self.username = username
    
    def logIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        self.browser.maximize_window()
        time.sleep(2)
        elementUsername = self.browser.find_element(By.CLASS_NAME, "r-30o5oe") #classın tamamını yazmadan da çalışıyomuş
        elementUsername.click()
        elementUsername.send_keys(self.username)
        elementUsername.send_keys(Keys.ENTER)
        time.sleep(1)
        
        keys_to_type = [] #şifrenin elemanları

        # Her tuşu basarak yazdırma işlemi
        for key in keys_to_type:
            keyboard.press(key)
            time.sleep(0.1)  # Her tuş arasında biraz gecikme
            keyboard.release(key)
        
        keyboard.press_and_release('enter')
    
    def TweetIt(self,tweet):
        time.sleep(2)
        keyboard.press_and_release('n')
        time.sleep(3)
        keys_to_type = list(tweet)
        for key in keys_to_type:
            keyboard.press(key)
            time.sleep(0.1)  # Her tuş arasında biraz gecikme
            keyboard.release(key)
        tweet_button = self.browser.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
        tweet_button.click()

        
        
twBot = TwitterBot(username)
twBot.logIn()
time.sleep(2)
twBot.TweetIt("tweeted from vsc")


