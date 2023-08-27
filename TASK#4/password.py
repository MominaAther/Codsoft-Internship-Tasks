from tkinter import *
import random

def generate_password():
    length = scvalue.get()
    if length.isdigit():
        length = int(length)
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/|_-"
        password = ''.join(random.choice(characters) for _ in range(length))
        scvalue.set(password)  
    else:
        scvalue.set("Invalid Length")  

def clear_entry():
    scvalue.set("") 

root = Tk()
root.title("Password Generator")
p1 = PhotoImage(file='password.png')
root.iconphoto(False, p1)
root.geometry("500x400")
root.maxsize(500,400)
root.minsize(500,400)
root.config(bg="black")

scvalue = StringVar()
scvalue.set("")

display_label = Label(
    text="Enter the length of required password",
    padx=10, pady=5, bg='black', fg='white', font=("Comic Sans MS", 19, "bold")
)
display_label.pack(anchor="w", padx=10, pady=20)

task_entry = Entry(root, textvar=scvalue, font=("Comic Sans MS", 15))
task_entry.pack(fill=X, padx=20, pady=20)

generate_button = Button(
    root, text="Generate", padx=5, pady=5,
    font= "ComicSansMS 19 normal", bg="green", highlightbackground="grey",
    command=generate_password
)
generate_button.pack(pady=20,padx=15,fill='x')

clear_button = Button(
    root, text="Clear", padx=5, pady=5,
    font="ComicSansMS 19 normal", bg="red", highlightbackground="grey",
    command=clear_entry
)
clear_button.pack(pady=20,padx=15,fill='x')

root.mainloop()


























































































# from tkinter import *
# from tkinter import PhotoImage, messagebox
# import random


# #list=["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","/",'|',"_","-"]
# def click(event):
    
#     global scvalue
#     text = event.widget.cget("text")
#     print(text)
#     l1=["1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","/",'|',"_","-"]
#     l2 = []
#     if text == "Generate":
#         if scvalue.get().isdigit():
#             value = int(scvalue.get())
#             # for i in range(value):
#                  #     print(i)
#             for i in range(value):
#                 L2.append(l1.random())

#         else:
#             try:
#                 value = eval(screen.get())
#             except Exception as e:
#                 scvalue.set("Error")
#                 screen.update()

#         scvalue.set(value)
#         screen.update()

#     elif text == "C":
#         scvalue.set("")
#         screen.update()
#     else:
#         scvalue.set(scvalue.get() + text)
#         screen.update()


    

# root = Tk()
# root.title("Password Generator")
# # p1 = PhotoImage(file='to-do-list.png')
# # root.iconphoto(False, p1)
# root.minsize(500,600)
# root.maxsize(500,600)
# root.config(bg="black")
# scvalue = StringVar()
# scvalue.set("")

# display_label = Label(text="Enter the length of required password", padx=10, pady=5, bg='black', fg='white', font = ("Comic Sans MS", 19, "bold"))
# display_label.pack(anchor="w", padx=10, pady=20)

# task_entry = Entry(root, textvar = scvalue, font = ("Comic Sans MS", 15))
# task_entry.pack(fill=X, padx=20, pady=20)

# b = Button(root, text="Generate", padx=10, pady=10, font="lucida 25 normal", bg = "red", highlightbackground="grey", highlightthickness=2)
# b.bind("<Button-1>", click)
# b.pack()
 
# root.mainloop()

# # value = 7
# # for i in range(value):
# #     print(i)
