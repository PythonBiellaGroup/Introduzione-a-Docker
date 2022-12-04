from typing import Any
import mysql.connector
from mysql.connector import Error
from webapp.src.common.config import settings

def mysql_connect(db_config: dict = settings.DB_CONFIG) -> Any:
        """
        Default mysql connection without sqlalchemy
        """
        try:
            engine = mysql.connector.connect(
                host=db_config["host"],
                user=db_config["user"],
                password=db_config["password"],
                port=db_config["port"],
                database=db_config["dbname"],
            )
            if engine.is_connected():
                db_Info = engine.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = engine.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                cursor.close()
                engine.close()

            return engine
        except Error as e:
            print("Error while connecting to MySQL", e)

def create_table(engine: Any):
    try:
        mySql_Create_Table_Query = """CREATE TABLE Users ( 
                            Id int(11) NOT NULL,
                            Name varchar(250) NOT NULL,
                            Password varchar(250) NOT NULL,
                            PRIMARY KEY (Id)) """

        cursor = engine.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("Laptop Table created successfully ")
        cursor.close()
        engine.close()
        return True
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))



def insert_login_data(engine: Any, name: str, password: str):
    try:
        
        mySql_insert_query = """INSERT INTO Users (Name, Password) 
                                VALUES (%s, %s) """

        record = (name, password)
        cursor = engine.cursor()
        cursor.execute(mySql_insert_query, record)
        engine.commit()
        print("Record inserted successfully into Laptop table")
        cursor.close()
        engine.close()
        return True
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))
