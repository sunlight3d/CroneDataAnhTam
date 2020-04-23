
CREATE TABLE tblCategories(
	category_id INTEGER PRIMARY KEY,
	category_name VARCHAR(1000)
);
DROP TABLE tblProducts;
CREATE TABLE tblProducts(
	product_id VARCHAR(200) PRIMARY KEY,
	product_name VARCHAR(1000),
	description VARCHAR(1000),
	available INTEGER,
	image_name VARCHAR(1000),
	image_url VARCHAR(1000),
	category_id INTEGER
);