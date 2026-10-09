import tkinter as tk
from tkinter import messagebox

File_Name = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(File_Name, "r") as 
file:
            for task in file:
                task = task.strip()
                if task:

task_list.insert(tk.END, task)
    except FileNotFoundError
         pass

# Save tasks to file 
def save_tasks():
    with open(File_Name, "w") as 
file:
         task = task_list.get(0, tk. END)
                for task in tasks:
                    file.write(task + "\n")

# Add task
def add_task():
    task = task_entry.get().strip()

    if task == "":

messagebox.showwarning("warning", "Please enter a tasks!")
    else:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_task()

# Delete selected task 
def delete_task():
    try:
        selected_task = task_list.delete(selected_task)
        save_task()
        expect IndexError:

messagebox.showwarning("Warning", "Please select a task!")


# Clear all task
def clear_task():
    if task_list.size() == 0;
        messagebox.showinfo("Info", "No task to clear")
        else:
            result = messagebox.askeysno(
                                   "Confirm"
                                    "Are you sure you want to delete all tasks?"
                             )

                             if result:
                                task_list.delete(0, tk.END)
                                save_task()

# Main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="My To-Do List"
    font=("Arial", 22, "bold")
)
heading.pack(pady=20)

# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    command=add_task
)
add_button.pack(pady=5)

# Delete button
clear_button = tk.Button(
    root,
    text="Delete Selected",
    font=("Arial", 12),
    command=clear_tasks
)
clear_button.pack(pady=5)

# Load saved task
load_task()

# Rum application
root.mainloop()
