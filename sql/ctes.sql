-- esta query devuelve los clientes que han gastado más en una ciudad específica, ordenados por el total gastado
-- utilizando una CTE para calcular el total gastado y el número de compras por cliente
WITH CustomerSpending AS (
    SELECT
        CustomerID,
        SUM(TotalPrice) AS TotalSpent,
        COUNT(SalesID) AS NumberOfPurchases
    FROM sales
    GROUP BY CustomerID
)
SELECT
    c.CustomerID,
    c.FirstName,
    c.LastName,
    cs.TotalSpent,
    cs.NumberOfPurchases
FROM customers c
JOIN CustomerSpending cs ON c.CustomerID = cs.CustomerID
WHERE c.CityID = 1
ORDER BY cs.TotalSpent DESC;