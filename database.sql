
CREATE TABLE tblCategories(
	category_id INTEGER PRIMARY KEY,
	category_name VARCHAR(1000)
);

CREATE TABLE tblProducts(
	product_id VARCHAR(200) PRIMARY KEY,
	product_name VARCHAR(1000),
	product_description VARCHAR(1000),
	available INTEGER,
	category_id INTEGER
);
INSERT INTO tblCategories(category_id, category_name) VALUES(%s, %s)
INSERT INTO tblProducts(product_id, product_name, product_description, available, category_id) VALUES(%s, %s,%s, %s,%s)