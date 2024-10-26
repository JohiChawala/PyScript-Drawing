import re
from tabulate import tabulate

# Define token patterns for PyScript commands
token_patterns = [
    (r'move', 'MOVE'),
    (r'draw_circle', 'DRAW_CIRCLE'),
    (r'set_color', 'SET_COLOR'),
    (r'clear', 'CLEAR'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\d+', 'NUMBER'),  # Numbers
    (r',', 'COMMA'),
    (r'red|blue|green|black|yellow', 'COLOR'),  # Colors
    (r';', 'SEMICOLON'),
]

# Tokenizer function that skips spaces and outputs tokens in table format
def tokenize(command):
    tokens = []
    token_log = []  # List to store tokens and values for table format
    command = command.strip()  # Remove leading/trailing spaces
    while command:
        command = command.lstrip()  # Remove any leading spaces
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(command)
            if match:
                text = match.group(0)
                if token_type:
                    tokens.append((token_type, text))
                    token_log.append([token_type, text])  # Add token and text for table
                command = command[len(text):]
                break
        if not match:
            raise ValueError(f"Unexpected character: {command[0]}")
    
    # Return token log as a string in table format for the frontend
    headers = ["Token Type", "Token Value"]
    token_table = tabulate(token_log, headers, tablefmt="grid")
    
    return tokens, token_table

# Command execution logic
def execute_commands(tokens, canvas):
    pos_x, pos_y = 0, 0  # Default position
    color = "black"  # Default color
    symbol_table = {
        "Position_X": pos_x,
        "Position_Y": pos_y,
        "Color": color
    }  # Symbol table

    i = 0
    while i < len(tokens):
        token_type, token_value = tokens[i]

        if token_type == "MOVE":
            i += 2  # Skip LPAREN
            x = int(tokens[i][1])  # Number token for X-coordinate
            i += 2  # Skip COMMA
            y = int(tokens[i][1])  # Number token for Y-coordinate
            pos_x, pos_y = x, y  # Update the current position
            symbol_table["Position_X"] = pos_x  # Update symbol table
            symbol_table["Position_Y"] = pos_y  # Update symbol table
            i += 2  # Skip RPAREN and SEMICOLON
        elif token_type == "DRAW_CIRCLE":
            i += 2  # Skip LPAREN
            radius = int(tokens[i][1])  # Get the radius of the circle
            i += 2  # Skip RPAREN and SEMICOLON
            # Draw the circle using the current color and position
            canvas.create_oval(pos_x - radius, pos_y - radius, pos_x + radius, pos_y + radius, outline=color)
            print(f"Drew circle at ({pos_x}, {pos_y}) with radius {radius} and color {color}")
        elif token_type == "SET_COLOR":
            i += 2  # Skip LPAREN
            # Check if the next token is a valid color
            if tokens[i][0] == "COLOR":
                color = tokens[i][1]  # Update the current color
                symbol_table["Color"] = color  # Update symbol table
                i += 2  # Skip RPAREN and SEMICOLON
                print(f"Set color to {color}")
            else:
                raise ValueError("Invalid color specified")
        elif token_type == "CLEAR":
            canvas.delete("all")  # Clear the canvas
            pos_x, pos_y = 0, 0  # Reset position on clear
            color = "black"  # Reset color on clear
            symbol_table = {"Position_X": pos_x, "Position_Y": pos_y, "Color": color}  # Reset symbol table
            i += 2  # Skip RPAREN and SEMICOLON
            print("Cleared the canvas")
        else:
            i += 1  # Move to next token
    
    return symbol_table  # Return the symbol table
