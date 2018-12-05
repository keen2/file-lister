import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog

import os


class Application(tk.Frame):
    def __init__(self, master=None):
        # make the application actually appear on the screen
        super().__init__(master)


# Create a toplevel widget of tkinter as main window of an application
app = Application()
# Set title of master frame
app.master.title('FileLister')
# Run the main loop of Tcl.
app.mainloop()
