from tkinter import *
from tkinter import ttk

class Converter:
    def __init__(self):
        
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

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()