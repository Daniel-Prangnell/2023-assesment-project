from tkinter import *
from functools import partial  # To prevent unwanted windows
import math

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
                                  command=lambda: change_mode("Degrees", self))
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
                                 command=lambda: change_mode("Radians", self))
    self.to_radian_mode.grid(row=0, column=2, pady=5, padx=5)

    # Set up GUI Frame for value inputs
    self.input_value_frame = Frame(self.heading_instruction_frame)
    self.input_value_frame.grid(row=3)

    self.side_length_text = Label(
      self.input_value_frame,
      text="Input the values for the side lengths in the boxes below",
      width=24,
      wraplength=200,
      justify="center")
    self.side_length_text.grid(row=1, column=0, columnspan=2, pady=5, padx=5)

    self.angle_size_text = Label(
      self.input_value_frame,
      text="Input the values for the side lengths in the boxes below",
      width=24,
      wraplength=200,
      justify="center")
    self.angle_size_text.grid(row=1, column=3, columnspan=2, pady=5, padx=5)

    #side length input text
    self.hypotenuse_length_text = Label(self.input_value_frame,
                                        text="Hypotenuse: ",
                                        width=10,
                                        wraplength=150,
                                        justify="center")
    self.hypotenuse_length_text.grid(row=2, column=0)

    self.adjacent_length_text = Label(self.input_value_frame,
                                      text="Adjacent: ",
                                      width=10,
                                      wraplength=150,
                                      justify="center")
    self.adjacent_length_text.grid(row=3, column=0)

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

    #side length input text
    self.adjacent_angle_text = Label(self.input_value_frame,
                                     text="Adjacent: ",
                                     width=10,
                                     wraplength=150,
                                     justify="center")
    self.adjacent_angle_text.grid(row=2, column=3)

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

    self.calculate_button = Button(self.input_value_frame,
                                   text="Calculate",
                                   bg="#009900",
                                   fg=button_fg,
                                   font=button_font,
                                   width=20,
                                   command=lambda: self.get_values())
    self.calculate_button.grid(row=4, column=3, columnspan=2, pady=3, padx=10)

    self.misc_labels_help_button = Frame(self.heading_instruction_frame)
    self.misc_labels_help_button.grid(row=4)

    self.display_area = Label(self.misc_labels_help_button,
                              text="Area: {}".format(area),
                              width=20,
                              wraplength=150,
                              justify="center")
    self.display_area.grid(row=0, column=1)

    self.error_message = Label(self.misc_labels_help_button,
                               text="{}".format(error),
                               fg="#9C0000",
                               width=40,
                               wraplength=300,
                               justify="center")
    self.error_message.grid(row=1, column=1)

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

  #fuction to get the values from the input boxes
  def get_values(self):
    # value of the hypotenuse side
    side_hypotenuse = ""
    #value for the adjacent side
    side_adjacent = ""
    # value for the opposite side
    side_opposite = ""
    # value for the adjacent angle
    angle_adjacent = ""
    # value for the opposite angle
    angle_opposite = ""

    # value of the hypotenuse side
    side_hypotenuse = self.hypotenuse_length_entry.get()
    #value for the adjacent side
    side_adjacent = self.adjacent_length_entry.get()
    # value for the opposite side
    side_opposite = self.opposite_length_entry.get()
    # value for the adjacent angle
    angle_adjacent = self.adjacent_angle_entry.get()
    # value for the opposite angle
    angle_opposite = self.opposite_angle_entry.get()
    print("before change:{} {} {} {} {}".format(side_hypotenuse, side_adjacent,
                                                side_opposite, angle_adjacent,
                                                angle_opposite))
    # if there wasnt a value entered, set value to 0
    try:
      if side_hypotenuse == "":
        side_hypotenuse = float(0)
      else:
        side_hypotenuse = float(side_hypotenuse)
      if side_adjacent == "":
        side_adjacent = float(0)
      else:
        side_adjacent = float(side_adjacent)
      if side_opposite == "":
        side_opposite = float(0)
      else:
        side_opposite = float(side_opposite)
      if angle_adjacent == "":
        angle_adjacent = float(0)
      else:
        angle_adjacent = float(angle_adjacent)
      if angle_opposite == "":
        angle_opposite = float(0)
      else:
        angle_opposite = float(angle_opposite)
      print("After change:{} {} {} {} {}".format(side_hypotenuse,
                                                 side_adjacent, side_opposite,
                                                 angle_adjacent,
                                                 angle_opposite))
      check_input_values(self, side_hypotenuse, side_adjacent, side_opposite,
                         angle_adjacent, angle_opposite)
    except ValueError:
      error_text = "Error: Non-valid value entered, e.g XI, letters, symbols"
      self.error_message.config(text=error_text)


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


