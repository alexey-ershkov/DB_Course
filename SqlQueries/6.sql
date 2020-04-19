SELECT r.Number, r.Name, r.Places FROM room2017 rv
JOIN Room r ON r.Number = rv.RoomNumber
WHERE rv.Times IN (
    SELECT MAX(rov.Times) FROM room2017 rov
);