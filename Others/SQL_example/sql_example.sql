--Loc ra cac ORDERNUMBER phat sinh tu 01/07/2003 - 15/07/2003 & sap xep theo thu tu ngay phat sinh ORDERDATE
select * 
from dbo.data_sample a
where ORDERDATE between '01-jul-2003' and '15-jul-2003'
order by ORDERDATE;

--Thong ke so luong ORDERNUMBER theo thang, dinh dang thangnam (YYYYMM)
select  CONVERT(varchar(6), ORDERDATE, 112) month_report
		,count(distinct ORDERNUMBER) so_luong_order
from dbo.data_sample a
group by CONVERT(varchar(6), ORDERDATE, 112)
order by CONVERT(varchar(6), ORDERDATE, 112);

--Tim ra 3 thang co so luong ORDERNUMBER lon nhat
select  top 3 
		 CONVERT(varchar(6), ORDERDATE, 112) month_report
		,count(distinct ORDERNUMBER) so_luong_order
from dbo.data_sample a
group by CONVERT(varchar(6), ORDERDATE, 112)
order by count(distinct ORDERNUMBER) desc;

--Tim ra 5 ORDERNUMBER mang lai doanh thu lon nhat (lam tron 2 chu so) va so luong product_code cua cac order do
select  top 5 
		 ORDERNUMBER
		,round(sum(sales),2) total_sales
		,count(distinct PRODUCTCODE) no_productcode
from dbo.data_sample a
group by ORDERNUMBER
order by round(sum(sales),2) desc;

--Kiem tra xem co ORDERNUMBER nao phat sinh tai it nhat 2 ngay khac nhau hay khong
select  ORDERNUMBER
		,count(distinct ORDERDATE) NO_ORDERDATE
from dbo.data_sample a
group by ORDERNUMBER
having count(distinct ORDERDATE) > 1;

--Danh so thu tu phat sinh ORDERNUMBER duoc sap xep theo QUANTITYORDERED giam dan va productcode tang dan
select ROW_NUMBER() over(partition by ORDERNUMBER order by QUANTITYORDERED desc,productcode) so_thu_tu
	,a.* 
from dbo.data_sample a;

--Lay ra giao dich phat sinh dau tien cua tung ORDERNUMBER duoc sap xep theo QUANTITYORDERED giam dan va productcode tang dan
with tmp as
(
select ROW_NUMBER() over(partition by ORDERNUMBER order by QUANTITYORDERED desc ,productcode) so_thu_tu
	,a.* 
from dbo.data_sample a
)
select * from tmp
where so_thu_tu = 1
;
--Tinh khoang thoi gian giua 2 ORDERNUMBER
with tmp as
(
select distinct ORDERNUMBER,ORDERDATE  from dbo.data_sample a
)
select  a.*
		,lag(ORDERDATE) over(order by ORDERDATE) PRE_ORDERDATE
		,DATEDIFF(DAY,lag(ORDERDATE) over(order by ORDERDATE),ORDERDATE) DATE_DIFF
from tmp a;

--Tinh binh quan khoang thoi gian giua 2 ORDERNUMBER
with tmp_1 as
(
select distinct ORDERNUMBER,ORDERDATE  from dbo.data_sample a
),
tmp_2 as
(
select  a.*
		,lag(ORDERDATE) over(order by ORDERDATE) PRE_ORDERDATE
		,DATEDIFF(DAY,lag(ORDERDATE) over(order by ORDERDATE),ORDERDATE) DATE_DIFF
from tmp_1 a
)
select AVG(date_diff) so_ngay_bq from tmp_2
;
