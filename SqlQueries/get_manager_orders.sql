select ID, name, Participants, `Pre-Payment` as PrePayment, RealCost, Room__Number  from Booking
where Manager__Number = %s;