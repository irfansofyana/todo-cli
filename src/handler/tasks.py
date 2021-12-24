from database.tasks import *
from printy import printy
from PyInquirer import prompt
from prettytable import from_db_cursor
from printy import printy
from examples import custom_style_3
from questions.see_tasks import *
from database.tasks import *
from utils.interface import *
from utils.tables import create_pretty_tables

import pyfiglet
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


def show_top_five_tasks(db_conn):
    try:
        text = pyfiglet.figlet_format("Top 5 Tasks!")
        clear_screen()
        printy(text, "Br")

        tasks = get_top_five_tasks(db_conn)

        if len(tasks) > 0:
            tasks_table = create_pretty_tables(tasks)
            printy(tasks_table, "B")
            printy("Keep up the high spirit, you can do it!", "oB")
        else:
            printy("There is no tasks left for today :) Keep up the goodwork!", "nB")
    except Exception as err:
        printy(f"Failed to show top 5 task: {err}", "Br")
    finally:
        print("")

def handle_see_uncompleted_tasks(db_conn):
    try:
        tasks = get_uncompleted_tasks(db_conn)

        if len(tasks) > 0:
            tasks_table = create_pretty_tables(tasks)
            printy(tasks_table, "B")
        else:
            msg = f"Good job! all tasks are completed."
            printy(msg, "Br")
    except Exception as err:
        printy(f"Failed to show all uncompleted tasks: {err}", "Br")
    finally:
        print(input("\nPlease press enter to back\n"))

def handle_detail_task(answer, db_conn):
    try:
        task_id = answer["task_id"]
        task = get_detail_task(db_conn, task_id)

        if len(task) > 0:
            task_table = create_pretty_tables(task)
            printy(task_table, "B")
        else:
            msg = f"Sorry, task with ID = {task_id} is not found"
            printy(msg, "Br")
    except Exception as err:
        printy(f"Failed to show detail task: {err}", "Br")
    finally:
        print(input("\nPlease press enter to back\n"))


def handle_do_a_task(answer, db_conn):
    try:
        task_id = answer["task_id"]
        rowcount = do_a_task(db_conn, task_id)

        if rowcount > 0:
            printy("Now, task is In Progress. Go make it done!", "nB")
        else:
            msg = f"Sorry, task with ID = {task_id} is not found"
            printy(msg, "Br")
    except Exception as err:
        printy(f"Failed to update the status of the task: {err}", "Br")
    finally:
        print(input("\nPlease press enter to back\n"))


def handle_update_task(answer, db_conn):
    try:
        task = Task(
            name=answer["task_name"],
            description=answer["task_description"],
            start_date=answer["task_date"],
            tags=answer["task_tags"],
            id=answer["task_id"],
        )
        rowcount = update_task(db_conn, task)

        if rowcount > 0:
            printy("Task updated successfully!", "nB")
        else:
            msg = f"Sorry, task with ID = {task_id} is not found"
            printy(msg, "Br")
    except Exception as err:
        printy(f"Failed to update task: {err}", "Br")
    finally:
        print(input("\nPlease press enter to back\n"))


def handle_mark_done_a_task(answer, db_conn):
    try:
        task_id = answer["task_id"]
        rowcount = mark_done_task(db_conn, task_id)

        if rowcount > 0:
            printy("Task updated successfully!", "nB")
        else:
            msg = f"Sorry, task with ID = {task_id} is not found"
            printy(msg, "Br")
    except Exception as err:
        printy(f"Failed to update the status of the task: {err}", "Br")
    finally:
        print(input("\nPlease press enter to back\n"))
