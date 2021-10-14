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
    print("")


def handle_see_tasks(answer, db_conn):
    command = answer["main"].lower()
    if command == "see detail a task":
        ans = prompt(see_detail_a_task_questions, style=custom_style_3)
        handle_detail_task(ans, db_conn)
    elif command == "update a task":
        ans = prompt(update_a_task_questions, style=custom_style_3)
        handle_update_task(ans)
    elif command == "mark done a task":
        ans = prompt(mark_done_a_task_questions, style=custom_style_3)
        handle_mark_done_a_task(ans)
    elif command == "back":
        time.sleep(0)


def handle_detail_task(answer, db_conn):
    task_id = answer['task_id']
    task_cursor = get_detail_task(db_conn, task_id)
    task_table = from_db_cursor(task_cursor)
    if len(list(task_table)) > 0:
        printy(task_table, "B")
    else:
        msg = f"Sorry coudln't find the task with ID = {task_id}"
        printy(msg, "Br")
    print(input("\nPlease press enter to back\n"))


def handle_update_task(answer):
    print(answer)
    print(input("Please press enter to back\n"))


def handle_mark_done_a_task(answer):
    print(answer)
    print(input("Please press enter to back\n"))
