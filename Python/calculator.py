import tkinter as tk
import math
import re

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        expression = re.sub(r'(\w+)(\d+)', r'\1(\2)', expression) # log3, sin45 -> log(3), sin(45)
        result = eval(expression, {"__builtins__": None}, {
            "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, 
            "log": math.log, "exp": math.exp, "pi": math.pi, 
            "log10": math.log10, "radians": math.radians, "degrees": math.degrees})

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator in python by Toxiic536")
window.geometry("500x700")
window.config(bg="#f0f0f0")

button_style = {
    'font': ('Arial', 18),
    'width': 5,
    'height': 2,
    'bg': '#2e2e2e',
    'fg': 'white',
    'activebackground': '#555555'
}

entry = tk.Entry(window, font=('Arial', 24), bd=10, relief="sunken", justify="right", bg="#e0e0e0")
entry.grid(row=0, column=0, columnspan=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('^', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('sqrt', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('cos', 4, 4),
    ('C', 5, 0), ('tan', 5, 1), ('log', 5, 2), ('exp', 5, 3), ('pi', 5, 4)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, command=calculate, **button_style)
    elif text == "C":
        button = tk.Button(window, text=text, command=clear, **button_style)
    else:
        button = tk.Button(window, text=text, command=lambda value=text: click_button(value), **button_style)
    button.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
