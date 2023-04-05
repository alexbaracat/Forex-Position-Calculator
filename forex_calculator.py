import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # import messagebox for displaying warnings

# List of Pairs
intervals = ["USD", "CAD", "JPY", "NZD", "AUD"]

pair1_value = "USD"
pair2_value = "CAD"
pair2_values = list(intervals)
pair2_values.remove(pair1_value)

# Risk percentage values
risk_values = [f"{i}%" for i in range(1, 26)]

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def position():
    position_size_str = position_size_TXT.get()
    risk_str = risk_combobox.get().rstrip('%')

    if not is_number(position_size_str):
        messagebox.showwarning("Invalid input", "Please enter a valid numeric value for position size.")
        return

    position_size = float(position_size_str)
    risk = float(risk_str) / 100
    result = position_size * risk
    result_label_TXT.delete(0, tk.END)
    result_label_TXT.insert(0, str(result))

def curr_pair1(*args):
    pair1_values = list(intervals)
    pair1_values.remove(pair2_value)
    pair1_combobox['values'] = pair1_values
    pair1_combobox.current(0)

def curr_pair2(*args):
    # Get the selected value in Pair I combobox
    pair1_value = pair1_combobox.get()

    # Remove the selected value from the Pair II combobox values
    pair2_values = list(intervals)
    pair2_values.remove(pair1_value)
    pair2_combobox['values'] = pair2_values
    pair2_combobox.current(0)

print("hello world")
# ------------------------- GUI -------------------------

# Create a basic Tkinter window
window = tk.Tk()
window.title("Forex Size Calculator")

# Define grid layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)



# PANEL 0 -----------------------------------------------
panel0 = tk.Frame(window)
panel0.grid(row=0, column=0, rowspan=2, sticky="nsew")

# PANEL 0 - Combobox for Pair I
pair1_label = tk.Label(panel0, text="Pair I:")
pair1_label.grid(row=0, column=0, sticky="w")
pair1_combobox = ttk.Combobox(panel0, values=intervals)
pair1_combobox.current(0)
pair1_combobox.grid(row=1, column=0, sticky="ew")

# PANEL 1 -----------------------------------------------
panel1 = tk.Frame(window)
panel1.grid(row=0, column=2, rowspan=2, sticky="nsew")

# PANEL 1 - Combobox for Pair II
pair2_label = tk.Label(panel1, text="Pair II:")
pair2_label.grid(row=0, column=0, sticky="w")
pair2_combobox = ttk.Combobox(panel1, values=pair2_values)
pair2_combobox.current(0)
pair2_combobox.grid(row=1, column=0, sticky="ew")

# Bind the Pair I combobox to the curr_pair2 function
pair1_combobox.bind("<<ComboboxSelected>>", curr_pair2)

# NEW PANEL UNDER PANEL 0 AND PANEL 1 ----------------
panel01 = tk.Frame(window)
panel01.grid(row=2, column=0, columnspan=3, sticky="nsew")

# POSITION SIZE
position_size_label = tk.Label(panel01, text="Position Size:")
position_size_label.grid(row=0, column=0, sticky="w")
#
position_size_TXT = tk.Entry(panel01)
position_size_TXT.grid(row=0, column=1, sticky="ew")

# RISK
risk_label = tk.Label(panel01, text="Risk:")
risk_label.grid(row=1, column=0, sticky="w")
#
risk_combobox = ttk.Combobox(panel01, values=risk_values)
risk_combobox.current(0)
risk_combobox.grid(row=1, column=1, sticky="ew")

# CALCULATE BUTTON
display_button = tk.Button(panel01, text="Calculate", command=position)
display_button.grid(row=2, column=1, sticky="e", padx=5)

# RESULT
result_label = tk.Label(panel01, text="Result:")
result_label.grid(row=3, column=0, sticky="w")
#
result_label_TXT = tk.Entry(panel01)
result_label_TXT.grid(row=3, column=1, sticky="ew")

#--------------------------------------------------------
# Start the Tkinter main loop

window.mainloop()
#--------------------------------------------------------
