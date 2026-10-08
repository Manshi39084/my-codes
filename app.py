import tkinter as tk
from tkinter import messagebox

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for task in file:
                task = task.strip()
                if task:
                    task_list.insert(tk.END, task)
    except FileNotFoundError:
        pass


# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        tasks = task_list.get(0, tk.END)

        for task in tasks:
            file.write(task + "\n")


# Add task
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()


# Delete selected task
def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")


# Clear all tasks
def clear_tasks():
    if task_list.size() == 0:
        messagebox.showinfo("Info", "No tasks to clear.")
    else:
        result = messagebox.askyesno(
            "Confirm",
            "Delete all tasks?"
        )

        if result:
            task_list.delete(0, tk.END)
            save_tasks()


# Main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.resizable(False, False)


# Heading
heading = tk.Label(
    root,
    text="My To-Do List",
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)


# Task entry
task_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=35
)
task_entry.pack(pady=10)


# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    command=add_task
)
add_button.pack(pady=5)


# Task list
task_list = tk.Listbox(
    root,
    font=("Arial", 13),
    width=40,
    height=12
)
task_list.pack(pady=15)


# Delete button
delete_button = tk.Button(
    root,
    text="Delete Selected",
    font=("Arial", 12),
    command=delete_task
)
delete_button.pack(pady=5)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear All",
    font=("Arial", 12),
    command=clear_tasks
)
clear_button.pack(pady=5)


# Load saved tasks
load_tasks()


# Run application
root.mainloop()