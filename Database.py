from psycopg2 import psycopg2
class Database:
	def __init__(self):        
		self.connection_string = "dbname='towneshops' user='root' host='localhost' password='' port='3306'"
		self.connection = null
		self.get_cursor()

	def get_cursor(self):
		self.connection = psycopg2.connect(connection_string)
		cursor = connection.cursor()
		return cursor



	def insert_product( self, productId, productName, productDescription, available, categoryId ):
		sql = "INSERT INTO tblProducts(productId, productName, productDescription, available, categoryId)"+
				" VALUES(%s, %s,%s, %s,%s)"
		self.get_cursor().execute(sql, (productId, productName, productDescription, available, categoryId))
		self.connection.commit()

	def insert_category( self, categoryId, categoryName ):
		sql = "INSERT INTO tblCategories(categoryId, categoryName) VALUES(%s, %s)"
		self.get_cursor().execute(sql, (categoryId, categoryName))
		self.connection.commit()
	

