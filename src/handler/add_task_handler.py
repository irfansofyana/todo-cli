from database.tasks import *
from printy import printy

import time


def handle_add_task(db_conn, ans):
    try:
        task = Task(
            name=ans["task_name"],
            description=ans["task_description"],
            start_date=ans["task_date"],
            tags=ans["task_tags"],
            importance=ans["task_importance"],
            urgency=ans["task_urgency"],
        )
        insert_task(db_conn, task)
        printy("Task added. Go for it!", "n>B")
    except Exception as err:
        printy(f"Failed to add tasks to DB: {err}", "Br")
    finally:
        time.sleep(1)
