from tkinter import *
from functools import partial  # To prevent unwanted windows
import math

mode = "Degrees"
area = "uncalculated"
error = ""
number_saved_triangles = 0
save_file = open("history.txt", "w").close()


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
      text="Input the values for the angle sizes in the boxes below",
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
    self.display_area.grid(row=0, column=0, columnspan=2)

    self.error_message = Label(self.misc_labels_help_button,
                               text="{}".format(error),
                               fg="#9C0000",
                               width=40,
                               wraplength=300,
                               justify="center")
    self.error_message.grid(row=1, column=0, columnspan=2)

    self.help_button = Button(self.misc_labels_help_button,
                              text="Help / Info",
                              bg="#CC6600",
                              fg=button_fg,
                              font=button_font,
                              width=20,
                              command=self.help_menu)
    self.help_button.grid(row=2, column=0, pady=3, padx=10)

    self.history_button = Button(self.misc_labels_help_button,
                                 text="History",
                                 bg="#b80287",
                                 fg=button_fg,
                                 font=button_font,
                                 width=20,
                                 command=self.history_menu)
    self.history_button.grid(row=2, column=1, pady=3, padx=10)

  # Opens Helps menu
  def help_menu(self):
    DisplayHelp(self)

  def history_menu(self):
    DisplayHistory(self)

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

    # if there wasnt a value entered, set value to 0
    # Also setting value type to float so that they can be printed
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

    except ValueError:
      error_text = "Error: Non-valid value entered, e.g XI, letters, symbols"
      self.error_message.config(text=error_text)

    check_input_values(self, side_hypotenuse, side_adjacent, side_opposite,
                       angle_adjacent, angle_opposite)


def change_mode(value, self):
  global mode
  # disable degrees buton if the mode is set to degrees
  if value == "Degrees":
    # set radians button to normal
    self.to_radian_mode.config(state=NORMAL)
    # set degrees button to disabled
    self.to_degrees_mode.config(state=DISABLED)
    mode = "Degrees"

  # disable radians buton if the mode is set to radians
  if value == "Radians":
    # set degrees button to normal
    self.to_degrees_mode.config(state=NORMAL)
    # set radians button to disabled
    self.to_radian_mode.config(state=DISABLED)
    mode = "Radians"
  #change the show mode text
  self.show_mode.config(text="Mode: {}".format(value))


def check_input_values(self, side_hypotenuse, side_adjacent, side_opposite,
                       angle_adjacent, angle_opposite):
  error_text = ""
  has_error = False
  # testing if all the values have been entered, if yes print error
  if (side_hypotenuse, side_adjacent, side_opposite, angle_adjacent,
      angle_opposite).count(0) == 0:
    error_text = "Error: All values entered"
    has_error = True

  # testing if no values have been entered, if yes print error
  if (side_hypotenuse, side_adjacent, side_opposite, angle_adjacent,
      angle_opposite).count(0) == 5:
    error_text = "Error: No values entered"
    has_error = True

  # testing if the user has entered at least one length
  if (side_hypotenuse, side_adjacent, side_opposite).count(0) == 3:
    error_text = "Error: At least one length value must be entered"
    has_error = True

  # testing to see if the user has entered 2 different values
  if (side_hypotenuse, side_adjacent, side_opposite, angle_adjacent,
      angle_opposite).count(0) >= 4:
    error_text = "Error: less than two values input"
    has_error = True

  #testing to see if user has enter more than 2 values
  if (side_hypotenuse, side_adjacent, side_opposite, angle_adjacent,
      angle_opposite).count(0) <= 2:
    error_text = "Error: Please enter only 2 values, this is to avoid having miscalculations"
    has_error = True

  # testing to see if a side value is negative, if yes print error message
  if side_hypotenuse < 0 or side_adjacent < 0 or side_opposite < 0:
    error_text = "Error: Side value cannot be negative"
    has_error = True

  # testing to see if a angle value is negative, if yes print error message
  if angle_adjacent < 0 or angle_opposite < 0:
    error_text = "Error: Angle value cannot be negative"
    has_error = True

  # testing if the hypotenuse is the longest side, if yes print error message
  if (side_hypotenuse <= side_adjacent
      or side_hypotenuse <= side_opposite) and side_hypotenuse > 0:
    error_text = "Error: Hypotenuse side must be the longest side"
    has_error = True

  # testing if the input angle exceeds or is equal to 90 degrees
  if (angle_adjacent >= 90 or angle_opposite >= 90) and mode == "Degrees":
    error_text = "Error: angle cannot equal or exceed 90 degrees"
    has_error = True

  # testing if the input angle exceeds or is equal
  if (angle_adjacent >= math.pi / 2
      or angle_opposite >= math.pi / 2) and mode == "Radians":
    error_text = "Error: angle cannot equal or exceed π/2 or 1.5707... radians"
    has_error = True

  # testing if angle is negative
  if angle_adjacent < 0 or angle_opposite < 0:
    error_text = "Error: angle cannot be negative"
    has_error = True

  self.error_message.config(text=error_text)
  if has_error == False:
    Calculations(self, side_hypotenuse, side_adjacent, side_opposite,
                 angle_adjacent, angle_opposite)


