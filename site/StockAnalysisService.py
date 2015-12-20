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
        the max profits with unlimited transactions in date range [from_date, to_date)
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

    def max_profits_k_transaction(self,k = 2,symbol="AAPL",from_date="2014-01-01", to_date="2015-01-01"):
        """
        the max profits by maximum k transactions in date range [from_date, to_date)
        only calculate open price for simplification
        """
        rows = db_conn.execute_select_sql_file('./service_sqls/open_prices.sql',symbol,from_date,to_date)
        prices = [rows[j][1] for j in xrange(len(rows))]
        date_format = "{:%Y-%m-%d}"
        n = len(prices)
        if n<=1:
            return {"symbol":symbol,"from_date":from_date,"to_date":to_date,"max_profits":0,"records":[], "transaction_times":k}

        if (k >= n / 2):
            quick_res = self.quick_solve(prices)
            return {"symbol":symbol,"from_date":from_date,"to_date":to_date,"max_profits":quick_res["max_profit"],"records":quick_res["records"], "transaction_times":k}
        
        dp = [[0 for j in xrange(n)] for i in xrange(k+1)]

        # -1 means not in the transaction, 0 means to hold, 1 means to sell
        last_records = [[-1 for _ in xrange(n)] for _ in xrange(n)]
        cur_records = [[-1 for _ in xrange(n)] for _ in xrange(n)]
        cur_record = [-1 for _ in xrange(n)]
        
        for i in range(1,k+1):
            hold_idx = 0
            temp = dp[i-1][0] - prices[0]
            for j in xrange(1,n):
                # equals to j-1 th transaction or sell to complete new transaction.
                if(temp+prices[j] > dp[i][j-1]):
                    dp[i][j] = temp+prices[j]
                    # new transaction complete
                    cur_record[j] = 1
                    # clear records in range [hold_idx, j)
                    self.clear_record(cur_record,hold_idx, j)
                    # should copy the last_records[hold_idx]
                    self.copy_record(last_records[hold_idx-1], cur_record, 0, hold_idx)
                else:
                    dp[i][j] = dp[i][j-1]
                # update cur_records to save cur_record
                self.copy_record(cur_record,cur_records[j],0,n)

                # potential hold should cost least, which means to remain most profit after hold.
                if(dp[i-1][j]-prices[j] > temp):
                    temp = dp[i-1][j] - prices[j]
                    hold_idx = j
            last_records, cur_records = cur_records, last_records
        return {"symbol":symbol,"from_date":from_date,"to_date":to_date,"max_profits":dp[k][n-1],"records":cur_record, "transaction_times":k}

    def quick_solve(self, prices):
        profits = 0
        records = [-1 for _ in xrange(len(prices))]
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profits += (prices[i]-prices[i-1])
                records[i-1] = 0
                records[i] = 1
        return {"max_profit":profits, "records":records}

    def copy_record(self, from_record, to_record, col_begin, col_end):
        for i in range(col_begin, col_end):
            to_record[i] = from_record[i]

    def clear_record(self, record, col_begin, col_end):
        for i in range(col_begin, col_end):
            record[i] = 0

