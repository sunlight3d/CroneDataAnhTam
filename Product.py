from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from driver import driver
from Login import Login
from Database import database
import urllib.request

class Product:
    def __init__(self, product_id, product_name, available, image_url):
        self.product_id = product_id
        self.product_name = product_name
        self.available = available
        self.image_url = image_url

    @staticmethod
    def get_products(link__to_products_page):
        #"https://towneshops.directedje.com/Galardi/product-listing.asp?RPP=1000&P=1&CID=583&IDS=&QTY="
        driver.get(link__to_products_page)
        products_elements = driver.find_elements_by_xpath("//table[@class='productlisting']//child::tr")
        products = []
        for products_element in products_elements:
            temp = products_element.text.split("\n")
            product_id = temp[0]
            product_name = temp[2]
            available = temp[4].split(" ")[0] if "Available" in temp[4] else 0
            image_url = products_element.find_element_by_xpath("//a[@class='thickbox']").get_attribute('href')
            image_name = image_url.split("/")[-1]
            urllib.request.urlretrieve(image_url, './images/' + image_name)
            new_product = Product(product_id, product_name, available, image_url)
            products.append(new_product)
        return products

    @staticmethod
    def insert_products_to_db():
        products = Product.get_products()
        for product in products:
            database.insert_product(product.product_id, product.product_name, "", product.available, product.category_id)

