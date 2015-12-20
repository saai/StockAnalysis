CREATE DATABASE IF NOT EXISTS stock;
USE stock;
CREATE TABLE IF NOT EXISTS tbl_price (
    symbol VARCHAR(10) NOT NULL,
    high FLOAT NOT NULL,
    low FLOAT NOT NULL,
    open FLOAT NOT NULL,
    close FLOAT NOT NULL,
    adj_close FLOAT NOT NULL,
    daily_avg FLOAT NOT NULL,
    day DATETIME NOT NULL,
    INDEX symbol(symbol),
    INDEX day(day),
    INDEX symbol_day(symbol, day)
);
CREATE TABLE IF NOT EXISTS tbl_sector_info (
    symbol VARCHAR(10) NOT NULL,
    industry VARCHAR(255),
    sector VARCHAR(255),
    INDEX symbol(symbol),
    INDEX industry(industry),
    INDEX sector(sector)
);