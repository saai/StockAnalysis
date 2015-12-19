select symbol, 
avg(((open*open) + (high*high)+ (low*low) + (close*close) + (adj_close*adj_close))/5) - avg((open+high+low+close+adj_close)/5)*avg((open+high+low+close+adj_close)/5) as varience
from tbl_price
where day >= '%s' and day < '%s' 
group by symbol
order by varience desc
;