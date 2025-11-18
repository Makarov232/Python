import tkinter as tk
from datetime import datetime
import os

PAST_COLOR = "red"
NOW_COLOR = "orange"
FUTURE_COLOR = "lightgray"

def load_tasks(filename):
    tasks = []
    if not os.path.exists(filename):
        return tasks

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or ";" not in line:
                continue
            name, date_str = line.split(";", 1)
            if date_str.lower() == "now":
                date = "now"
            else:
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    continue
            tasks.append((name, date))
    return tasks

def describe_task(name, date):
    today = datetime.today().date()
    if date == "now":
        return f"Прямо щаз происходит {name}", NOW_COLOR
    delta = (date - today).days
    if delta > 0:
        return f"Осталось {delta} дней до {name}", FUTURE_COLOR
    elif delta < 0:
        return f"Прошло {abs(delta)} дней от {name}", PAST_COLOR
    else:
        return f"Прямо щаз происходит {name}", NOW_COLOR

def show_tasks():
    root = tk.Tk()
    root.title("Что мне делать, как мне жить?")

    root.configure(bg="black")

    title = tk.Label(root, text="Мои текущие задачи", font=("Arial", 24, "bold"), fg="yellow", bg="black")
    title.pack(pady=10)

    tasks = load_tasks("/Users/makarov/Downloads/js/python/tkinter/tasks.txt")

    for name, date in tasks:
        text, color = describe_task(name, date)
        label = tk.Label(root, text=text, font=("Arial", 14), fg=color, bg="black")
        label.pack(anchor="w", padx=20)

    root.mainloop()

show_tasks()
