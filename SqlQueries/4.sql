SELECT DISTINCT m.Number, m.Name, m.Surname, m.DateOfBirth, m.Passport, m.StartWork, m.EndWork FROM Manager m
LEFT JOIN Booking b on m.Number = b.Manager__Number
WHERE b.ID IS NULL;