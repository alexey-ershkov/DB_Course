SELECT m.Number, m.Name, m.Surname, m.DateOfBirth, m.Passport, m.StartWork, m.EndWork FROM Manager m
LEFT JOIN(
    SELECT b.ID, b.Manager__Number FROM Booking b
    WHERE YEAR(b.DateTime) = 2013 AND MONTH(b.DateTime) = 3
)test
ON test.Manager__Number = m.Number
WHERE test.ID IS NULL;