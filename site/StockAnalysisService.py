import db_conn as db_conn 
import datetime as datetime

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

	def top_change_stocks(self,count=10, from_date="2014-07-01", to_date="2014-10-01"):
		"""
		the top {count} stocks whose price changes the most in date range [from_date, to_date)
		date format "YYYY-MM-DD"
		return ['symbol1', 'symbol2',...]

		"""
		# sort by the varience of each stock's 5 prices
		rows = db_conn.execute_select_sql_file('./service_sqls/stock_varience.sql',from_date,to_date)
		if count >= len(rows):
			return [rows[i][0] for i in xrange(len(rows))]
		else:
			return [rows[i][0] for i in xrange(count)]

	def top_industries(self,change_percentiles=0.3,count=3,from_date = "2014-01-01", to_date="2014-07-01"):
		"""
		the top {count} sectores whose price changed over {change_percentiles} in date range [from_date, to_date)
		return ['symbol1', 'symbol2']
		date format "YYYY-MM-DD"
		"""
		# top industries which has the most stocks whose price has change over {change_percentiles} 
		rows = db_conn.execute_select_sql_file('./service_sqls/top_industries.sql',change_percentiles,from_date,to_date)
		if count >= len(rows):
			return [rows[i][0] for i in xrange(len(rows))]
		else:
			return [rows[i][0] for i in xrange(count)]

	def max_profits(self,symbol="AAPL",from_date="2014-01-01", to_date="2015-01-01"):
		"""
		the max profits by unlimited transaction in date range [from_date, to_date)
		only calculate open price for simplification
		"""
		rows = db_conn.execute_select_sql_file('./service_sqls/open_prices.sql',symbol,from_date,to_date)
		prices = [rows[j][1] for j in xrange(len(rows))]
		
		date_format = "{:%Y-%m-%d}"
		records = []
		max_p = 0
		i  = 0 
		while(i < len(prices)):
			while(i+1< len(prices) and prices[i] >= prices[i+1]):
				i += 1
			low = prices[i]
			buy_day = rows[i][2]
			while(i+1 < len(prices) and prices[i]<=prices[i+1]):
				i += 1
			high = prices[i]
			sell_day = rows[i][2]
			p = high - low
			if(p > 0):
				records.append((date_format.format(buy_day),date_format.format(sell_day),p))
				max_p += p
			i += 1
		return {"symbol":symbol,"from_date":from_date,"to_date":to_date,"max_profits":max_p,"records":records}

	def max_profits_n_transaction(self,symbol="AAPL",from_date="2014-01-01", to_date="2015-01-01"):
		pass





