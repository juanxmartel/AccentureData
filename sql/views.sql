CREATE OR REPLACE VIEW V_SalesOverview AS
SELECT
    s.SalesID,
    s.SalesDate,
    p.ProductName,
    cat.CategoryName,
    s.Quantity,
    s.TotalPrice,
    CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName,
    ci.CityName,
    co.CountryName,
    CONCAT(e.Firstname, ' ', e.LastName) AS SalesPersonName
FROM sales s
JOIN products p ON s.ProductID = p.ProductID
JOIN categories cat ON p.CategoryID = cat.CategoryID
JOIN customers c ON s.CustomerID = c.CustomerID
JOIN employees e ON s.SalesPersonID = e.EmployeeID
JOIN cities ci ON c.CityID = ci.CityID
JOIN countries co ON ci.CountryID = co.CountryID;