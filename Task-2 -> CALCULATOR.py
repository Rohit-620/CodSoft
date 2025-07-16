import tkinter as tk
from tkinter import messagebox

# Function 
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Input Error", "Invalid operation.")
            return

        result_label.config(text=f"✅ Result: {result}", fg="green")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x420")
root.config(bg="#f0f4c3")

# Title
title = tk.Label(root, text="🌟 Calculator 🌟", font=("Helvetica", 20, "bold"), bg="#f0f4c3", fg="#4e342e")
title.pack(pady=20)

# First Number
tk.Label(root, text="Enter First Number:", bg="#f0f4c3", font=("Arial", 12)).pack()
entry1 = tk.Entry(root, font=("Arial", 14), bg="#ffe0b2", fg="#bf360c", width=22, justify='center')
entry1.pack(pady=8)

# Second Number
tk.Label(root, text="Enter Second Number:", bg="#f0f4c3", font=("Arial", 12)).pack()
entry2 = tk.Entry(root, font=("Arial", 14), bg="#b2ebf2", fg="#006064", width=22, justify='center')
entry2.pack(pady=8)

# Operation Selection 
tk.Label(root, text="Choose Operation:", bg="#f0f4c3", font=("Arial", 12)).pack(pady=5)
operation = tk.StringVar(value='+')
operation_frame = tk.Frame(root, bg="#f0f4c3")
operation_frame.pack()

tk.Radiobutton(operation_frame, text="+", variable=operation, value='+', font=("Arial", 12),
               bg="#a5d6a7", fg="#1b5e20", selectcolor="#c8e6c9", width=5).pack(side='left', padx=5)

tk.Radiobutton(operation_frame, text="-", variable=operation, value='-', font=("Arial", 12),
               bg="#90caf9", fg="#0d47a1", selectcolor="#bbdefb", width=5).pack(side='left', padx=5)

tk.Radiobutton(operation_frame, text="×", variable=operation, value='*', font=("Arial", 12),
               bg="#f48fb1", fg="#880e4f", selectcolor="#fce4ec", width=5).pack(side='left', padx=5)

tk.Radiobutton(operation_frame, text="÷", variable=operation, value='/', font=("Arial", 12),
               bg="#ffe082", fg="#e65100", selectcolor="#fff3e0", width=5).pack(side='left', padx=5)

# Calculate Button
tk.Button(root, text="Calculate", font=("Arial", 14, "bold"), bg="#8d6e63", fg="white", width=15, command=calculate).pack(pady=20)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#f0f4c3", fg="black")
result_label.pack(pady=10)

# Run
root.mainloop()
