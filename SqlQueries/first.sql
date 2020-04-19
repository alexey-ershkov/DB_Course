SELECT cast(b.DateTime as date) AS Date, r.Name, b.`Pre-Cost`, b.RealCost, m.Surname FROM Booking b
JOIN Room r ON b.Room__Number = r.Number
JOIN Manager m ON b.Manager__Number = m.Number
WHERE MONTH(b.DateTime) = 3 AND YEAR(b.DateTime) = 2017;
