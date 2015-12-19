import db_conn as db_conn 

class StockAnalysisService(object):
	"""docstring for StockAnalysisService"""
	def __init__(self):
		super(StockAnalysisService, self).__init__()

	def daily_avg(self,from_date, to_date):
		"""
		daily average price in date range [from_date, to_date)
        return [("symbol1",130.00),...]
		"""
		# db_conn exe sql select column1, avg(column2) from table group by column1
		pass

	def top_change_stocks(self,count=10, from_date=None, to_date=None):
		"""
		the top {count} stocks whose price changes the most in date range [from_date, to_date)
		return ['symbol1', 'symbol2',...]
		"""
		# sort by the varience of each stock's 5 prices
		rows = db_conn.execute_select_sql_file('./stock_varience.sql')
		if count >= len(rows):
			return [rows[i][0] for i in xrange(len(rows))]
		else:
			return [rows[i][0] for i in xrange(count)]

	def top_industries(self,change_percentiles=0.3,count=3,from_date = None, to_date=None):
		"""
		the top {count} sectores whose price changed over {change_percentiles} in date range [from_date, to_date)
		return ['symbol1', 'symbol2']
		"""
		# top industries which has the most stocks whose price has change over {change_percentiles} 
		rows = db_conn.execute_select_sql_file('./top_industries.sql')
		if count >= len(rows):
			return [rows[i][0] for i in xrange(len(rows))]
		else:
			return [rows[i][0] for i in xrange(count)]

	def max_profits(self,from_date, to_date):
		"""
		the max profits by unlimited transaction in date range [from_date, to_date)
        
		"""
		pass

