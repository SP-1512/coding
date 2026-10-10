select name as Customers 
FROM customers
where id NOT IN (select customerId FROM orders); 