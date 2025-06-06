-- esta query devuelve el top 3 productos más vendidos por categoría
SELECT
    CategoryName,
    ProductName,
    TotalQuantity,
    ProductRank
FROM (
    SELECT
        c.CategoryName,
        p.ProductName,
        SUM(s.Quantity) AS TotalQuantity,
        RANK() OVER (PARTITION BY c.CategoryName ORDER BY SUM(s.Quantity) DESC) AS ProductRank
    FROM sales s
    JOIN products p ON s.ProductID = p.ProductID
    JOIN categories c ON p.CategoryID = c.CategoryID
    GROUP BY c.CategoryName, p.ProductName
) AS RankedProducts
WHERE ProductRank <= 3;