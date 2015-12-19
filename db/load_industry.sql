# mysql -u root < prepare_db.sql
use stock;
LOAD DATA INFILE '/Users/shayan/Documents/projects/myown/StockAnalysis/raw_data/industry.csv'
INTO TABLE tbl_sector_info
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@col1,@col2,@col3,@col4) 
SET 
symbol=nullif(@col1,''), 
industry=nullif(@col2,''), 
sector=nullif(@col3,'');
SHOW WARNINGS;
