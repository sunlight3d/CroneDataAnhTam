from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
from driver import driver
import re
from Login import Login
from Database import database
import urllib.request
from selenium.common.exceptions import TimeoutException
from urls import URL_HOME, URL_LOGIN, URL_PRODUCT_DETAIL, URL_PRODUCT_LISTING
import os
class Product:
    def __init__(self, product_id, product_name, available, image_name, image_url, category_id):
        self.product_id = product_id
        self.product_name = product_name
        self.available = available
        self.image_name = image_name
        self.image_url = image_url
        self.category_id = category_id
    @staticmethod
    def get_products_and_save_to_db(category_id):
        link_to_products_page = URL_PRODUCT_LISTING+"RPP=1000&P=1&CID="+str(category_id)+"&IDS=&QTY="
        #"https://towneshops.directedje.com/Galardi/product-listing.asp?RPP=1000&P=1&CID=583&IDS=&QTY="
        try:
            driver.get(link_to_products_page)
        except TimeoutException:
            driver.execute_script("window.stop();")
        products_elements = driver.find_elements_by_xpath("//table[@class='productlisting']//child::tr")
        products = []
        for product_element in products_elements:
            try:
                temp = product_element.text.split("\n")
                product_id = temp[0]
                product_name = r'{}'.format(temp[2])
                available = temp[4].split(" ")[0] if "Available" in temp[4] else 0
                try:
                    image_url = product_element.find_element_by_class_name('thickbox').get_attribute('href')
                    image_name = image_url.split("/")[-1]
                except Exception as e:
                    image_url = ""
                    image_name = ""
                # save image to images
                new_product = Product(product_id, product_name, available, image_name, image_url, category_id)
                products.append(new_product)
                database.insert_product(new_product.product_id,
                                        new_product.product_name,
                                        new_product.available,
                                        new_product.image_name,
                                        new_product.image_url,
                                        new_product.category_id)
            except Exception as e:
                print("error creating product : "+str(e))
        print("Finish insert products for category_id : "+str(category_id))
        return products

    @staticmethod
    def get_products_from_db():
        tuple_products = database.get_products()
        products = []
        for tuple_product in tuple_products:
            product = Product(tuple_product[0],
                              tuple_product[1],
                              tuple_product[2],
                              tuple_product[3],
                              tuple_product[4],
                              tuple_product[5])
            products.append(product)
        return products

    @staticmethod
    def save_product_images(products):
        i = 0
        for product in products:
            try:
                product_id = product.product_id
                image_url = product.image_url
                image_name = product_id + ".jpg"
                image_name = re.sub(r'\s+', '', image_name)
                image_name = re.sub(r'/', '-', image_name)
                if not os.path.isfile('./images/' + image_name) and 'http' in image_url:
                    urllib.request.urlretrieve(image_url, './images/' + image_name)
                    i = i + 1
                    print(str(i) + " - Saved file : " + image_name)
            except Exception as e:
                print("Cannot save image: " + image_name+".Error: "+str(e))


