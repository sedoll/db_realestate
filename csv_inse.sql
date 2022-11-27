-- SHOW VARIABLES LIKE 'secure_file%';
-- 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data1.csv'
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/apt.csv' 
INTO TABLE new_table
CHARACTER SET euckr
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dong, @address, @par_add, @sub_add, @name, @deal, @month, @day, @acount, @rent, @floor, @year, @cancellation, @property, @station_area)
SET dong = @dong,
	address = @address,
    par_add = @par_add,
    sub_add = @sub_add,
    name = @name,
    deal = @deal,
    month = @month,
    day = @day,
    acount = @acount,
    rent = @rent,
    floor = @floor,
    year = @year,
    cancellation = NULLIf(@cancellation,''),
    property = NULLIf(@property,''),
    station_area = NULLIf(@station_area,'');