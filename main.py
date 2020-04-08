from selenium import webdriver
import urllib.request
from Category import Category
from Product import Product
categories = Category.get_categories()
# Category.insert_categories_to_db(categories)
# for category in categories:
#     products = Product.get_products(category.category_id)

#test
products = Product.get_products_from_db()

# Product.insert_products_to_db(products)
Product.save_product_images(products)
print("end")
