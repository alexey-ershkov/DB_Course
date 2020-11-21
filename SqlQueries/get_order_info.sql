select Dish, Count from BookingString BS
join Menu M on M.Number = BS.`Dish__Menu-Number`
where BS.Booking_ID = %s;