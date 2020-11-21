select ID, DateTime, Participants, `Pre-Cost` as PreCost, RealCost, `Pre-Payment` as PrePayment, Room__Number, name from Booking B
where B.Manager__Number = %s and B.ID = %s;