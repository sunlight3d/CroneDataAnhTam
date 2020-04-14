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
    def get_categories_and_save_to_db():
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
            database.insert_category(category_id, category_name)
            print("Insert category with id = {}, name = {} to Database".format(category_id, category_name))
        return categories

    @staticmethod
    def get_categories_from_db():
        tuple_categories = database.get_categories()
        categories = []
        for tuple_category in tuple_categories:
            category = Category(tuple_category[0],
                              tuple_category[1])
            categories.append(category)
        return categories

