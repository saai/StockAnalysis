CREATE DATABASE IF NOT EXISTS stock;
USE stock;
CREATE TABLE IF NOT EXISTS tbl_price (
    symbol VARCHAR(10) NOT NULL,
    high FLOAT NOT NULL,
    low FLOAT NOT NULL,
    open FLOAT NOT NULL,
    close FLOAT NOT NULL,
    adj_close FLOAT NOT NULL,
    day DATETIME NOT NULL,
    INDEX symbol(symbol),
    INDEX day(day),
    INDEX symbol_day(symbol, day)
);