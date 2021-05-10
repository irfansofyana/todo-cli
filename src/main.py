from __future__ import print_function, unicode_literals

import time

from PyInquirer import prompt

from questions.main_menu import *
from questions.add_task import *

from examples import custom_style_3
from utils.interface import *

import pyfiglet
from printy import printy


def see_tasks():
    clear_screen()
    print("Dummy")


def add_task():
    clear_screen()
    print_app_header()

    ans = prompt(add_task_questions, style=custom_style_3)
    task_name = ans['task_name']
    task_description = ans['task_description']
    task_tags = ans['task_tags']
    task_date = ans['task_date']

    print(task_name, task_description, task_tags, task_date)


def handle_command(comm):
    if comm == 'exit':
        exit()
    elif comm == 'see tasks':
        see_tasks()
    elif comm == 'add task':
        add_task()


def print_app_header():
    app_header_text = pyfiglet.figlet_format('TODO-cli')
    printy(app_header_text, 'bB')


if __name__ == "__main__":
    clear_screen()
    while 1:
        print_app_header()

        answer = prompt(main_menu_questions, style=custom_style_3)
        command = answer['main'].lower()
        handle_command(command)

        time.sleep(1)
        clear_screen()
