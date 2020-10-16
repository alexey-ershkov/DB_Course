create table Manager
(
	Number int not null
		primary key,
	Name varchar(255) not null,
	Surname varchar(255) not null,
	DateOfBirth date not null,
	Passport int not null,
	StartWork date not null,
	EndWork date null
);

create table Docs
(
	id int auto_increment
		primary key,
	doc_year int not null,
	doc_month int not null,
	Manager int not null,
	OrderNumbers int not null,
	Summary int not null,
	constraint Docs_Manager_Number_fk
		foreign key (Manager) references Manager (Number)
);

create table Menu
(
	Number int not null
		primary key,
	Dish varchar(255) not null,
	Cost int not null,
	`Weight(grams)` int not null
);

create table Room
(
	Number int not null
		primary key,
	Name varchar(255) not null,
	Places int not null
);

create table Booking
(
	ID int auto_increment
		primary key,
	DateTime datetime not null,
	Participants int not null,
	`Pre-Cost` int not null,
	RealCost int null,
	`Pre-Payment` int null,
	Manager__Number int null,
	Room__Number int null,
	constraint Order_Manager_Number_fk
		foreign key (Manager__Number) references Manager (Number),
	constraint Order_Room_Number_fk
		foreign key (Room__Number) references Room (Number)
);

create table BookingString
(
	ID int auto_increment
		primary key,
	Booking_ID int not null,
	`Dish__Menu-Number` int not null,
	Count int not null,
	constraint OrderString_Menu_Number_fk
		foreign key (`Dish__Menu-Number`) references Menu (Number),
	constraint OrderString_Order_ID_fk
		foreign key (Booking_ID) references Booking (ID)
);

CREATE PROCEDURE Documentation(doc_year int, doc_month int)
BEGIN
    DECLARE Manager_ID, BookingCount, Summary int;
    DECLARE done int default 0;
    DECLARE exist int default 0;
    DECLARE affect int default 0;
    DECLARE doc CURSOR FOR
        SELECT M.Number, COUNT(B.ID), SUM(B.RealCost) FROM Manager M
        JOIN Booking B on M.Number = B.Manager__Number
        WHERE YEAR(B.DateTime) = doc_year AND MONTH(B.DateTime) = doc_month
        GROUP BY M.Number;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
    SELECT COUNT(*) into exist FROM Docs D
    WHERE D.doc_year = doc_year AND D.doc_month = doc_month;
    IF (exist = 0) THEN
        OPEN doc;
        REPEAT
            FETCH doc INTO Manager_ID, BookingCount, Summary;
            IF (done=0) THEN
                SELECT 1 INTO affect;
                INSERT INTO Docs VALUES (NULL, doc_year, doc_month, Manager_ID, BookingCount, Summary);
            END IF;
        UNTIL done=1 END REPEAT;
        CLOSE doc;
        IF (affect = 1) THEN
            SELECT 'Отчет успешно создан' AS 'Статус';
        ELSE
            SELECT 'В данный месяц не было заказов' AS 'Статус';
        END IF;
    ELSE
        SELECT 'Такой отчет уже сущствует' AS 'Статус';
    END IF;
END;