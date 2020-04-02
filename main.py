x = "https://towneshops.directedje.com/Galardi/catalog.asp"
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome()
driver.get ("https://towneshops.directedje.com/Galardi/login.asp")
driver.find_element_by_id("Client.UserName").send_keys("elisa")
driver.find_element_by_id("Client.Password").send_keys("GGI")

#driver.find_elements_by_xpath("//*[@class='productlisting']").click()
driver.find_element_by_xpath("//*[@class='button' and @value='Login']").click()
print("hello")

driver.get ("https://towneshops.directedje.com/Galardi/product-listing.asp?RPP=1000&P=1&CID=583&IDS=&QTY=")
x = driver.find_element_by_xpath("//table[@class='productlisting']")
x1 = x.text
x2 = x1.split("\n")
x3 = x.find_elements_by_xpath("//a[contains(text(), 'Details')]")
detail_product = x3[0].get_attribute("href")

driver.get ("https://towneshops.directedje.com/Galardi/product-details.asp?ID=10366&CID=727&P=1")
x4 = driver.find_element_by_xpath("//table[@class='productdetails']//child::tr")
x5 = x4.text.split("\n")
print("hello")