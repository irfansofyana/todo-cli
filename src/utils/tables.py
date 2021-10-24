import prettytable
from prettytable import ALL as ALL
from prettytable import DOUBLE_BORDER

def format_text(text, max_line_length=20):
    ACC_length = 0
    words = text.split(" ")
    formatted_text = ""
    for word in words:
        if ACC_length + (len(word) + 1) <= max_line_length:
            formatted_text = formatted_text + word + " "
            ACC_length = ACC_length + len(word) + 1
        else:
            formatted_text = formatted_text + "\n" + word + " "
            ACC_length = len(word) + 1
    return formatted_text

def create_pretty_tables(tables):
    items_table = prettytable.PrettyTable(hrules=ALL)
    header_columns = [key for key in tables[0]]
    items_table.field_names = header_columns
    for row in tables:
        for key in row:
            row[key] = format_text(str(row[key]), max_line_length=15)
        items_table.add_row([row[key] for key in row])
    items_table.set_style(DOUBLE_BORDER)
    return items_table
