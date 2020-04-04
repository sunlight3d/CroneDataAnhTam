from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from driver import driver
class Login:
    def __init__(self):
        pass
    def login(self):
        driver.get(URL_LOGIN)
        driver.find_element_by_id("Client.UserName").send_keys("elisa")
        driver.find_element_by_id("Client.Password").send_keys("GGI")
        driver.find_element_by_xpath("//*[@class='button' and @value='Login']").click()
        wait = WebDriverWait(driver, 5)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "categories")))
