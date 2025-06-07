DELIMITER $$
CREATE PROCEDURE SP_GetProductSales_V2(IN p_ProductID INT)
BEGIN
    SELECT
        p.ProductName,
        IFNULL(SUM(s.Quantity), 0) AS TotalQuantitySold,
        IFNULL(SUM(s.TotalPrice), 0) AS TotalRevenue
    FROM products p
    LEFT JOIN sales s ON p.ProductID = s.ProductID
    WHERE p.ProductID = p_ProductID
    GROUP BY p.ProductName;
END$$
DELIMITER ;