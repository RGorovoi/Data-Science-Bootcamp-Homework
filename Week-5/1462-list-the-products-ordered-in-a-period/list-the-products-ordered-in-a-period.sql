# Write your MySQL query statement below

SELECT p.product_name, o.total_units AS unit
FROM Products p
INNER JOIN
(
    SELECT product_id, SUM(unit) AS total_units
    FROM Orders
    WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
    GROUP BY product_id
    HAVING SUM(unit) >=100
) o ON p.product_id = o.product_id
    