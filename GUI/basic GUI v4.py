from tkinter import *
from functools import partial  # To prevent unwanted windows

mode = "Degrees"
area = "uncalculated"

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
    # Display the simple instructions
    self.basic_instructions = Label(self.heading_instruction_frame,
                                   text=instuctions,
                                   wrap=250,
                                   width=40,
                                   justify="center")
    self.basic_instructions.grid(row=1)



    
    # Set up GUI Frame for calculating type button (degrees / radians)
    self.mode_button_frame = Frame(self.heading_instruction_frame)
    self.mode_button_frame.grid(row=2)

    # change type of calculation mode to degrees
    self.to_degrees_mode = Button(self.mode_button_frame,
                                    text="Degrees",
                                    bg="#990099",
                                    fg=button_fg,
                                    font=button_font,
                                    width=10,
                                    state=DISABLED,
                                    command=lambda: change_mode("Degrees", self))
    self.to_degrees_mode.grid(row=0, column=0,pady=5, padx=5)

    # display what mode it is in
    self.show_mode = Label(self.mode_button_frame,
                                    text="Mode: {}".format(mode),
                                    width=12)
    self.show_mode.grid(row=0, column=1,pady=5, padx=5)

    # change type of calculation mode to radian
    self.to_radian_mode = Button(self.mode_button_frame,
                                    text="Radians",
                                    bg="#296EB4",
                                    fg=button_fg,
                                    font=button_font,
                                    width=10,
                                    command=lambda: change_mode("Radians", self))
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
    self.angle_size_text.grid(row=1, column=1,pady=5, padx=5)

    # Length value inputs boxes
    # hypotenuse length value input box
    self.hypotenuse_length_entry = Entry(self.input_value_frame, font=("Arial", "14"), )
    self.hypotenuse_length_entry.grid(row=2, padx=10, pady=3)

    # adjacent length value input box
    self.adjacent_length_entry = Entry(self.input_value_frame, font=("Arial", "14"), )
    self.adjacent_length_entry.grid(row=3, padx=10, pady=3)

    # opposite length value input box
    self.opposite_length_entry = Entry(self.input_value_frame, font=("Arial", "14"), )
    self.opposite_length_entry.grid(row=4, padx=10, pady=3)

    # Angle value input boxes
    # adjacent angle value input box
    self.adjacent_angle_entry = Entry(self.input_value_frame, font=("Arial", "14"), )
    self.adjacent_angle_entry.grid(row=2, column=1, padx=10, pady=3)

    # opposite angle value input box
    self.opposite_angle_entry = Entry(self.input_value_frame, font=("Arial", "14"), )
    self.opposite_angle_entry.grid(row=3, column=1, padx=10, pady=3)


    self.calculate_button = Button(self.input_value_frame,
                                    text="Calculate",
                                    bg="#009900",
                                    fg=button_fg,
                                    font=button_font,
                                    width=20)
    self.calculate_button.grid(row=4, column=1,pady=3, padx=10)





def change_mode(value, self):
  # disable degrees buton if the mode is set to degrees
  if value == "Degrees":
    # set radians button to normal
    self.to_radian_mode.config(state=NORMAL)
    # set degrees button to disabled
    self.to_degrees_mode.config(state=DISABLED)

  # disable radians buton if the mode is set to radians
  if value == "Radians":
    # set degrees button to normal
    self.to_degrees_mode.config(state=NORMAL)
    # set radians button to disabled
    self.to_radian_mode.config(state=DISABLED)
  #change the show mode text
  self.show_mode.config(text="Mode: {}".format(value))
  print(value) #---------------------------------------------temperary--------------------------
# Main Routine
if __name__ == "__main__": 
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()