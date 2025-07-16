import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()
    if not str(length).isdigit() or int(length) < 4:
        messagebox.showerror("❌ Invalid Input", "Please enter a valid number (min: 4)")
        return

    length = int(length)
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_chars, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy to clipboard using Tkinter
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Keeps the clipboard content after the app is closed
        messagebox.showinfo("✅ Copied", "Password copied to clipboard! 📋")

# GUI setup
root = tk.Tk()
root.title("Password Generator 🔐")
root.geometry("450x350")
root.config(bg="#ffe6e6")

# Heading
tk.Label(root, text="🔐 Password Generator made by Rohit", font=("Helvetica", 20, "bold"),
         fg="#4B0082", bg="#ffe6e6").pack(pady=20)

# Input Frame
frame = tk.Frame(root, bg="#ffe6e6")
frame.pack(pady=10)

tk.Label(frame, text="🔢 Length:", font=("Arial", 14, "bold"),
         fg="#007acc", bg="#ffe6e6").pack(side=tk.LEFT)

length_var = tk.StringVar()
tk.Entry(frame, textvariable=length_var, font=("Arial", 14), width=5,
         bg="#fff8dc", fg="#000").pack(side=tk.LEFT, padx=10)

# Password Entry
password_entry = tk.Entry(root, font=("Arial", 16), justify='center',
                          bg="#e0ffff", fg="#000080", width=30)
password_entry.pack(pady=20)

# Button Frame
btn_frame = tk.Frame(root, bg="#ffe6e6")
btn_frame.pack()

generate_btn = tk.Button(btn_frame, text="🎲 Generate", command=generate_password,
                         font=("Arial", 14, "bold"), bg="#90ee90", fg="#006400", width=12)
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="📋 Copy", command=copy_to_clipboard,
                     font=("Arial", 14, "bold"), bg="#add8e6", fg="#00008b", width=12)
copy_btn.grid(row=0, column=1, padx=10)

# Footer
tk.Label(root, text="✨ Safe & Secure ✨", font=("Arial", 10, "italic"),
         bg="#ffe6e6", fg="#8b0000").pack(pady=10)

root.mainloop()