def Calculations(self, side_hypotenuse, side_adjacent, side_opposite,
                 angle_adjacent, angle_opposite):
  # if the mode is set to degrees, setting the angle values to radians
  if mode == "Degrees":
    # making the angle values radians
    angle_adjacent = math.radians(angle_adjacent)
    angle_opposite = math.radians(angle_opposite)

  #*********************calculations (sides)*********************
  # continue looping until all sides are worked out
  while (side_hypotenuse, side_adjacent, side_opposite).count(0) != 0:

    # test to see if there is only one unknown side
    if (side_hypotenuse, side_adjacent, side_opposite).count(0) == 1:

      # test if the hypotenuse is the unknown side
      if side_hypotenuse == 0:
        side_hypotenuse = math.sqrt(
          math.pow(side_adjacent, 2) +
          math.pow(side_opposite, 2))  #A² + B² = C²

      # test if the adjacent is the unknown side
      elif side_adjacent == 0:
        side_adjacent = math.sqrt(
          math.pow(side_hypotenuse, 2) -
          math.pow(side_opposite, 2))  #A² = C² - B²

      # test if the opposite is the unknown sideside
      elif side_opposite == 0:
        side_opposite = math.sqrt(
          math.pow(side_hypotenuse, 2) -
          math.pow(side_adjacent, 2))  #B² = C² - A²

    # test whether there is 2 unknown sides
    if (side_hypotenuse, side_adjacent, side_opposite).count(0) == 2:

      # Test if the adjacent side is unknown and the adjacent angle is known
      if side_adjacent == 0:
        # test if the adjacent angle is known
        if angle_adjacent != 0:
          #test if the hypotenuse side is known
          if side_hypotenuse != 0:
            #calculation for adjacent length using adjacent angle and the hypotenuse side
            side_adjacent = math.cos(angle_adjacent) * side_hypotenuse

          #test if the opposite side is known
          elif side_opposite != 0:
            #calculation for adjacent side using adjacent angle and the opposite side
            side_adjacent = math.tan(angle_adjacent) * side_opposite

        # test if the opposite angle is known
        if angle_opposite != 0:
          # test if the hypotenuse side is known
          if side_hypotenuse != 0:
            #calculation for adjacent length using adjacent angle and the hypotenuse side
            side_adjacent = math.cos(angle_opposite) * side_hypotenuse

          #test if the opposite side is known
          elif side_opposite != 0:
            #calculation for adjacent side using adjacent angle and the opposite side
            side_adjacent = math.tan(angle_opposite) * side_opposite

      # Test if the oppostie side is unknown and is the opposite angle is known
      elif side_opposite == 0:
        # test if the opposite angle is known
        if angle_opposite != 0:
          #see if the hypotenuse side is known
          if side_hypotenuse != 0:
            #calculation for opposite side using adjacent angle and the hypotenuse side
            side_opposite = math.sin(angle_opposite) * side_hypotenuse

          # Test if the adjacent side is known
          elif side_adjacent != 0:
            #calculation for opposite side using adjacent angle and the adjacent side
            side_opposite = math.tan(angle_opposite) * side_adjacent

        # test if the adjacent angle is known
        elif angle_adjacent != 0:
          #see if the hypotenuse side is known
          if side_hypotenuse != 0:  #see if the hypotenuse side is known
            side_opposite = math.sin(angle_adjacent) * side_hypotenuse

          # Test if the adjacent side is known
          elif side_adjacent != 0:
            #calculation for opposite side using adjacent angle and the adjacent side
            side_opposite = math.tan(angle_adjacent) * side_adjacent

  #*********************Calculations (angles)*********************
  # Continue looping until both angles are known
  while (angle_adjacent, angle_opposite).count(0) != 0:

    # Testing if one angle is known
    if (angle_adjacent, angle_opposite).count(0) == 1:
      # Test if the adjacent angle is unknown and opposite angle is known
      if angle_adjacent == 0:
        angle_adjacent = (
          math.pi / 2) - angle_opposite  #calculation: Angle 1 = 90 - angle 2

      # Test if the oppostie angle is unknown and adjacent angle is known
      if angle_opposite == 0:
        angle_opposite = (
          math.pi / 2) - angle_adjacent  #calculation: Angle 2 = 90 - angle 1

    # Testing if both angles are unknown
    if angle_adjacent == 0 and angle_opposite == 0:

      # if the opposite side and hypontenuse are known, use them to work out the angles
      if side_opposite != 0 and side_hypotenuse != 0:
        angle_adjacent = math.asin(side_opposite /
                                   side_hypotenuse)  #calculation: Soh Cah Toa
        angle_opposite = math.acos(side_opposite /
                                   side_hypotenuse)  #calculation: Soh Cah Toa

      # if the adjacent side and hypontenuse are known, use them to work out the angles
      elif side_adjacent != 0 and side_hypotenuse != 0:
        angle_adjacent = math.asin(side_adjacent /
                                   side_hypotenuse)  #calculation: Soh Cah Toa
        angle_opposite = math.acos(side_adjacent /
                                   side_hypotenuse)  #calculation: Soh Cah Toa

      # if the opposite and adjacent sides are known, use them to work out the angles
      elif side_adjacent != 0 and side_opposite != 0:
        angle_adjacent = math.asin(side_opposite /
                                   side_adjacent)  #calculation: Soh Cah Toa
        angle_opposite = math.acos(side_opposite /
                                   side_adjacent)  #calculation: Soh Cah Toa

  # if the mode is on degrees transform angles into degrees,
  # because to work out the values they need to be transfomered in radians
  if mode == "Degrees":
    angle_adjacent = angle_adjacent * (180 / math.pi)
    angle_opposite = angle_opposite * (180 / math.pi)

  # This area is used to put the values into the text boxes
  self.hypotenuse_length_entry.delete(0, END)
  self.hypotenuse_length_entry.insert(0, round(side_hypotenuse, 2))

  self.adjacent_length_entry.delete(0, END)
  self.adjacent_length_entry.insert(0, round(side_adjacent, 2))

  self.opposite_length_entry.delete(0, END)
  self.opposite_length_entry.insert(0, round(side_opposite, 2))

  self.adjacent_angle_entry.delete(0, END)
  self.adjacent_angle_entry.insert(0, round(angle_adjacent, 2))

  self.opposite_angle_entry.delete(0, END)
  self.opposite_angle_entry.insert(0, round(angle_opposite, 2))

  #----------------------------------------AREA---------------------------------------
  global area
  area = round((side_adjacent * side_opposite) / 2, 2)
  self.display_area.config(text="Area: {}".format(area))

  #---------------------------------------- Saving Values --------------------------------------------

  #store values in external txt file. already formated
  global number_saved_triangles
  number_saved_triangles += 1

  save_file = open("history.txt", "a")
  save_file.write("Calculation {} triangle sizes: \n".format(
    str(number_saved_triangles)))
  save_file.write("Hypotenuse length: {} \n".format(
    str(round(side_hypotenuse, 2))))
  save_file.write("Adjacent length: {} \n".format(str(round(side_adjacent,
                                                            2))))
  save_file.write("Opposite length: {} \n".format(str(round(side_opposite,
                                                            2))))
  save_file.write("Adjacent angle: {}° \n".format(str(round(angle_adjacent,
                                                            2))))
  save_file.write("Opposite angle: {}° \n\n\n".format(
    str(round(angle_opposite, 2))))
  save_file.close()


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


