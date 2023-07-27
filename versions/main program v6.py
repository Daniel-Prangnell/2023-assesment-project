#---------------------this version is a continuation from Basic GUI V5


from tkinter import *
from functools import partial  # To prevent unwanted windows

# Default values for variables, such as the area if it hasnt be calculated or setting the default mode to degrees 
mode = "Degrees"
area = "uncalculated"
error = ""


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
                                  command=lambda: change_mode("Degrees", self)) # start the function that changes the mode (degrees / radians)
    self.to_degrees_mode.grid(row=0, column=0, pady=5, padx=5)

    # display what mode it is in
    self.show_mode = Label(self.mode_button_frame,
                           text="Mode: {}".format(mode),
                           width=12)
    self.show_mode.grid(row=0, column=1, pady=5, padx=5)

    # change type of calculation mode to radian
    self.to_radian_mode = Button(self.mode_button_frame,
                                 text="Radians",
                                 bg="#296EB4",
                                 fg=button_fg,
                                 font=button_font,
                                 width=10,
                                 command=lambda: change_mode("Radians", self)) # start the function that changes the mode (degrees / radians)
    self.to_radian_mode.grid(row=0, column=2, pady=5, padx=5)

    # Set up GUI Frame for value inputs
    self.input_value_frame = Frame(self.heading_instruction_frame)
    self.input_value_frame.grid(row=3)

    # text to show which side they should enter the side values into
    self.side_length_text = Label(
      self.input_value_frame,
      text="Input the values for the side lengths in the boxes below",
      width=24,
      wraplength=200,
      justify="center")
    self.side_length_text.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

    # text to show which side they should enter the angle values into
    self.angle_size_text = Label(
      self.input_value_frame,
      text="Input the values for the side lengths in the boxes below",
      width=24,
      wraplength=200,
      justify="center")
    self.angle_size_text.grid(row=1, column=3, columnspan=2, pady=5, padx=5)

    #side length input text
    # side: hypotenuse text
    self.hypotenuse_length_text = Label(self.input_value_frame,
                                        text="Hypotenuse: ",
                                        width=10,
                                        wraplength=150,
                                        justify="center")
    self.hypotenuse_length_text.grid(row=2, column=0)

    # side: adjacent text
    self.adjacent_length_text = Label(self.input_value_frame,
                                      text="Adjacent: ",
                                      width=10,
                                      wraplength=150,
                                      justify="center")
    self.adjacent_length_text.grid(row=3, column=0)

    # side: opposite text
    self.opposite_length_text = Label(self.input_value_frame,
                                      text="Opposite: ",
                                      width=10,
                                      wraplength=150,
                                      justify="center")
    self.opposite_length_text.grid(row=4, column=0)

    # Length value inputs boxes
    # hypotenuse length value input box
    self.hypotenuse_length_entry = Entry(self.input_value_frame,
                                         font=("Arial", "14"),
                                         width=12)
    self.hypotenuse_length_entry.grid(row=2, column=1, padx=10, pady=3)

    # adjacent length value input box
    self.adjacent_length_entry = Entry(self.input_value_frame,
                                       font=("Arial", "14"),
                                       width=12)
    self.adjacent_length_entry.grid(row=3, column=1, padx=10, pady=3)

    # opposite length value input box
    self.opposite_length_entry = Entry(self.input_value_frame,
                                       font=("Arial", "14"),
                                       width=12)
    self.opposite_length_entry.grid(row=4, column=1, padx=10, pady=3)

    # side length input text
    # angle: adjacent text
    self.adjacent_angle_text = Label(self.input_value_frame,
                                     text="Adjacent: ",
                                     width=10,
                                     wraplength=150,
                                     justify="center")
    self.adjacent_angle_text.grid(row=2, column=3)

    # angle: opposite text
    self.opposite_angle_text = Label(self.input_value_frame,
                                     text="Opposite: ",
                                     width=10,
                                     wraplength=150,
                                     justify="center")
    self.opposite_angle_text.grid(row=3, column=3)

    # Angle value input boxes
    # adjacent angle value input box
    self.adjacent_angle_entry = Entry(self.input_value_frame,
                                      font=("Arial", "14"),
                                      width=12)
    self.adjacent_angle_entry.grid(row=2, column=4, padx=10, pady=3)

    # opposite angle value input box
    self.opposite_angle_entry = Entry(self.input_value_frame,
                                      font=("Arial", "14"),
                                      width=12)
    self.opposite_angle_entry.grid(row=3, column=4, padx=10, pady=3)


    #calculation button - this is used to activate the calculation function
    self.calculate_button = Button(self.input_value_frame,
                                   text="Calculate",
                                   bg="#009900",
                                   fg=button_fg,
                                   font=button_font,
                                   width=20)
    self.calculate_button.grid(row=4, column=3, columnspan=2, pady=3, padx=10)

    # Set up GUI Frame for help button, area display, and error message
    self.misc_labels_help_button = Frame(self.heading_instruction_frame)
    self.misc_labels_help_button.grid(row=4)

    # display the value of the area, if a area has calculated show the value, if not show uncalculated
    self.display_area = Label(self.misc_labels_help_button,
                              text="Area: {}".format(area),
                              width=20,
                              wraplength=150,
                              justify="center")
    self.display_area.grid(row=0, column=1)

    # error message
    self.error_message = Label(self.misc_labels_help_button,
                               text="{}".format(error),
                               width=20,
                               wraplength=150,
                               justify="center")
    self.error_message.grid(row=1, column=1)

    #help button
    self.help_button = Button(self.misc_labels_help_button,
                              text="Help / Info",
                              bg="#CC6600",
                              fg=button_fg,
                              font=button_font,
                              width=20,
                              command=self.help_menu)
    self.help_button.grid(row=2, column=1, pady=3, padx=10)

  # Opens Helps menu
  def help_menu(self):
    DisplayHelp(self)


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
  print(
    value
  )  #---------------------------------------------temperary--------------------------

#help case, this is to show the help / info menu
class DisplayHelp:

  def __init__(self, partner):
    #background of help menu
    background = "#ffe6cc"
    #to display the help menu ontop of the main program
    self.help_box = Toplevel()

    #to disable help button so they cant pen up multiple help menus
    partner.help_button.config(state=DISABLED)

    # setup to be able to close the help menu
    self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                       partner))


    # help menu size
    self.help_frame = Frame(self.help_box,
                            width=300,
                            height=200,
                            bg=background)

    self.help_frame.grid()

    # help menu heading
    self.help_heading_label = Label(self.help_frame,
                                    bg=background,
                                    text="Help / Info",
                                    font=("Arial", "14", "bold"))
    self.help_heading_label.grid(row=0)

    # help / info text
    help_text = "insert help info here"

    # display the help text
    self.help_text_label = Label(self.help_frame,
                                 bg=background,
                                 text=help_text,
                                 wrap=350,
                                 justify="left")
    self.help_text_label.grid(row=1, padx=10)

    # button to close the help menu
    self.dismiss_button = Button(self.help_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 bg="#CC6600",
                                 fg="#FFFFFF",
                                 command=partial(self.close_help, partner))
    self.dismiss_button.grid(row="2")

  # close the help menu
  def close_help(self, partner):
    partner.help_button.config(state=NORMAL)
    self.help_box.destroy()


# Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()
