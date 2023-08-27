from tkinter import *

def click(event):
    
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                scvalue.set("Error")
                screen.update()

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.title("Calculator")
p1 = PhotoImage(file='calculator.png')
root.iconphoto(False, p1)
root.minsize(400,600)
root.maxsize(400,600)
root.config(bg="black")
scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar = scvalue, font = "lucida 35 normal", highlightbackground="grey", highlightthickness=2)
screen.pack(fill = X and Y, pady = 20, padx = 35)

# frame # 1

f = Frame(root, padx=10, pady=10, bg = "black")
f.pack()
b = Button(f, text="9", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="8", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="7", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=0, column=2, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="+", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=0, column=3, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)



# frame # 2

f = Frame(root, padx=10, pady=10, bg = "black")
f.pack()
b = Button(f, text="6", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="5", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=1, column=1, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="4", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=1, column=2, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="-", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=1, column=3, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)



# frame # 3

f = Frame(root, padx=10, pady=10, bg = "black")
f.pack()
b = Button(f, text="3", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=2, column=0, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="2", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=2, column=1, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="1", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=2, column=2, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="*", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=2, column=3, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)



# frame # 4

f = Frame(root, padx=10, pady=10, bg = "black")
f.pack()
b = Button(f, text="C", padx=10, pady=10, font="lucida 25 normal", bg = "orange", highlightbackground="grey", highlightthickness=2)
b.grid(row=3, column=0, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="0", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=3, column=1, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="=", padx=10, pady=10, font="lucida 25 normal", bg = "red", highlightbackground="grey", highlightthickness=2)
b.grid(row=3, column=2, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)
b = Button(f, text="/", padx=10, pady=10, font="lucida 25 normal", bg="grey", highlightthickness=2)
b.grid(row=3, column=3, padx=8, pady=8, sticky="nsew")
b.bind("<Button-1>", click)


root.mainloop()
