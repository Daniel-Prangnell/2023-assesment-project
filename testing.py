from tkinter import *
from functools import partial  # To prevent unwanted windows


class converter:

  def __init__(self):

    # commmon format for all buttons
    # Arail size 14 bold, with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"
    # Set up GUI Frame for title / simple intructions
    self.heading_instruction_frame = Frame(padx=10, pady=10)
    self.heading_instruction_frame.grid()
    # heading text
    self.heading = Label(self.heading_instruction_frame,
                              text="Right Angled Triangle Solver",
                              font=("Arial", "16", "bold"))
    self.heading.grid(row=0)
    # Simple intructions text
    instuctions = "Please select a mode, then input each of the values into the respective input square."
    self.basic_instructions = Label(self.heading_instruction_frame,
                                   text=instuctions,
                                   wrap=250,
                                   width=40,
                                   justify="center")
    self.basic_instructions.grid(row=1)



    
    # Set up GUI Frame for calculating type (degrees / radians)
    self.mode_button_frame = Frame(self.heading_instruction_frame)
    self.mode_button_frame.grid(row=2)

    self.to_degrees_mode = Button(self.mode_button_frame,
                                    text="Degrees",
                                    bg="#990099",
                                    fg=button_fg,
                                    font=button_font,
                                    width=10)
    self.to_degrees_mode.grid(row=0, column=0,pady=5, padx=5)

    self.show_mode = Label(self.mode_button_frame,
                                    text="Mode: <mode>",
                                    width=12,
                                    justify="left")
    self.show_mode.grid(row=0, column=1,pady=5, padx=5)

    self.to_radian_mode = Button(self.mode_button_frame,
                                    text="Radians",
                                    bg="#009900",
                                    fg=button_fg,
                                    font=button_font,
                                    width=10)
    self.to_radian_mode.grid(row=0, column=2,pady=5, padx=5)





    # Set up GUI Frame for value inputs
    self.input_value_frame = Frame(self.heading_instruction_frame)
    self.input_value_frame.grid(row=3)
    
    

    self.side_length_text = Label(self.input_value_frame,
                                    text="Input the values for the side lengths in the boxes below",
                                    width=24,
                                    wraplength=200,
                                    justify="center")
    self.side_length_text.grid(row=1, column=0,pady=5, padx=5)

    self.angle_size_text = Label(self.input_value_frame,
                                    text="Input the values for the side lengths in the boxes below",
                                    width=24,
                                    wraplength=200,
                                    justify="center")
    self.angle_size_text.grid(row=1, column=2,pady=5, padx=5)
  


    self.to_help = Button(self.input_value_frame,
                                    text="Help",
                                    bg="#004C99",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12)
    self.to_help.grid(row=3, column=0,pady=5, padx=5)


# Main Routine
if __name__ == "__main__": 
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()