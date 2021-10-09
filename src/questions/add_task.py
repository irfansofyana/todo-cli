from utils.validation import *

add_task_questions = [
    {
        "type": "input",
        "name": "task_name",
        "message": "What's the name of the task?",
        "validate": lambda val: len(val) > 0,
    },
    {
        "type": "input",
        "name": "task_description",
        "message": "Please write the description of the task",
    },
    {
        "type": "checkbox",
        "name": "task_tags",
        "message": "Select the tag(s) for the task",
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
    {
        "type": "input",
        "name": "task_importance",
        "message": "From 1-10, how important is this task?",
        "validate": lambda val: validate_importance(val),
    },
    {
        "type": "input",
        "name": "task_urgency",
        "message": "From 1-10, how urgent is this task?",
        "validate": lambda val: validate_urgency(val),
    },
]
