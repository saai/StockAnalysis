select symbol, open , day
from tbl_price
where symbol='%s' and day >= '%s' and day < '%s' 
order by day
;