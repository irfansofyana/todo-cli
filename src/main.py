from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from questions.main_menu import *
from questions.add_task import *
from questions.see_tasks import *

from handler.see_tasks_handler import *
from handler.add_task_handler import *

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


def see_tasks(db_conn):
    show_top_five_tasks(db_conn)

    ans = prompt(see_tasks_questions, style=custom_style_3)
    handle_see_tasks(ans)


def add_task(db_conn):
    print_app_header()

    ans = prompt(add_task_questions, style=custom_style_3)
    handle_add_task(db_conn, ans)


def handle_command(comm, db_conn):
    if comm == "exit":
        exit()
    elif comm == "see tasks":
        see_tasks(db_conn)
    elif comm == "add task":
        add_task(db_conn)


def print_app_header():
    app_header_text = pyfiglet.figlet_format("TODO-cli")
    clear_screen()
    printy(app_header_text, "bB")


def init_db():
    db_path = os.getenv("DATABASE_PATH")
    if len(db_path) == 0 or db_path is None:
        db_path = 'tasks.db'
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

        answer = prompt(main_menu_questions, style=custom_style_3)
        command = answer["main"].lower()
        handle_command(command, db_conn)

        time.sleep(0.1)
