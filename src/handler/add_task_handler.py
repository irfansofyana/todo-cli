def handle_add_task(ans):
    task_name = ans['task_name']
    task_description = ans['task_description']
    task_tags = ans['task_tags']
    task_date = ans['task_date']

    print(task_name, task_description, task_tags, task_date)
    print(input("Please press enter to back\n"))