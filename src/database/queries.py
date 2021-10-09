CREATE_TASKS_TABLE = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name VARCHAR(55) NOT NULL,
        description TEXT,
        start_date TEXT NOT NULL,
        status VARCHAR(20) NOT NULL,
        importance INTEGER NOT NULL,
        urgency INTEGER NOT NULL,
        tags TEXT
    );
"""