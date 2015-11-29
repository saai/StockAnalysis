#!/usr/bin/env python
import os
import sys
import json
import MySQLdb as mysql

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
DB_NAME = "stock"

def get_stocks_data(data_dir):
    ret = []
    for lists in os.listdir(data_dir): 
        path = os.path.join(data_dir, lists) 
        if not os.path.isdir(path) and os.path.splitext(path)[1] == ".json":
            # open stock json file
            with open(path) as fp:
                m = json.loads(fp.read())
                ret.append(m)
    return ret

def transaction(db, sqls):
    db.autocommit(False)
    cursor = db.cursor()
    try:
        for sql in sqls:
            cursor.execute(sql)
        db.commit()
    except mysql.Error, e:
        db.rollback()
        return e

def load_data(stocks_data):
    try:
        conn = mysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, DB_NAME)
        # use transaction
        sqls = []
        for stock_data in stocks_data:
            sym = stock_data["Symbol"]
            prices = stock_data["Prices"]
            for date in prices:
                val = prices[date]
                # 2015-10-10 => {'Adj Close':xxx, 'High' : xxx, 'Low': xxx, 'Open': xxx, 'Close':...} 
                high, low = float(val['High']), float(val['Low'])
                open_price, close_price = float(val['Open']), float(val['Close'])
                adj_close = float(val['Adj Close'])
                sql = "INSERT INTO tbl_price VALUES('%s',%f, %f, %f, %f, %f, '%s');" % (sym, high, low, open_price, close_price, adj_close, date)
                sqls.append(sql)
        print 'begin insert', len(sqls), 'lines'
        if  transaction(conn, sqls) == None:
            print 'insert OK'
    except mysql.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    finally:    
        conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'load_data.py [data_dir]'
        sys.exit(1)
    ret = get_stocks_data(sys.argv[1])
    load_data(ret)