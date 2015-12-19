select 
symbol, 
avg((open-avg_price)*(open-avg_price) + (close-avg_price)*(close-avg_price))/2 as varience, 
sqrt(avg((open-avg_price)*(open-avg_price) + (close-avg_price)*(close-avg_price))/2 ) as stdev
from tbl_price
left join (
	select symbol as symbol1, avg(open+close)/2 as avg_price
	from tbl_price
	group by symbol1
) price_exp
on tbl_price.symbol = price_exp.symbol1
group by symbol
order by stdev desc 
;

select symbol, 
avg(((open*open) +(close*close))/2) - avg((open+close)/2)*avg((open+close)/2) as varience,
sqrt(avg(((open*open) +(close*close))/2) - avg((open+close)/2)*avg((open+close)/2)) as stdev
from tbl_price 
group by symbol
order by stdev desc 
;

select symbol, 
avg((open*open)) - avg(open)*avg(open) as varience,
sqrt(avg((open*open)) - avg(open)*avg(open)) as stdev
from tbl_price 
group by symbol
order by stdev desc 
;