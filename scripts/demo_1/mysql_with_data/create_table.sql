USE be_db;
START TRANSACTION;
CREATE TABLE IF NOT EXISTS avg_rates ( id INT NOT NULL AUTO_INCREMENT
                                     , Paese VARCHAR(256) 
                                     , Valuta VARCHAR(256)
                                     , CodiceISO VARCHAR(3)
                                     , CodiceUIC INT
                                     , Quotazionemedia FLOAT
                                     , Convenzionedicambio VARCHAR(256)
                                     , Anno INT 
                                     , Mese INT 
                                     , PRIMARY KEY (id)
                                     );
COMMIT;

