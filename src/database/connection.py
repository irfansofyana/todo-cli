import sqlite3
from queries import *


def get_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn, None
    except Exception as err:
        return None, err


if __name__ == "__main__":
    conn, _ = get_connection("../../db/tasks-dummy.db")
    conn.execute(CREATE_TASKS_TABLE)
    conn.close()
