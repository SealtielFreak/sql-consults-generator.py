DROP TABLE IF EXISTS Client;
CREATE TABLE Client(
    IDClient            INT NOT NULL AUTO_INCREMENT UNIQUE,

    FirtsName           VARCHAR(16),
    SecondName          VARCHAR(16),

    DateRegister        DATETIME,

    LicensePlate        VARCHAR(8),
    CirculationCard     VARCHAR(8),

    PRIMARY KEY (IDClient, LicensePlate)
);

DROP TABLE IF EXISTS ChecketOut;
CREATE TABLE ChecketOut(
    ID                  INT NOT NULL AUTO_INCREMENT UNIQUE,

    IDClient            INT NOT NULL,
    DateCheck           DATETIME,
    
    PRIMARY KEY(ID, DateCheck),
    FOREIGN KEY(IDClient) REFERENCES Client(IDClient)
);

DROP TABLE IF EXISTS ChecketIn;
CREATE TABLE ChecketIn(
    ID                  INT NOT NULL AUTO_INCREMENT UNIQUE,

    IDClient            INT NOT NULL,
    DateCheck           DATETIME,
    
    PRIMARY KEY(ID, DateCheck),
    FOREIGN KEY(IDClient) REFERENCES Client(IDClient)
);

DROP TABLE IF EXISTS Checked;
CREATE TABLE Checked(
    ID                  INT NOT NULL AUTO_INCREMENT UNIQUE,

    IDCheckedIn         INT,
    IDCheckedOut        INT,
    
    PRIMARY KEY(ID),
    FOREIGN KEY(IDCheckedIn) REFERENCES ChecketIn(ID),
    FOREIGN KEY(IDCheckedOut) REFERENCES ChecketOut(ID)
);
