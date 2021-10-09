import time
import pyfiglet

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

    tasks = get_top_five_tasks(db_conn)
    tasks_table = from_db_cursor(tasks)
    printy(tasks_table, "B")

def handle_see_tasks(answer):
    command = answer["main"].lower()
    if command == "see detail a task":
        ans = prompt(see_detail_a_task_questions, style=custom_style_3)
        handle_detail_task(ans)
    elif command == "update a task":
        ans = prompt(update_a_task_questions, style=custom_style_3)
        handle_update_task(ans)
    elif command == "mark done a task":
        ans = prompt(mark_done_a_task_questions, style=custom_style_3)
        handle_mark_done_a_task(ans)
    elif command == "back":
        time.sleep(0)


def handle_detail_task(answer):
    print(answer)
    print(input("Please press enter to back\n"))


def handle_update_task(answer):
    print(answer)
    print(input("Please press enter to back\n"))


def handle_mark_done_a_task(answer):
    print(answer)
    print(input("Please press enter to back\n"))
