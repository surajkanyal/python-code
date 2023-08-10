import tkinter as tk

# Conversion functions
def cm_to_inches(cm):
    return cm * 0.393701

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_meters(cm):
    return cm / 100

def meters_to_cm(meters):
    return meters * 100

# GUI
def convert_length():
    input_value = float(entry_input.get())
    selected_unit = dropdown_from_var.get()
    target_unit = dropdown_to_var.get()

    if selected_unit == "Centimeters" and target_unit == "Inches":
        result = cm_to_inches(input_value)
    elif selected_unit == "Inches" and target_unit == "Centimeters":
        result = inches_to_cm(input_value)
    elif selected_unit == "Centimeters" and target_unit == "Meters":
        result = cm_to_meters(input_value)
    elif selected_unit == "Meters" and target_unit == "Centimeters":
        result = meters_to_cm(input_value)
    else:
        result = input_value

    label_result.config(text=f"Result: {result:.2f} {target_unit}")

root = tk.Tk()
root.title("Length Conversion")

# Input widgets
label_input = tk.Label(root, text="Enter length:")
label_input.pack(pady=5)

entry_input = tk.Entry(root)
entry_input.pack(pady=5)

# Dropdown menus for unit selection
units = ["Centimeters", "Inches", "Meters"]

dropdown_from_var = tk.StringVar()
dropdown_from_var.set(units[0])
dropdown_from = tk.OptionMenu(root, dropdown_from_var, *units)
dropdown_from.pack(pady=5)

dropdown_to_var = tk.StringVar()
dropdown_to_var.set(units[1])
dropdown_to = tk.OptionMenu(root, dropdown_to_var, *units)
dropdown_to.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_length)
button_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
