#!/usr/bin/env python2
import ystockquote
import datetime
from dateutil.relativedelta import relativedelta
import json
import urllib2

def get_stock_year_price(symbol,year_begin, year_end):
	'''
	Get the prices of Stock {symbol} from year_begin (int) to year_end (int)

	Returns a dictionary like:
	{"Symbol": symbol, "Prices": {"2015-1-1":..., "2015-2-1":...}}

	'''
	d = datetime.datetime(year_begin,1,1)
	end_date = datetime.datetime(year_end,12,31)
	ret = {"Symbol":symbol,"Prices":{}}
	# iterating over month
	while  d < end_date:
		next_mon = d + relativedelta(months=1) 
		# fetch this month's all trade days' data
		try:
			m =  ystockquote.get_historical_prices(symbol, d.strftime("%Y-%m-%d"), next_mon.strftime("%Y-%m-%d"))
		except urllib2.HTTPError:
			d = next_mon
			continue
		for day, data in m.iteritems():
			ret["Prices"][day] = data
		d = next_mon
	return ret