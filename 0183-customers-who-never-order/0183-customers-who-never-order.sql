# Write your MySQL query statement below
select name as Customers from Customers as c
left join orders as o 
on c.id=o.customerid
where o.customerid is null
