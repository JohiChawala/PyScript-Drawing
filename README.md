

# PyScript Language

## Overview

**PyScript** is a simple scripting language designed for basic drawing commands on a canvas. It allows users to control a "pen" to draw shapes, move to specific positions, set colors, and clear the canvas. This language is ideal for those looking to perform graphical operations through scripting.

## Language Features

- **Move Command**: Move the pen to a specified `(x, y)` position on the canvas.
- **Draw Circle Command**: Draw a circle at the current pen position with a given radius.
- **Set Color Command**: Change the color of subsequent drawing operations.
- **Clear Command**: Clear the entire drawing canvas.

## Language Description

### Commands

| Command        | Description                                      |
|----------------|--------------------------------------------------|
| `move(x, y);`          | Move the pen to coordinates `(x, y)`.           |
| `draw_circle(r);`      | Draw a circle with radius `r` at the pen's position. |
| `set_color(color);`    | Set the drawing color to `color` (e.g., red, blue, green). |
| `clear();`             | Clear the entire canvas.                        |

### Supported Colors

- **red**
- **blue**
- **green**
- **black**

## Grammar Rules

The following Context-Free Grammar (CFG) defines PyScript's syntax:

- **Program Structure**

    ```plaintext
    <program>        ::= <command_list>
    <command_list>   ::= <command> ";" <command_list> | <command> ";"
    <command>        ::= <move_command> | <draw_command> | <set_color_command> | <clear_command>
    ```

- **Commands**

    ```plaintext
    <move_command>       ::= "move" "(" <number> "," <number> ")"
    <draw_command>       ::= "draw_circle" "(" <number> ")"
    <set_color_command>  ::= "set_color" "(" <color> ")"
    <clear_command>      ::= "clear" "(" ")"
    ```

- **Values and Constants**

    ```plaintext
    <number>         ::= <digit> <number> | <digit>
    <digit>          ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
    <color>          ::= "red" | "blue" | "green" | "black"
    ```

## Explanation of Grammar Rules

- `<program>`: The start symbol representing a full script composed of a list of commands.
- `<command_list>`: Represents one or more commands, each followed by a semicolon (`;`).
- `<command>`: A single action, such as moving the pen, drawing a circle, setting a color, or clearing the canvas.
- `<move_command>`: Moves the pen to a specified `(x, y)` position.
- `<draw_command>`: Draws a circle with a specified radius.
- `<set_color_command>`: Sets the pen color for future drawing actions.
- `<clear_command>`: Clears the canvas.
- `<number>` and `<digit>`: Define numeric values for positions and sizes.
- `<color>`: Specifies the set of supported color names.

## How to Run

To run the PyScript program:

1. Run `frontend.py` using the following command:
   ```bash
   python frontend.py
   ```
2. Execute commands within the program to draw on the canvas.

--- 
