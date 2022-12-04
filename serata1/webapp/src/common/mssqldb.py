import pandas as pd
import pyodbc
from webapp.src.common.config import settings

def connect(db_config: dict = settings.MS_DB_CONFIG)
    """Connect to a MS SQL Server

    Args:
        db_config [dict]: dictionary containing the connection parameters (defined into settings)

    Returns:
        pyodbc.Connection: connection object

    """
    conn_str = ("Driver={SQL Server Native Client 11.0};"
            f"Server={db_config['host']},{db_config['port']};"
            f"Database={db_config['dbname']};"
            "Trusted_Connection=yes;"
            f"UID={db_config['user']};"
            f"PWD={db_config['port']};")
    
    conn = pyodbc.connect(conn_str)
    return conn

def launch_query(conn: pyodbc.connect, query:str = "SELECT 1"):
    
    # create cursor
    cursor = conn.cursor()
    # launch query
    res = cursor.execute("query")
    if res:
        return True
    else: 
        return False

def extract_data(conn: pyodbc.connect, query: str = "SELECT 1", pandas: bool = True):
    """Extract data from a MS SQL Server

    Args:
        conn: connection object
        query: query to execute

    Returns:
        list: list of rows

    """
    # create cursor
    cursor = conn.cursor()
    # launch query
    cursor.execute(query)
    # extract data
    if pandas:
        data = pd.read_sql("SELECT TOP(1000) * FROM customers", conn)
    else:
        data = cursor.fetchall()
    return data

def insert_login_data(conn: pyodbc.connect, username: str, password: str):
    cursor = conn.cursor()

    cursor.execute(f"""
                INSERT INTO users (username, password)
                VALUES
                ({username}, {password})
                """)
    res = conn.commit()
    if res:
        return True
    else:
        return False