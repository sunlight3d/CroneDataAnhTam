x = "https://towneshops.directedje.com/Galardi/catalog.asp"
from selenium import webdriver
import pandas as pd
import urllib.request

driver = webdriver.Chrome()
driver.get ("https://towneshops.directedje.com/Galardi/login.asp")
driver.find_element_by_id("Client.UserName").send_keys("elisa")
driver.find_element_by_id("Client.Password").send_keys("GGI")

#driver.find_elements_by_xpath("//*[@class='productlisting']").click()
driver.find_element_by_xpath("//*[@class='button' and @value='Login']").click()

x6 = driver.find_elements_by_xpath("//table[@class='categories']//child::a")
x7 = x6[0].get_attribute('href') #https://towneshops.directedje.com/Galardi/product-listing.asp?CID=-2&IDS=&QTY=
x8 = x6[0].get_attribute('text')
#https://towneshops.directedje.com/Galardi/product-listing.asp?P=1&CID=-2&IDS=&QTY=&RPP=1000

driver.get ("https://towneshops.directedje.com/Galardi/product-listing.asp?RPP=1000&P=1&CID=583&IDS=&QTY=")
x = driver.find_element_by_xpath("//table[@class='productlisting']")
x9 = driver.find_elements_by_xpath("//table[@class='productlisting']//child::tr")
print("hello")
x10 = x9[0]
x11 = x10.text.split("\n")
productId = x11[0]
productName = x11[2]
available = x11[4].split(" ")[0] if "Available" in x11[4] else 0
x12 = x10.find_element_by_xpath("//a[@class='thickbox']").get_attribute('href')
x13 = x12.split("/")[-1]

urllib.request.urlretrieve(x12, './images/'+x13)
#x12 la link anh
print("hello")

x1 = x.text
x2 = x1.split("\n")


x3 = x.find_elements_by_xpath("//a[contains(text(), 'Details')]")
detail_product = x3[0].get_attribute("href")

driver.get ("https://towneshops.directedje.com/Galardi/product-details.asp?ID=10366&CID=727&P=1")
x4 = driver.find_element_by_xpath("//table[@class='productdetails']//child::tr")
x5 = x4.text.split("\n")
print("hello")