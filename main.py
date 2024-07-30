import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(char, k=length))
    return password

def generate_button_click():
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length should be greater than 0.")
        else:    
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password,font=("Helvetica", 8, "bold"),fg="red")
            
            
app = tk.Tk()
app.title("Password Generator")
app.geometry("500x500")


user_label = tk.Label(app, text="Enter username",font=("Helvetica", 8, "bold"))
user_label.pack()

user_entry = tk.Entry(app)
user_entry.pack()


length_label = tk.Label(app, text="Enter password length",font=("Helvetica", 8, "bold"))
length_label.pack()

length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_button_click,font=("Helvetica", 8, "bold"),bg="green",fg="white")
generate_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Start the Tkinter main loop
app.mainloop()