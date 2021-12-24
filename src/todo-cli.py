from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from pathlib import Path

from questions.main_menu import *
from questions.add_task import *
from questions.see_tasks import *

from handler.tasks import *

from database.connection import get_connection
from database.queries import *

from examples import custom_style_3
from utils.interface import *
from printy import printy

import pyfiglet
import os
import sys
from dotenv import load_dotenv

load_dotenv()


def see_uncompleted_tasks(db_conn):
    handle_see_uncompleted_tasks(db_conn)


def see_detail_task(db_conn):
    ans = prompt(see_detail_a_task_questions, style=custom_style_3)
    handle_detail_task(ans, db_conn)


def add_task(db_conn):
    print_app_header()

    ans = prompt(add_task_questions, style=custom_style_3)
    handle_add_task(db_conn, ans)


def do_task(db_conn):
    ans = prompt(do_a_task_questions, style=custom_style_3)
    handle_do_a_task(ans, db_conn)


def finish_task(db_conn):
    ans = prompt(mark_done_a_task_questions, style=custom_style_3)
    handle_mark_done_a_task(ans, db_conn)


def update_task(db_conn):
    ans = prompt(update_a_task_questions, style=custom_style_3)
    handle_update_task(ans, db_conn)


def handle_command(comm, db_conn):
    if comm == "exit":
        sys.exit()
    elif comm == "see detail task":
        see_detail_task(db_conn)
    elif comm == "see all uncompleted tasks":
        see_uncompleted_tasks(db_conn)
    elif comm == "add task":
        add_task(db_conn)
    elif comm == "do task":
        do_task(db_conn)
    elif comm == "finish task":
        finish_task(db_conn)
    elif comm == "update task":
        update_task(db_conn)
    elif comm == "delete task":
        pass


def print_app_header():
    app_header_text = pyfiglet.figlet_format("TODO-cli")
    clear_screen()
    printy(app_header_text, "bB")


def init_db():
    path = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(path, 'database.db')
    db_conn, err = get_connection(db_path)

    if err is not None:
        print("Can't connect to database: ", err)
        return None

    init_db_tables(db_conn)

    return db_conn


def init_db_tables(db_conn):
    db_conn.execute(CREATE_TASKS_TABLE)
    db_conn.commit()


if __name__ == "__main__":
    db_conn = init_db()
    if db_conn is None:
        sys.exit()

    while 1:
        print_app_header()
        
        show_top_five_tasks(db_conn)
        
        answer = prompt(main_menu_questions, style=custom_style_3)
        command = answer["main"].lower()
        handle_command(command, db_conn)

        time.sleep(0.1)
