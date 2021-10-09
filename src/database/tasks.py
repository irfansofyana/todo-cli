class Task:
    def __init__(self, name, description, start_date, importance, urgency, tags, id=None, status="IN PROGRESS"):
        self.id = id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.status = status
        self.importance = importance
        self.urgency = urgency
        self.tags = ",".join(tags)

    def form_insert_query_tuple(self):
        return (
            self.name,
            self.description,
            self.start_date,
            self.status,
            self.importance,
            self.urgency,
            self.tags,
        )

def convert_row_tuple_to_task(row_tuple):
    t = Task(
        row_tuple[1],
        row_tuple[2],
        row_tuple[3],
        row_tuple[5],
        row_tuple[6],
        row_tuple[7],
        row_tuple[0],
        row_tuple[4],
    )
    return t

def get_all_tasks(conn):
    query = """
        SELECT *
        FROM tasks
    """
    tasks = []
    for row in conn.execute(query):
        task = convert_row_tuple_to_task(row)
        tasks.append(task)
    return tasks

def get_top_five_tasks(conn):
    query = """
        SELECT id, name, description, start_date
        FROM tasks
        LIMIT 5
    """
    rows = conn.execute(query)
    return rows

def insert_task(conn, task):
    query = """
        INSERT INTO tasks(
            name,
            description,
            start_date,
            status,
            importance,
            urgency,
            tags
        )
        VALUES (?,?,?,?,?,?,?)
    """
    conn.execute(query, task.form_insert_query_tuple())
    conn.commit()
