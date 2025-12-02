import tkinter as tk
import math

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace("^", "**")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def scientific_function(func):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        
        if func == "sin":
            entry.insert(0, str(math.sin(math.radians(value))))
        elif func == "cos":
            entry.insert(0, str(math.cos(math.radians(value))))
        elif func == "tan":
            entry.insert(0, str(math.tan(math.radians(value))))
        elif func == "sqrt":
            entry.insert(0, str(math.sqrt(value)))
        elif func == "log":
            entry.insert(0, str(math.log10(value)))
        elif func == "pi":
            entry.insert(0, str(math.pi))
    except:
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("360x550")

entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=5, relief="ridge")
entry.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '^', '+'
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(frame, text=button, width=5, height=2, font=('Arial', 18),
                    command=lambda b=button: button_click(b))
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Scientific buttons
sci_frame = tk.Frame(root)
sci_frame.pack()

sci_buttons = [
    ("sin", "sin"), ("cos", "cos"), ("tan", "tan"),
    ("√", "sqrt"), ("log", "log"), ("π", "pi")
]

for i, (label, func) in enumerate(sci_buttons):
    btn = tk.Button(sci_frame, text=label, width=5, height=2, font=('Arial', 18),
                    command=lambda f=func: scientific_function(f))
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)

# Equal & Clear
equal_btn = tk.Button(root, text="=", width=20, height=2, font=('Arial', 20), command=calculate)
equal_btn.pack(pady=10)

clear_btn = tk.Button(root, text="Clear", width=20, height=2, font=('Arial', 18), command=clear)
clear_btn.pack(pady=5)

root.mainloop()
