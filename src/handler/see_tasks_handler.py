import time

from PyInquirer import prompt
from questions.see_tasks import *
from examples import custom_style_3


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
