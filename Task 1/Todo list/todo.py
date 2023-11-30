from tkinter import *
from tkinter import messagebox

class TodoList:
    def _init_(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('400x400')

        self.tasks = []

        self.label = Label(self.root, text='To-Do List', font=('Arial', 18))
        self.label.pack(pady=10)

        self.task_entry = Entry(self.root, font=('Arial', 14))
        self.task_entry.pack(pady=10)

        self.add_button = Button(self.root, text='Add Task', command=self.add_task)
        self.add_button.pack(pady=5)

        self.listbox = Listbox(self.root, font=('Arial', 12), selectmode=SINGLE)
        self.listbox.pack(pady=10)

        self.complete_button = Button(self.root, text='Mark Complete', command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = Button(self.root, text='Delete Task', command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.show_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.show_tasks()
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning('Warning', 'Please enter a task.')

    def show_tasks(self):
        self.listbox.delete(0, END)
        for task in self.tasks:
            self.listbox.insert(END, task)

    def mark_complete(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks[task_index] = f"{self.tasks[task_index]} (Complete)"
            self.show_tasks()

    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.tasks[task_index]
            self.show_tasks()


if _name_ == "_main_":
    root = Tk()
    app = TodoList(root)
    root.mainloop()




