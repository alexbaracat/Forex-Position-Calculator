import tkinter as tk
from tkinter import ttk

def position():
    size = int(10)
    return

def update_pair2(*args):
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

# List of interval values
intervals = ["USD", "CAD", "JPY", "NZD", "AUD"]

# PANEL 0 -----------------------------------------------
panel0 = tk.Frame(window)
panel0.grid(row=0, column=0, rowspan=2, sticky="nsew")

# PANEL 0 - Combobox for Pair I
pair1_label = tk.Label(panel0, text="Pair I:")
pair1_label.grid(row=0, column=0, sticky="w")
pair1_combobox = ttk.Combobox(panel0, values=intervals)
pair1_combobox.current(0)
pair1_combobox.grid(row=1, column=0, sticky="ew")

# Position size and label
ticker_label = tk.Label(panel0, text="Position size:")
ticker_label.grid(row=2, column=0, sticky="w")
ticker_entry = tk.Entry(panel0)
ticker_entry.grid(row=3, column=0, sticky="ew")

# PANEL 1 -----------------------------------------------
panel1 = tk.Frame(window)
panel1.grid(row=0, column=2, rowspan=2, sticky="nsew")

# PANEL 1 - Combobox for Pair II
pair2_label = tk.Label(panel1, text="Pair II:")
pair2_label.grid(row=0, column=0, sticky="w")
pair2_combobox = ttk.Combobox(panel1, values=intervals)
pair2_combobox.current(0)
pair2_combobox.grid(row=1, column=0, sticky="ew")

# Bind the Pair I combobox to the update_pair2 function
pair1_combobox.bind("<<ComboboxSelected>>", update_pair2)

# NEW PANEL UNDER PANEL 0 AND PANEL 1 ----------------
panel01 = tk.Frame(window)
panel01.grid(row=2, column=0, columnspan=3, sticky="nsew")

# Label for position size
position_size_label = tk.Label(panel01, text="Position Size:")
position_size_label.grid(row=0, column=0, sticky="w")

# Entry widget for position size
position_size_entry = tk.Entry(panel01)
position_size_entry.grid(row=0, column=1, sticky="ew")

# PANEL 0 - Combobox for Calculate
display_button = tk.Button(panel01, text="Calculate", command=position())
display_button.grid(row=0, column=2, sticky="e", padx=5)

#--------------------------------------------------------
# Start the Tkinter main loop
window.mainloop()
#--------------------------------------------------------
