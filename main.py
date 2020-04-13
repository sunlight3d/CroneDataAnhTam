from selenium import webdriver
import urllib.request
from Category import Category
from Product import Product
# categories = Category.get_categories_and_save_to_db()
# for category in categories:
#     products = Product.get_products_and_save_to_db(category.category_id)
products = Product.get_products_from_db()
Product.save_product_images(products)
print("end")