def check_input_values(self, side_hypotenuse, side_adjacent, side_opposite,
                       angle_adjacent, angle_opposite):
  error_text = ""
  # testing if all the values have been entered, if yes print error
  if side_hypotenuse != 0 and side_adjacent != 0 and side_opposite != 0 and angle_adjacent != 0 and angle_opposite != 0:
    error_text = "Error: All values entered"

  # testing if no values have been entered, if yes print error
  if side_hypotenuse == 0 and side_adjacent == 0 and side_opposite == 0 and angle_adjacent == 0 and angle_opposite == 0:
    error_text = "Error: No values entered"

  # testing to see if a side value is negative, if yes print error message
  if side_hypotenuse < 0 or side_adjacent < 0 or side_opposite < 0:
    error_text = "Error: Side value cannot be negative"
  # testing to see if a angle value is negative, if yes print error message
  if angle_adjacent < 0 or angle_opposite < 0:
    error_text = "Error: Angle value cannot be negative"

  # testing if the hypotenuse is the longest side, if yes print error message
  if (side_hypotenuse <= side_adjacent
      or side_hypotenuse <= side_opposite) and side_hypotenuse > 0:
    error_text = "Error: Hypotenuse side must be the longest side"

  #testing if the total value of the input angles is equal to 90 degrees or π / 2
  if (angle_adjacent != 0 and angle_opposite != 0):
    if (mode == "Degrees" and angle_adjacent + angle_opposite > 90) or (mode == "Radian" and angle_adjacent + angle_opposite > math.pi / 2):
      error_text = "Error: combined value of angles cannot exceed 90 degrees or π / 2"
  if (angle_adjacent != 0 and angle_opposite != 0):
    if (mode == "Degrees" and angle_adjacent + angle_opposite < 90) or (mode == "Radians" and angle_adjacent + angle_opposite < math.pi / 2):
      error_text = "Error: combined value of input angles must be equal 90 degrees or π / 2"


  if side_hypotenuse == 0 and side_adjacent == 0 and side_opposite == 0:
    error_text = "Error: At least one length value must be entered"
  
  print(error_text)

  self.error_message.config(text=error_text)


class DisplayHelp:

  def __init__(self, partner):
    background = "#ffe6cc"
    self.help_box = Toplevel()

    partner.help_button.config(state=DISABLED)

    self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                       partner))

    self.help_frame = Frame(self.help_box,
                            width=300,
                            height=200,
                            bg=background)

    self.help_frame.grid()

    self.help_heading_label = Label(self.help_frame,
                                    bg=background,
                                    text="Help / Info",
                                    font=("Arial", "14", "bold"))
    self.help_heading_label.grid(row=0)

    help_text = "insert help info here"

    self.help_text_label = Label(self.help_frame,
                                 bg=background,
                                 text=help_text,
                                 wrap=350,
                                 justify="left")
    self.help_text_label.grid(row=1, padx=10)

    self.dismiss_button = Button(self.help_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 bg="#CC6600",
                                 fg="#FFFFFF",
                                 command=partial(self.close_help, partner))
    self.dismiss_button.grid(row="2")

  def close_help(self, partner):
    partner.help_button.config(state=NORMAL)
    self.help_box.destroy()


# Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()
