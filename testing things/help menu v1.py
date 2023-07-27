from tkinter import *
from functools import partial  # To prevent unwanted windows


class converter:

  def __init__(self):
    # commmon format for all buttons
    # Arial size 14 bold, with white text
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"

    # Set up GUI Frame
    self.temp_frame = Frame(padx=10, pady=10)
    self.temp_frame.grid()

    self.button_frame = Frame(padx=30, pady=30)
    self.button_frame.grid(row=0)

    self.help_button = Button(self.button_frame,
                              text="Help / Info",
                              bg="#CC6600",
                              fg=button_fg,
                              font=button_font,
                              width=12,
                              command=self.help_menu)
    self.help_button.grid(row=1, column=0, padx=5, pady=5)

  #@staticmethod
  def help_menu(self):
    DisplayHelp(self)


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
  root.title("Temperature Converter")
  converter()

  root.mainloop()
