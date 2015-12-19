class StockAnalysisService(object):
	"""docstring for StockAnalysisService"""
	def __init__(self, db_conn):
		super(StockAnalysisService, self).__init__()
		self.db_conn = db_conn

	def dailyAvg(from_date, to_date):
		"""
		daily average price in date range [from_date, to_date)
        return [("symbol1",130.00),...]
		"""
		# db_conn exe sql select column1, avg(column2) from table group by column1
		pass



	def topChangeStocks(count, from_date, to_date):
		"""
		the top {count} stocks whose price changes the most in date range [from_date, to_date)
		return ['symbol1', 'symbol2',...]
		"""

		# sort the varience of each stock price, 
		pass

	def topSectors(from_date, to_date, price_change_ratio, count):
		"""
		the top {count} sectores whose price changed over {price_change_ratio} in date range [from_date, to_date)
		return ['symbol1', 'symbol2']
		"""
		# 
		pass	

	def maxProfits(from_date, to_date):
		"""
		the max profits by unlimited transaction in date range [from_date, to_date)
        
		"""
		pass

