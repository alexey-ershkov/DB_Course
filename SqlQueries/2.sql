SELECT m.Number, m.Surname, COUNT(b.ID) AS Booking_Count, SUM(b.RealCost) AS Booking_Cost FROM Manager m
JOIN Booking b on m.Number = b.Manager__Number
WHERE YEAR (b.DateTime) = 2017 AND MONTH (b.DateTime) = 3
GROUP BY m.Number, m.Surname;