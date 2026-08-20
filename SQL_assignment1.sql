use database1;

CREATE TABLE Employees (EmployeeID INT PRIMARY KEY,EmployeeName VARCHAR(100) NOT NULL,Department VARCHAR(50),Salary DECIMAL(10,2) CHECK (Salary >= 0),JoiningDate DATE);

SELECT name,year,selling_price,fuel FROM [dbo].['CAR DETAILS FROM CAR DEKHO$'];

SELECT * FROM [dbo].['CAR DETAILS FROM CAR DEKHO$'] WHERE fuel ='Diesel';

SELECT * FROM [dbo].['CAR DETAILS FROM CAR DEKHO$'] WHERE selling_price=600000;

SELECT * FROM [dbo].['CAR DETAILS FROM CAR DEKHO$'] WHERE owner ='Second Owner';