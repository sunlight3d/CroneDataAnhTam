CREATE DATABASE towneshops IF NOT EXISTS;
CREATE TABLE tblCategories(
	categoryId INT PRIMARY KEY,
	categoryName VARCHAR(1000)
);

CREATE TABLE tblProducts(
	productId VARCHAR(200) PRIMARY KEY,
	productName VARCHAR(1000),
	productDescription VARCHAR(1000),
	available INT,
	categoryId INT,
);
INSERT INTO tblCategories(categoryId, categoryName) VALUES(%s, %s)
INSERT INTO tblProducts(productId, productName, productDescription, available, categoryId) VALUES(%s, %s,%s, %s,%s)