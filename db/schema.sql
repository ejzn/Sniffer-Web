CREATE TABLE PHONE(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   NAME           TEXT    NOT NULL,
   LAST_COM       datetime default current_timestamp
);

CREATE TABLE ACTIVITY(
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   ACTION           TEXT    NOT NULL,
   CATEGORY           TEXT    NOT NULL,
   COMPONENT           TEXT    NOT NULL,
   DETAILS TEXT,
   TIMESTAMP       datetime default current_timestamp,
   PHONE INT NOT NULL,
   FOREIGN KEY(PHONE) REFERENCES phone(ID)
);
