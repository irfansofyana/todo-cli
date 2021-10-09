from __future__ import print_function, unicode_literals
from PyInquirer import prompt

from questions.main_menu import *
from questions.add_task import *
from questions.see_tasks import *

from handler.see_tasks_handler import *
from handler.add_task_handler import *

from examples import custom_style_3
from utils.interface import *
import pyfiglet
from printy import printy


def see_tasks():
    print_app_header()
    ans = prompt(see_tasks_questions, style=custom_style_3)
    handle_see_tasks(ans)


def add_task():
    print_app_header()
    ans = prompt(add_task_questions, style=custom_style_3)
    handle_add_task(ans)


def handle_command(comm):
    if comm == "exit":
        exit()
    elif comm == "see tasks":
        see_tasks()
    elif comm == "add task":
        add_task()


def print_app_header():
    app_header_text = pyfiglet.figlet_format("TODO-cli")
    clear_screen()
    printy(app_header_text, "bB")


if __name__ == "__main__":
    while 1:
        print_app_header()

        answer = prompt(main_menu_questions, style=custom_style_3)
        command = answer["main"].lower()
        handle_command(command)

        time.sleep(1)
