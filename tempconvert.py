from tkinter import *
from tkinter import ttk
from turtle import bgcolor

class Converter:
    def __init__(self):

        # Common formatting for all buttons
        # Arial, size 14, bold with white text
        button_font = ("Arial", "14", "bold")
        
        # Setup GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text = "Temperture Convertor", font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame, text = instructions, wrap=250, width=40, justify="center")
        self.temp_instructions.grid(row=1)

        self.temp_entry = ttk.Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="", fg="#9C0000")
        self.temp_error.grid(row=3)

        self.button_frame = ttk.Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = ttk.Button(self.button_frame, text="To Celsius", width=16, command=self.to_celsius)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = ttk.Button(self.button_frame, text="To Farenheit", width=16)
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = ttk.Button(self.button_frame, text="Help / Info", width=16)
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = ttk.Button(self.button_frame, text="History / Export", width=16, state=DISABLED)
        self.history_button.grid(row=1, column=1, padx=5, pady=5)


    def check_temp(self, min_value):
        error = "Please enter a number that is more " \
                "than {}".format(min_value)

        try:
            response = self.temp_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "yes"
            else:
                has_error = "no"
        
        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.temp_error.config(text=error, fg="#9C0000")
        else:
            self.temp_error.config(text="You are OK", fg="blue")

    def to_celsius(self):
        self.check_temp(-459)

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()