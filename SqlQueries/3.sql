SELECT * FROM Manager m
WHERE m.DateOfBirth IN (
    SELECT MAX(mnr.DateOfBirth) from Manager mnr
);