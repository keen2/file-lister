#!/usr/bin/env python
'''
Script scans for files and subdirectories in a directory and writes to file 
a list of data structured by hierarchy.
'''

__author__ = "Andrei Ermishin"
__copyright__ = "Copyright 2018"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Andrei Ermishin"
__email__ = "andrey.yermishin@gmail.com"
__status__ = "Prototype"


import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog

import os


class Application(tk.Frame):
    '''Class is used to make structured text of files list at directories.'''

    def __init__(self, master=None):
        '''Constructor for Application.'''
        # make the application actually appear on the screen
        super().__init__(master)


def main(argv):
    # Create a toplevel widget of tkinter as main window of an application
    app = Application()
    # Set title of master frame
    app.master.title("FileLister")
    # Run the main loop of Tcl.
    app.mainloop()


if __name__ == "__main__":
    # execute only if run as a script
    import sys

    main(sys.argv)


# TODO:
# -if posiible do it recursively
# -argv[0]=self, argv[1]=source/dir, argv[2]=dest/file
