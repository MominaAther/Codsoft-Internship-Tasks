import tkinter as tk
from tkinter import PhotoImage, messagebox



class ContactBookApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # Create frames for each label-entry pair
        self.name_frame = tk.Frame(root, padx=10, pady=10, bg='black')
        self.name_frame.pack(padx=10, pady=10, anchor='nw')
        self.name_label = tk.Label(self.name_frame, text="Name:", bg='black', fg='white', font = ("Comic Sans MS", 12, "bold"))
        self.name_label.pack(side='left', padx=10, pady=10)
        self.name_entry = tk.Entry(self.name_frame)
        self.name_entry.pack(side='left', padx=10, pady=10, fill="x")

        self.phone_frame = tk.Frame(root, padx=10, pady=10, bg = "black")
        self.phone_frame.pack(padx=10, pady=10, anchor='nw')
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number:", bg='black', fg='white', font = ("Comic Sans MS", 12, "bold"))
        self.phone_label.pack(side='left', padx=10, pady=10)
        self.phone_entry = tk.Entry(self.phone_frame)
        self.phone_entry.pack(side='left', padx=10, pady=10, fill="x")

        self.email_frame = tk.Frame(root, padx=10, pady=10, bg = "black")
        self.email_frame.pack(padx=10, pady=10, anchor='nw')
        self.email_label = tk.Label(self.email_frame, text="Email Address:", bg='black', fg='white', font = ("Comic Sans MS", 12, "bold"))
        self.email_label.pack(side='left', padx=10, pady=10)
        self.email_entry = tk.Entry(self.email_frame)
        self.email_entry.pack(side='left', padx=10, pady=10, fill="x")

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font = ("Comic Sans MS", 12, "bold"), bg="black")
        self.add_button.pack(padx=10, pady=5)

        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts, font = ("Comic Sans MS", 12, "bold"), bg="black")
        self.display_button.pack(padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font = ("Comic Sans MS", 12, "bold"), bg="black")
        self.delete_button.pack(padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contacts.append((name, phone, email))
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added!")
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def display_contacts(self):
        if self.contacts:
            display_text = "\n".join([f"{name}\n{phone}\n{email}\n" for name, phone, email in self.contacts])
            display_window = tk.Toplevel(self.root)
            display_window.title("Contacts")
            display_label = tk.Label(display_window, text=display_text, padx=10, pady=5, bg='black', fg='white', font = ("Comic Sans MS", 12, "bold"))
            display_label.pack(anchor="w")
        else:
            messagebox.showinfo("No Contacts", "No contacts to display.")

    def delete_contact(self):
        if self.contacts:
            del self.contacts[-1]  # Delete the last contact
            messagebox.showinfo("Success", "Contact deleted!")
        else:
            messagebox.showwarning("Error", "No contacts to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contact Book")
    p1 = PhotoImage(file='book.png')
    root.iconphoto(False, p1)
    root.option_add("*Button*foreground", "white")
    # root.geometry("500x600")
    root.maxsize(300,450)
    root.minsize(300,450)
    root.config(bg="black")
    app = ContactBookApp(root)
   
    root.mainloop()
