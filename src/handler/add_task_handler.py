from database.tasks import *
from printy import printy

import time


def handle_add_task(db_conn, ans):
    try:
        task = Task(
            ans["task_name"],
            ans["task_description"],
            ans["task_date"],
            ans["task_importance"],
            ans["task_urgency"],
            ans["task_tags"],
        )
        insert_task(db_conn, task)
        printy("Task added. Go for it!", "n>B")
        time.sleep(1)
    except Exception as err:
        printy(f"Failed to add tasks to DB: {err}", "Br")
        time.sleep(1)
