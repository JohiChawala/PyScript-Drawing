import tkinter as tk
from tkinter import messagebox
from backend import tokenize, execute_commands
from tabulate import tabulate

# Create the Tkinter window
window = tk.Tk()
window.title("PyScript Drawing")

# Create a canvas for drawing
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

# Input box for user commands
command_entry = tk.Entry(window, width=50)
command_entry.pack()

# Output box for displaying token table and symbol table
output_box = tk.Text(window, height=20, width=50, state="normal")
output_box.pack()

# Function to execute command on button press
def run_command(event=None):  # Allow event parameter for keyboard binding
    command = command_entry.get()
    try:
        tokens, token_table = tokenize(command)  # Get tokens and token table
        output_box.delete(1.0, tk.END)  # Clear the output box
        output_box.insert(tk.END, "Token Table:\n")
        output_box.insert(tk.END, token_table + "\n\n")  # Display token table
        
        symbol_table = execute_commands(tokens, canvas)  # Execute commands and get symbol table
        
        # Display the symbol table
        symbol_log = [
            ["Position_X", symbol_table["Position_X"]],
            ["Position_Y", symbol_table["Position_Y"]],
            ["Color", symbol_table["Color"]]
        ]
        headers = ["Variable", "Value"]
        symbol_table_str = tabulate(symbol_log, headers, tablefmt="grid")
        output_box.insert(tk.END, "Symbol Table:\n")
        output_box.insert(tk.END, symbol_table_str + "\n")
        
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Bind the Enter key to the run_command function
command_entry.bind("<Return>", run_command)

# Button to run the command
run_button = tk.Button(window, text="Run", command=run_command)
run_button.pack()

# Main loop to run the application
window.mainloop()
# move(100, 200); set_color(red); draw_circle(30);
# move(200, 190); set_color(red); draw_circle(30);