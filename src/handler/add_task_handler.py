from database.tasks import *

def handle_add_task(db_conn, ans):
    try:
        task = Task(
            ans["task_name"],
            ans["task_description"],
            ans["task_date"],
            ans["task_importance"],
            ans["task_urgency"],
            ans["task_tags"]
        )
        insert_task(db_conn, task)
        print("Successfully add task to DB!")
    except Exception as err:
        print("Failed to add task to DB: ", err)
