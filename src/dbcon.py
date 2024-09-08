import pyodbc


def get_db_connection():
    server = "AHMADBABA\MSSQLSERVER01"  # e.g., 'localhost\\SQLEXPRESS'
    database = "chatbot_db"
    username = "sa"
    password = "a"
    driver = "{ODBC Driver 17 for SQL Server}"

    connection_string = f"""
    DRIVER={driver};
    SERVER={server};
    DATABASE={database};
    UID={username};
    PWD={password};
    """

    try:
        conn = pyodbc.connect(connection_string)
        print("db connected")
    except Exception as e:
        print(e)
        print("not connected")

    return conn
