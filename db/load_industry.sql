# mysql -u root < prepare_db.sql
use stock;
LOAD DATA INFILE '/Users/shayan/Documents/projects/myown/StockAnalysis/raw_data/industry.csv'
INTO TABLE tbl_sector_info
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(symbol, industry, sector);
