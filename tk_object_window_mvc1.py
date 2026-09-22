######################################################################
#
# Author: Michael Hughes
#
# Program: tk_object_window.py
#  
# Version: Demo 
#   
# Date: Sept 21, 2026
#
# Description: tkinter python object oriented window
#
# Language: Python3
#
######################################################################
#
#
print("Running:   tk_object_window.py . . . ")
#
#
print("  ")
print("  ")
#
import sys
print("Threads:  ", sys.thread_info)
print("Python:  ", sys.version)
print("Platform ID:  ", sys.platform)
print("Executable:  ", sys.executable)
#
print("  ")
print(" . . .  import tkinter as tk  . . . ")
print("  ")
#
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

print("  ")
print(" . . .  Verify  tk.TkVersion  . . . ")
print("  ")

print ("1 - tk.TkVersion = ", tk.TkVersion)
print ("2 - tk.TkVersion = ", tk.TkVersion)
print ("3 - tk.TkVersion = ", tk.TkVersion)

print("  ")
print("  ")

print(" . . .  main and mainloop implementation . . . ")
print("  ")
print(" . . .  Todo List - MVC Example - tk_object_window_mvc1")
print("  ")

import tkinter as tk

class TodoModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

class TodoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.controller.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

    def update_task_list(self, tasks):
        self.task_listbox.delete(0, tk.END)
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

    def get_task_input(self):
        return self.task_entry.get()

    def clear_task_input(self):
        self.task_entry.delete(0, tk.END)

class TodoController:
    def __init__(self, root):
        self.root = root
        self.model = TodoModel()
        self.view = TodoView(root, self)

    def add_task(self):
        task = self.view.get_task_input()
        if task.strip():
            self.model.add_task(task)
            self.view.update_task_list(self.model.get_tasks())
            self.view.clear_task_input()

def main():
    root = tk.Tk()
    root.title("Todo List - MVC Example - tk_object_window_mvc1")
    root.geometry("400x300")
    root.resizable(False, False)

    app = TodoController(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# class App(tk.Tk):
#   def __init__(self, arg1):
#     self.arg1 = arg1	
#     super().__init__()
#    # configure the root window
#     self.title("Application Name: tk_object_window_mvc1")
