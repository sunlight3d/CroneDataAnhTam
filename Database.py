import sqlite3
class Database:
	def __init__(self):        
		#self.connection_string = "dbname='towneshops' user='root' host='localhost' password='' port='3306'"
		self.connection = sqlite3.connect('towneshops.db')
		self.get_cursor()

	def get_cursor(self):
		self.connection = sqlite3.connect('towneshops.db')
		return self.connection.cursor()

	def insert_product( self, productId, productName, productDescription, available, categoryId ):
		try:
			sql = """INSERT INTO tblProducts(productId, productName, productDescription, available, categoryId)""" + \
				  """ VALUES(%s, %s,%s, %s,%s)"""
			self.get_cursor().execute(sql, (productId, productName, productDescription, available, categoryId))
			self.connection.commit()
			self.connection.close()
		except Exception as err:
			print("Cannot insert product with productName = "+productName)
			print(err)

	def insert_category( self, categoryId, categoryName ):
		try:
			sql = "INSERT INTO tblCategories(categoryId, categoryName) VALUES(%s, %s)"
			self.get_cursor().execute(sql, (categoryId, categoryName))
			self.connection.commit()
			self.connection.close()
		except Exception as err:
			print("Cannot insert category with id="+categoryId+"categoryName = "+categoryName)
			print(err)
database = Database()


