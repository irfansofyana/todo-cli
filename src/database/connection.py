import sqlite3


def get_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn, None
    except Exception as err:
        return None, err
