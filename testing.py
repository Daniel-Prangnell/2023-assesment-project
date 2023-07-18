from tkinter import *
from functools import partial  # To prevent unwanted windows


class converter:

  def __init__(self):

    # commmon format for all buttons
    # Arail size 14 bold, with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"

    # Set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    # heading text
    self.heading = Label(self.temp_frame,
                              text="Right Angled Triangle Solver",
                              font=("Arial", "16", "bold"))
    self.heading.grid(row=0)

    # Simple intructions text
    instuctions = "Please select a mode, then input each of the values into the respective input square."
    self.basic_instructions = Label(self.temp_frame,
                                   text=instuctions,
                                   wrap=250,
                                   width=40,
                                   justify="center")
    self.basic_instructions.grid(row=1)

    # Conversion, help and history / export buttons
    self.button_frame = Frame(self.temp_frame)
    self.button_frame.grid(row=4)

    self.to_degrees_mode = Button(self.button_frame,
                                    text="Degrees",
                                    bg="#990099",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12)
    self.to_degrees_mode.grid(row=0, column=0,pady=5, padx=5)

    self.show_mode = Label(self.button_frame,
                                    text="Mode: <mode>",
                                    width=24,
                                    justify="left")
    self.show_mode.grid(row=0, column=2,pady=5, padx=5)

    self.to_radian_mode = Button(self.button_frame,
                                    text="Radians",
                                    bg="#009900",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12)
    self.to_radian_mode.grid(row=1, column=0,pady=5, padx=5)

    self.to_help = Button(self.button_frame,
                                    text="Help",
                                    bg="#004C99",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12)
    self.to_help.grid(row=2, column=0,pady=5, padx=5)

  


# Main Routine
if __name__ == "__main__": 
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()