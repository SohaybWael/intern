SELECT SUM(TOTAL_PRICE) AS TOTALRENVENCE
FROM pizza_sale;

SELECT SUM (total_price)/ COUNT( DISTINCT order_id) AS AVG_ORDER_VALUE
FROM pizza_sale;

SELECT SUM(quantity) AS TOTALPIZZA_SOLD
FROM pizza_sale;

SELECT count(DISTINCT order_id) AS TotalOrder
FROM pizza_sale;

SELECT CONVERT(FLOAT, SUM(quantity )) / CONVERT(FLOAT,COUNT (DISTINCT order_id)) 
AS REUSLT
FROM pizza_sale;

SELECT  FORMAT(order_date,'dddd') AS Day_Name,COUNT(DISTINCT order_id) AS Totalorder
FROM pizza_sale
GROUP BY FORMAT(order_date,'dddd')
ORDER BY COUNT(order_date);

SELECT  FORMAT(order_date,'MMM') AS Month_Name,COUNT(DISTINCT order_id) AS Totalorder
FROM pizza_sale
GROUP BY FORMAT(order_date,'MMM');

SELECT pizza_category,SUM(total_price) AS TOTALREVENCE,
(SUM(total_price)/(SELECT SUM(total_price) FROM pizza_sale))*100 AS PCT
FROM pizza_sale
GROUP BY pizza_category
ORDER BY PCT DESC;

SELECT pizza_size,SUM(total_price) AS TOTALREVENCE,
(SUM(total_price)/(SELECT SUM(total_price) FROM pizza_sale))*100 AS PCT
FROM pizza_sale
GROUP BY pizza_size
ORDER BY pizza_size ASC;


SELECT pizza_category ,SUM(quantity) AS TotalQUANTITY_SOLD
FROM pizza_sale
GROUP BY pizza_category 
ORDER BY TotalQUANTITY_SOLD DESC;

SELECT  TOP 5 pizza_name ,SUM(total_price) AS Total_Revenue
FROM pizza_sale
GROUP BY pizza_name
ORDER BY Total_Revenue DESC;

SELECT TOP 5 pizza_name ,SUM(total_price) AS Total_Revenue
FROM pizza_sale
GROUP BY pizza_name
ORDER BY Total_Revenue ASC;

SELECT TOP 5 pizza_name , sum(quantity) AS Totalpizza_sold
FROM pizza_sale
GROUP BY pizza_name
ORDER BY Totalpizza_sold ASC;

SELECT TOP 5 pizza_name , sum(quantity) AS TotalOrder_sold
FROM pizza_sale
GROUP BY pizza_name
ORDER BY TotalOrder_sold DESC ;

SELECT TOP 5 pizza_name , count(DISTINCT order_id) AS TotalOrder
FROM pizza_sale
GROUP BY pizza_name
ORDER BY TotalOrder ASC;

SELECT TOP 5 pizza_name , count(DISTINCT order_id) AS TotalOrder
FROM pizza_sale
GROUP BY pizza_name
ORDER BY TotalOrder DESC;





  