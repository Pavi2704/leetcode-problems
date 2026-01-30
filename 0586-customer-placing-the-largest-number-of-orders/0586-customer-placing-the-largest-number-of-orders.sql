select customer_number
from orders
GROUP BY customer_number
order by count(customer_number) desc
limit 1