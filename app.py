import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

# Dictionary to store keyboard shortcuts and their associated functions
shortcuts = {}

# Function that gets called when a registered shortcut is pressed
def execute_function(func_name):
    messagebox.showinfo("Function Executed", f"Executing function: {func_name}")

# Listener callback for detecting key presses
def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
        
    # Check if the pressed key matches any of the registered shortcuts
    for shortcut, func_name in shortcuts.items():
        if key_name in shortcut:
            execute_function(func_name)

# Function to add a new shortcut
def add_shortcut():
    func_name = function_entry.get()
    shortcut = shortcut_entry.get()
    
    if func_name and shortcut:
        shortcuts[shortcut] = func_name
        update_shortcut_list()
        messagebox.showinfo("Shortcut Added", f"Shortcut '{shortcut}' for '{func_name}' added!")
    else:
        messagebox.showwarning("Input Error", "Both function name and shortcut are required.")

# Function to update the list of shortcuts displayed in the GUI
def update_shortcut_list():
    shortcut_list.delete(0, tk.END)
    for shortcut, func_name in shortcuts.items():
        shortcut_list.insert(tk.END, f"{shortcut} -> {func_name}")

# Create the main GUI window
root = tk.Tk()
root.title("Keyboard Shortcut Manager")

# GUI Layout
tk.Label(root, text="Function Name:").grid(row=0, column=0, padx=10, pady=10)
function_entry = tk.Entry(root)
function_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Keyboard Shortcut:").grid(row=1, column=0, padx=10, pady=10)
shortcut_entry = tk.Entry(root)
shortcut_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add Shortcut", command=add_shortcut)
add_button.grid(row=2, column=1, padx=10, pady=10)

# Listbox to display the shortcuts
shortcut_list = tk.Listbox(root, height=10, width=40)
shortcut_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the listener for keyboard events
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Run the GUI application
root.mainloop()