class DisplayHistory:

  def __init__(self, partner):
    background = "#ffe6cc"
    self.history_box = Toplevel()

    partner.history_button.config(state=DISABLED)

    self.history_box.protocol('WM_DELETE_WINDOW',
                              partial(self.close_history, partner))

    self.history_frame = Frame(self.history_box,
                               width=300,
                               height=200,
                               bg=background)

    self.history_frame.grid()

    self.history_heading_label = Label(self.history_frame,
                                       bg=background,
                                       text="History",
                                       font=("Arial", "14", "bold"))
    self.history_heading_label.grid(row=0)

    save_file = open("history.txt", "r")
    history_text = save_file.read()
    save_file.close()

    self.history_text_label = Label(self.history_frame,
                                    bg=background,
                                    text=history_text,
                                    wrap=350,
                                    justify="left")
    self.history_text_label.grid(row=1, padx=10)

    self.dismiss_button = Button(self.history_frame,
                                 font=("Arial", "12", "bold"),
                                 text="Dismiss",
                                 bg="#CC6600",
                                 fg="#FFFFFF",
                                 command=partial(self.close_history, partner))
    self.dismiss_button.grid(row="2")

  def close_history(self, partner):
    partner.history_button.config(state=NORMAL)
    self.history_box.destroy()


# Main Routine
if __name__ == "__main__":
  root = Tk()
  root.title("Right Angle Triangle Solver")
  converter()
  root.mainloop()
