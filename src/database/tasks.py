class Task:
    def __init__(
        self,
        name="",
        description="",
        start_date="",
        tags=[],
        importance=0,
        urgency=0,
        id=None,
        status="TODO",
    ):
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

    def form_update_query_tuple(self):
        return (
            self.name,
            self.description,
            self.tags,
            self.start_date,
            self.id,
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


def get_detail_task(conn, task_id):
    query = """
        SELECT *
        FROM tasks
        WHERE id = ?
    """
    cursor = conn.cursor()
    cursor.execute(query, task_id)
    return cursor


def mark_done_task(conn, task_id):
    query = """
        UPDATE tasks
        SET status = 'DONE'
        WHERE id = ?
    """
    cursor = conn.cursor()
    cursor.execute(query, task_id)
    conn.commit()
    return cursor.rowcount


def get_top_five_tasks(conn):
    query = """
        SELECT id, name, description, start_date, status
        FROM tasks
        WHERE status != 'DONE'
        AND start_date <= DATE('now', 'localtime')
        ORDER BY start_date ASC, urgency DESC, importance DESC
        LIMIT 5
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor


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


def update_task(conn, task):
    query = """
        UPDATE tasks
        SET
            name = ?,
            description = ?,
            tags = ?,
            start_date = ?
        WHERE id = ?
    """
    conn.execute(query, task.form_update_query_tuple())
    conn.commit()
