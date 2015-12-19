select tbl_sector_info.industry ,count(exceed_info.symbol) as exceed_count
from (
select symbol, min(low) as lowest, max(high) as highest, if((max(high) - min(low))/min(low) > %f, 1, 0) as exceed 
from tbl_price
where day >= '%s' and day < '%s'
group by symbol
) exceed_info
left join tbl_sector_info
on (tbl_sector_info.symbol = exceed_info.symbol)
where exceed_info.exceed = 1
group by industry
order by exceed_count desc
;
