import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.task_entry = tk.Entry(root)
        self.task_entry.pack(padx=10, pady=(0, 10), fill=tk.X, expand=True)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=10, pady=(0, 5), side=tk.LEFT)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=10, pady=(0, 5), side=tk.LEFT)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks.pop(task_index)
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
