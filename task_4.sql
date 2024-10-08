declare @start as datetime = '2000-03-01 00:00:00'
;
declare @end   as datetime = '2000-03-31 23:59:59'
;

select  name
	, start_date as time_utc
	, dateadd(hour, 3, start_date) as time_msk
from DQ.DB.employers
where start_date >= dateadd(hour, -3, @start) and start_date <= dateadd(hour, -3, @end)   
;