import sqlite3
class Database:
	def __init__(self):        
		#self.connection_string = "dbname='towneshops' user='root' host='localhost' password='' port='3306'"
		self.connection = sqlite3.connect('towneshops.db')
		self.get_cursor()

	def get_cursor(self):
		self.connection = sqlite3.connect('towneshops.db')
		return self.connection.cursor()

	def insert_product( self, product_id, product_name, available, image_name, image_url, category_id ):
		try:
			sql = """INSERT INTO tblProducts(product_id, product_name, available, image_name, image_url, category_id)""" + \
				  """ VALUES(?,?,?,?,?,?)"""
			self.get_cursor().execute(sql, [product_id, product_name, available, image_name, image_url, category_id])
			self.connection.commit()
			self.connection.close()
		except Exception as err:
			print("Cannot insert product with product_name = "+product_name)
			print(err)

	def insert_category( self, category_id, category_name ):
		try:
			sql = "INSERT INTO tblCategories(category_id, category_name) VALUES(?, ?)"
			self.get_cursor().execute(sql, [str(category_id), category_name])
			self.connection.commit()
			self.connection.close()
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
			print("Cannot get all products from DB. Error: "+str(err))
			return []

database = Database()


