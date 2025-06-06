DELIMITER $$
CREATE PROCEDURE SP_GetProductSales(IN p_ProductID INT)
BEGIN
    SELECT
        p.ProductName,
        SUM(s.Quantity) AS TotalQuantitySold,
        SUM(s.TotalPrice) AS TotalRevenue
    FROM sales s
    JOIN products p ON s.ProductID = p.ProductID
    WHERE s.ProductID = p_ProductID
    GROUP BY p.ProductName;
END$$
DELIMITER ;