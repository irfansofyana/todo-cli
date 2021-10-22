from utils.validation import *

see_tasks_questions = [
    {
        "type": "list",
        "name": "main",
        "message": "What do you want to do?",
        "choices": [
            "See detail a task",
            "Do a task",
            "Update a task",
            "Mark done a task",
            "Back",
        ],
    }
]

see_detail_a_task_questions = [
    {"type": "input", "name": "task_id", "message": "What's the task ID?"}
]

update_a_task_questions = [
    {"type": "input", "name": "task_id", "message": "What's the task ID?"},
    {
        "type": "input",
        "name": "task_name",
        "message": "What's the new name of the task?",
        "validate": lambda val: len(val) > 0,
    },
    {
        "type": "input",
        "name": "task_description",
        "message": "Please write the new description of the task",
    },
    {
        "type": "checkbox",
        "name": "task_tags",
        "message": "Select the new tag(s) for the task",
        "choices": [
            {"name": "Work"},
            {"name": "Study"},
            {"name": "Organization"},
            {"name": "Etc"},
        ],
    },
    {
        "type": "input",
        "name": "task_date",
        "message": "What date does this task start? (yyyy-mm-dd)",
        "validate": lambda val: validate_time(val),
    },
]

mark_done_a_task_questions = [
    {"type": "input", "name": "task_id", "message": "What's the task ID?"}
]

do_a_task_questions = [
    {"type": "input", "name": "task_id", "message": "What's the task ID?"}
]

back_question = [
    {
        "type": "list",
        "name": "main",
        "message": "What do you want to do?",
        "choices": ["Back"],
    }
]
