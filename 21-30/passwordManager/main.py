from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

class PasswordManager:
    def __init__(self, master):
        self.master = master
        master.title("Password Manager")
        master.config(padx=50, pady=50)

        self.canvas = Canvas(height=200, width=200)
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)

        # Labels
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=2, column=0)
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, "grinningtickingclocker@gmail.com")
        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        self.generate_password_button = Button(text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=3, column=2)
        self.add_button = Button(text="Add", width=36, command=self.save)
        self.add_button.grid(row=4, column=1, columnspan=2)

        # Search Button
        self.search_button = Button(text="Search", width=16, command=self.find_password)
        self.search_button.grid(row=1, column=3)

    def generate_password(self):
        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        password_length = random.randint(8, 12)
        password_characters = letters + numbers + symbols

        generated_password = ''.join(random.choice(password_characters) for i in range(password_length))

        self.password_entry.delete(0, END)
        self.password_entry.insert(0, generated_password)
        pyperclip.copy(generated_password)

    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                           f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    self.website_entry.delete(0, END)
                    self.email_entry.delete(0, END)
                    self.password_entry.delete(0, END)

    def find_password(self):
        website = self.website_entry.get()
        try:
            with open("data.txt", "r") as data_file:
                lines = data_file.readlines()
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            for line in lines:
                if website in line:
                    data = line.strip().split(" | ")
                    email = data[1]
                    password = data[2]
                    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                    return  # Stop searching after finding the first match
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

if __name__ == "__main__":
    root = Tk()
    app = PasswordManager(root)
    root.mainloop()
