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


usage = '\nNote, usage: %s dir_path file_path\n'
usage += 'Shortly for current directory: %s . file_name\n'


import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog

# For low-level path manipulation on strings: import os.
# New module offers classes representing filesystem paths.
from pathlib import Path


def scan_directory(path):
    '''
    Returns a list of files and directories along given path.
    ######## desc
    '''
    entries_list = []
    # Filter
    # for entry in pathlib_path.glob('*.py'):
    for entry in path.iterdir():
        # if entry.is_dir():
        entries_list.append(entry.name)

    return entries_list


class Application(tk.Frame):
    '''
    Class is used to create GUI for scanning files in directories.
    '''

    def __init__(self, master=None):
        '''Constructor for Application.'''
        # make the application actually appear on the screen
        super().__init__(master)


def main(argv):

    # Run GUI.
    if len(argv) == 1:
        # Create a toplevel widget of tkinter as main window of an application
        app = Application()
        app.master.title('FileLister ' + __version__[:-2])
        app.master.geometry('640x480')
        app.master.resizable(False, False)
        # Run the main loop of Tcl.
        app.mainloop()
    
    # Use console.
    elif len(argv) > 1:
        if Path(argv[1]).is_dir():
            # Path object is returned.
            dir_path = Path(argv[1])
            found_files = scan_directory(dir_path)

            # Print results to file.
            if len(argv) > 2:
                file_path = Path(argv[2])###
                with file_path.open('w') as fhand:
                    print(*found_files, sep='\n', file=fhand)
            
            # if no file_path print to console.
            else:
                print(*found_files, sep='\n')

        else:
            print('Invalid directory path!', usage.replace('%s', argv[0]))


if __name__ == "__main__":
    # execute only if run as a script
    import sys

    main(sys.argv)


# TODO:
# - if file_path doesn't have ".txt" (suffix)
# - if posiible do scan recursively
# - maxdepth