import MySQLdb as mysql

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
DB_NAME = "stock"

def execute_select_sql_file(path,*args):
	conn = mysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, DB_NAME)
	try:
		sql = []
		for line in open(path):
			sql.append(line)
		str_sql = ("".join(sql))%tuple(args)
		return execute_select_sql_str(conn, str_sql)
	except Exception, e:
		print 'exception',e
	finally:
		conn.close()

def execute_select_sql_str(str_sql):
	
	conn = mysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, DB_NAME)

	try:
		return execute_select_sql_str(conn, str_sql)
	except Exception, e:
		print 'exception',e
	finally:
		conn.close()

def execute_select_sql_str(db,str_sql):
	try:
		cursor = db.cursor()
		cursor.execute(str_sql)
		db.commit()

		# get the number of rows in the resultset
		numrows = int(cursor.rowcount)

		# get and display one row at a time.
		rows = []
		for x in range(0,numrows):
			row = cursor.fetchone()
			rows.append(row)
		return rows
	except Exception, e:
		print 'exception',e
		return None


