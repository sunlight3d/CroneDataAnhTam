from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from driver import driver
from Login import Login
from Database import database
class Category:
    def __init__(self, category_name, category_id):
        self.category_name = category_name
        self.category_id = category_id
        
    @staticmethod
    def get_categories():
        login = Login()
        login.login()
        a_elements = driver.find_elements_by_xpath("//table[@class='categories']//child::a")
        categories = []
        for a_element in a_elements:
            link_href = a_element.get_attribute('href')
            category_id = int((link_href.split('?')[-1]).split("=")[-1])
            category_name = a_element.get_attribute('text')
            new_category = Category(category_name, category_id)
            categories.append(new_category)
        return categories

    @staticmethod
    def insert_categories_to_db(categories):
        for category in categories:
            database.insert_category(category.category_id, category.category_name)
        print("Insert categories successfully")

