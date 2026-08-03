import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do List")
root.geometry("300x400")

bg_color = "#2b2b2b"
button_bg = "#3c3f41"
text_color = "#ffffff"

root.configure(bg=bg_color)

task_input = tk.Entry(root, bg=button_bg, fg=text_color, insertbackground=text_color)
task_input.pack(pady=10)

def add_task():
    addedTask = task_input.get()
    if addedTask.strip():
        task_list.insert(tk.END, addedTask)
        task_input.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def remove_task():
    selectedTask = task_list.curselection()
    if selectedTask:
        task_list.delete(selectedTask)
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

add_button = tk.Button(root, text="Add Task", command=add_task, bg=button_bg, fg=text_color)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg=button_bg, fg=text_color)
remove_button.pack(pady=5)

list_frame = tk.Frame(root, bg=bg_color)
list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

task_scroll = tk.Scrollbar(list_frame)
task_scroll.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(list_frame, yscrollcommand=task_scroll.set, bg=button_bg, fg=text_color, selectbackground="#5285a6")
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

task_scroll.config(command=task_list.yview)

root.mainloop()