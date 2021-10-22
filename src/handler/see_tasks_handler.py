import pyfiglet
import time

from PyInquirer import prompt
from prettytable import from_db_cursor
from printy import printy
from examples import custom_style_3

from questions.see_tasks import *
from database.tasks import *
from utils.interface import *


def show_top_five_tasks(db_conn):
    try:
        text = pyfiglet.figlet_format("Top 5 Tasks!")
        clear_screen()
        printy(text, "Br")

        tasks_cursor = get_top_five_tasks(db_conn)
        tasks_table = from_db_cursor(tasks_cursor)

        if len(list(tasks_table)) > 0:
            printy(tasks_table, "B")
            printy("Keep up the high spirit, you can do it!", "oB")
        else:
            printy("There is no tasks left for today :) Keep up the goodwork!", "nB")
    except Exception as err:
        printy(f"Failed to show top 5 task: {err}", "Br")
    finally:
        print("")


def handle_see_tasks(answer, db_conn):
    command = answer["main"].lower()
    if command == "see detail a task":
        ans = prompt(see_detail_a_task_questions, style=custom_style_3)
        handle_detail_task(ans, db_conn)
    elif command == "do a task":
        ans = prompt(do_a_task_questions, style=custom_style_3)
        handle_do_a_task(ans, db_conn)
    elif command == "update a task":
        ans = prompt(update_a_task_questions, style=custom_style_3)
        handle_update_task(ans, db_conn)
    elif command == "mark done a task":
        ans = prompt(mark_done_a_task_questions, style=custom_style_3)
        handle_mark_done_a_task(ans, db_conn)
    elif command == "back":
        time.sleep(0)


def handle_detail_task(answer, db_conn):
    try:
        task_id = answer["task_id"]
        task_cursor = get_detail_task(db_conn, task_id)
        task_table = from_db_cursor(task_cursor)
        if len(list(task_table)) > 0:
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
        print(input("Please press enter to back\n"))


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
