from selenium import webdriver
from bs4 import BeautifulSoup
import time

#start with web browser
browser=webdriver.Chrome()

def getHtmlSourceCode():
    #get source code and prettify with bs4
    url="https://www.trendyol.com/monster/abra-a5-v16-7-3-intel-core-i5-11400h-16gb-ram-500gb-ssd-4gb-gtx1650-freedos-15-6-fhd-144hz-p-133966690"
    browser.get(url)
    html = browser.page_source
    time.sleep(2)
    soup = BeautifulSoup(html, 'html.parser')
    getHtmlSourceCode=soup
    return getHtmlSourceCode
# print(soup.prettify()) #burası tüm sayfayı yazdrıcak, hangi kısımları yazdıracağını biz değiştircez.
# soup.find_all("div",{"id":"content"}) id'si content olan div'i bul demek
getPrice=getHtmlSourceCode().find("span",{"class":"prc-dsc"}).text
getPrdctName=getHtmlSourceCode().find("h1",{"class":"pr-new-br"}).text
products=[getPrdctName,getPrice]
print(products[0],"ürününün fiyatı",products[1])

#close browser
browser.close()