"""
The launcher of snake game.
VARIABLES:
    dw (int): display width.
    dh (int): display height.
    sw (int): snake width
"""

import tkinter as tk
import snake

dw = 100
dh = 100
sw = 10
def btn_play_click():
    """The handler of btn_play click.
        VARIABLES:
            dw (int): display width.
            dh (int): display height.
            sw (int): snake width

    """
    dw = int(display_width_entry.get())
    dh = int(display_height_entry.get())
    sw = int(snake_width_entry.get())
    start_game(dw, dh, sw)

def start_game(dw, dh, sw):
    """
    Start game.
    ARGUMENTS:
        dw (int)= display width.
        dh (int)= display weight.
        sw (int)= snake width.
    """
    snake.main(dw, dh, sw)

"""Seting start window."""
start_window = tk.Tk()

frame1 = tk.Frame(master = start_window,
                  bg = "black")

"""The label "Welcome to the "Snake" game!" """
welcome_lbl = tk.Label(master = frame1,
                       width = 27,
                       text = 'Welcome to the "Snake" game!',
                       bg = "black",
                       fg = "yellow")
welcome_lbl.pack()


"""Setting the input data."""
setting_frame= tk.Frame(master = start_window,
                        bg = "black")

"""The label "Display width" """
display_width_lbl = tk.Label(master = setting_frame,
                             width = 27,
                             text = "Display width",
                             bg = "black",
                             fg = "yellow")
display_width_lbl.pack()

"""The text box which sets the display width"""
display_width_entry= tk.Entry(master = setting_frame)
display_width_entry.insert(0, "200")
display_width_entry.pack()

"""The label "Display height" """
display_height_lbl = tk.Label(master = setting_frame,
                              text = "Display height",
                              bg = "black",
                              fg = "yellow")
display_height_lbl.pack()

"""The text box which sets the display height"""
display_height_entry= tk.Entry(master = setting_frame)
display_height_entry.insert(0, "200")
display_height_entry.pack()

"""The label "Snake width" """
snake_width_lbl = tk.Label(master = setting_frame,
                           text = "Snake width",
                           bg = "black",
                           fg = "yellow")
snake_width_lbl.pack()

"""The text box which sets snake width"""
snake_width_entry = tk.Entry(master = setting_frame)
snake_width_entry.insert(0, "20")
snake_width_entry.pack()


"""The button of start the game."""
play_btn = tk.Button(master = setting_frame,
                     text = "Play",
                     command = btn_play_click,
                     width = 24,
                     height = 3,
                     bg = "blue",
                     fg = "yellow")
play_btn.pack()

frame1.pack()
setting_frame.pack()
start_window.mainloop()
