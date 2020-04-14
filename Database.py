import sqlite3


class Database:
    def __init__(self):
        # self.connection_string = "dbname='towneshops' user='root' host='localhost' password='' port='3306'"
        self.connection = sqlite3.connect('towneshops.db')
        self.get_cursor()

    def get_cursor(self):
        self.connection = sqlite3.connect('towneshops.db')
        return self.connection.cursor()

    def is_exist_product(self, product_id, product_name):
        try:
            sql = """SELECT COUNT(*) FROM tblProducts """ + \
                  """WHERE tblProducts.product_id = ? AND tblProducts.product_name = ?"""
            cursor = self.get_cursor()
            cursor.execute(sql, [product_id, product_name])
            dict_products = cursor.fetchall()
            self.connection.close()
            return int(dict_products[0][0]) > 0
        except Exception as err:
            print("Cannot get tblProducts from DB. Error: " + str(err))
            return False

    def insert_product(self, product_id, product_name, available, image_name, image_url, category_id):
        try:
            if self.is_exist_category(product_id, product_name):
                print("product with id={}, product_name = {} exists".format(product_id, product_name))
            else:
                sql = "INSERT INTO tblProducts(product_id, product_name, available, image_name, image_url,category_id)"+\
                      """ VALUES(?,?,?,?,?,?)"""
                self.get_cursor().execute(sql, [product_id, product_name, available, image_name, image_url, category_id])
                self.connection.commit()
                self.connection.close()
                print("Inserted product with id={}, product_name = {}".format(product_id, product_name))
        except Exception as err:
            print("Cannot insert product with product_name = " + product_name)
            print(err)

    def is_exist_category(self, category_id, category_name):
        try:
            sql = """SELECT COUNT(*) FROM tblCategories """ + \
                  """WHERE tblCategories.category_id = ? AND tblCategories.category_name = ?"""
            cursor = self.get_cursor()
            cursor.execute(sql, [category_id, category_name])
            dict_categories = cursor.fetchall()
            self.connection.close()
            return int(dict_categories[0][0]) > 0
        except Exception as err:
            print("Cannot get tblCategories from DB. Error: " + str(err))
            return False

    def insert_category(self, category_id, category_name):
        try:
            if self.is_exist_category(category_id, category_name):
                print("category with id={}, category_name = {} exists".format(category_id, category_name))
            else:
                sql = "INSERT INTO tblCategories(category_id, category_name) VALUES(?, ?)"
                self.get_cursor().execute(sql, [str(category_id), category_name])
                self.connection.commit()
                self.connection.close()
                print("Inserted category with id={}, category_name = {}".format(category_id, category_name))
        except Exception as err:
            print("Cannot insert category with id={}, category_name = {}".format(category_id, category_name))
            print(err)

    def get_products(self):
        try:
            sql = """SELECT * FROM tblProducts"""
            cursor = self.get_cursor()
            cursor.execute(sql, [])
            dict_products = cursor.fetchall()
            self.connection.close()
            return dict_products
        except Exception as err:
            print("Cannot get all products from DB. Error: " + str(err))
            return []

    def get_categories(self):
        try:
            sql = """SELECT * FROM tblCategories"""
            cursor = self.get_cursor()
            cursor.execute(sql, [])
            dict_categories = cursor.fetchall()
            self.connection.close()
            return dict_categories
        except Exception as err:
            print("Cannot get all categories from DB. Error: " + str(err))
            return []


database = Database()
