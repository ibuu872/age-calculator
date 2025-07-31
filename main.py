import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        birth_date = date(year, month, day)
        today = date.today()
        
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Create and place the widgets
tk.Label(root, text="Enter Day:").pack(pady=2)
entry_day = tk.Entry(root)
entry_day.pack()

tk.Label(root, text="Enter Month:").pack(pady=2)
entry_month = tk.Entry(root)
entry_month.pack()

tk.Label(root, text="Enter Year:").pack(pady=2)
entry_year = tk.Entry(root)
entry_year.pack()

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

result_label = tk.Label(root, text="Your Age: ")
result_label.pack(pady=10)

# Start the main loop
root.mainloop()