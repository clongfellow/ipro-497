CREATE DATABASE IF NOT EXISTS ipro_db;
USE ipro_db;
DROP TABLE processes;

CREATE TABLE processes(
    ID INT NOT NULL AUTO_INCREMENT ,
    PROCESS_ID INT NOT NULL,
    SESSION_NAME TEXT,
    SESSION_NUMBER TEXT,
    MEM_USAGE TEXT,
    PROCESS_NAME TEXT,
    TIME_STAMP TEXT,
    PRIMARY KEY (ID)
);

INSERT INTO processes (PROCESS_ID, SESSION_NAME, SESSION_NUMBER, MEM_USAGE, PROCESS_NAME, TIME_STAMP) VALUES(
	-- example data, later will need to get data formatted from .csv file from front-end
    500,
    "CONSOLE",
    "1",
    "500kb",
    "TEST.EXE",
    "1/24/2022"
);

SELECT * FROM processes;
