from tkinter import *

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(END, "\u2718 " + task)
        task_entry.delete(0, END)

def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)

def mark_complete():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        selected_task = task_list.get(selected_task_index)
        if selected_task.startswith("\u2718 "):
            updated_task = "\u2714 " + selected_task[2:]
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, updated_task)

root = Tk()
root.title("TO-DO List")
p1 = PhotoImage(file='to-do-list.png')
root.iconphoto(False, p1)
root.geometry("500x600")
root.minsize(400,600)
root.maxsize(400,600)
root.config(bg="black")
root.option_add("*Button*foreground", "white")

task_list = Listbox(root, font = ("Comic Sans MS", 20), bg="black")
task_list.pack(fill=BOTH, expand=True, padx=20, pady=5)
task_list.config(fg="white")

task_entry = Entry(root, font = ("Comic Sans MS", 15))
task_entry.pack(fill=X, padx=20, pady=5)

add_button = Button(root, text="Add Task", command=add_task, font = ("Comic Sans MS", 12, "bold"), bg="black")
add_button.pack(fill=X, padx=20, pady=5)

mark_button = Button(root, text="Mark Complete", command=mark_complete, font = ("Comic Sans MS", 12, "bold"), bg="black")
mark_button.pack(fill=X, padx=20, pady=5)

remove_button = Button(root, text="Remove Task", command=remove_task, font = ("Comic Sans MS", 12, "bold"), bg="black")
remove_button.pack(fill=X, padx=20, pady=5)

save_button = Button(root, text="Save")

root.mainloop()
