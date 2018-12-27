#!/usr/bin/env python
"""Script scans for files and subdirectories in a directory and writes to file 
a list of data structured by hierarchy.
Requires Python 3.4 for pathlib module.
"""

__author__ = "Andrei Ermishin"
__copyright__ = "Copyright 2018"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.2"
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

from datetime import date

# 16 x 9
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 450

DEF_FNAME = 'FileLister'


def scan_directory(path):
    """Input: Path object of directory.
    ######## desc
    Returns a list of files and directories along given path.
    ######## desc
    """
    # def tree(directory):
    #     print(f'+ {directory}')
    #     for path in sorted(directory.rglob('*')):
    #         depth = len(path.relative_to(directory).parts)
    #         spacer = '    ' * depth
    #         print(f'{spacer}+ {path.name}')
    # Output:
    # >>> tree(pathlib.Path.cwd())
    # + /home/gahjelle/realpython
    #     + directory_1
    #         + file_a.md
    #     + directory_2
    #         + file_a.md
    #         + file_b.pdf
    #         + file_c.py
    #     + file_1.txt
    #     + file_2.txt
    entries_list = []
    # recursive - rglob()
    # Filter
    # for entry in pathlib_path.glob('*.py'):
    for entry in path.iterdir():
        # if entry.is_dir():
        entries_list.append(entry.name)

    return entries_list


class Window(ttk.Frame):
    """Class is used to create GUI for scanning files in directories."""

    def __init__(self, master=None):
        """Construct a Ttk Frame."""
        # The class instance (=self) will be content=ttk.Frame(root)
        super().__init__(master)
        self.master = master    # it's root=tk.TK()
        self.dir_path = Path.cwd()
        self.file_path = self.dir_path.joinpath(DEF_FNAME 
                                                + str(date.today()) + '.txt')
        self.frame_padx = 15
        self.frame_pady = 10
        
        self.create_widgets()
        self.arrange_widgets()
    
    def create_widgets(self):
        """Create widgets within main frame (self)."""
        # dir_frame
        self.dir_frame = ttk.Labelframe(self.master, text='Directory to scan')
        self.choose_dir_btn = ttk.Button(self.dir_frame, text='Choose...',
                                    command=self.master.destroy)
        self.dir_lbl = ttk.Label(self.dir_frame)
        self.dir_lbl_text = tk.StringVar()
        self.dir_lbl['textvariable'] = self.dir_lbl_text
        self.dir_lbl_text.set(str(self.dir_path))

        # file_frame
        self.file_frame = ttk.Labelframe(self.master, text='File to save')
        self.save_file_btn = ttk.Button(self.file_frame, text='Save as...',
                                    command=self.save_file_dlg)
        self.file_lbl = ttk.Label(self.file_frame)
        self.file_lbl_text = tk.StringVar()
        self.file_lbl['textvariable'] = self.file_lbl_text
        self.file_lbl_text.set(str(self.file_path))

        # options_frame
        self.options_frame = ttk.Labelframe(self.master, text='Options')
        self.scan_subfolders = tk.BooleanVar()
        self.scan_subfolders.set(True)
        self.scan_subf_chk = ttk.Checkbutton(self.options_frame, 
                                text='Scan subfolders', 
                                variable=self.scan_subfolders, onvalue=True)

        self.run_btn = ttk.Button(self.master, text='Run',
                                    command=self.master.destroy)
        self.about_btn = ttk.Button(self.master, text='About',
                                    command=self.master.destroy)
        self.quit_btn = ttk.Button(self.master, text='Exit',
                                    command=self.master.destroy)

    def arrange_widgets(self):
        """Organaze and show widgets."""

        self.dir_frame.pack(fill='x', 
                            padx=self.frame_padx, pady=self.frame_pady)
        self.choose_dir_btn.pack(side='left', padx=20, pady=20)
        self.dir_lbl.pack(side='right', padx=20, pady=20)

        self.file_frame.pack(fill='x', 
                            padx=self.frame_padx, pady=self.frame_pady)
        self.save_file_btn.pack(side='left', padx=20, pady=20)
        self.file_lbl.pack(side='right', padx=20, pady=20)

        self.options_frame.pack(fill='x',
                                padx=self.frame_padx, pady=self.frame_pady)
        self.scan_subf_chk.pack()

        self.run_btn.pack(side='right', padx=20, pady=20)
        self.about_btn.pack(side='left', padx=20, pady=20)
        self.quit_btn.pack(side='right', padx=20, pady=20)
    
    def save_file_dlg(self):
        """Open dialog window which allows to choose a path for saving."""

        fname = filedialog.asksaveasfilename(defaultextension='.txt', 
                    filetypes=[('All files', '.*'), ('Text files', '.txt')], 
                    initialfile=DEF_FNAME + str(date.today()))
        if fname:
            self.file_path = Path(fname)
            self.file_lbl_text.set(fname)


def main(argv):
    """Uses GUI class or console to scan folders depending on arguments."""
    # Run GUI.
    if len(argv) == 1:
        # Create a toplevel widget of tkinter as main window of an application
        root = tk.Tk()
        app = Window(root)
        app.master.title('FileLister ' + __version__[:-2])
        app.master.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        app.master.resizable(False, False)
        # Run the main loop of Tcl.
        app.master.mainloop()
    
    # Use console.
    elif len(argv) > 1:
        if Path(argv[1]).is_dir():
            # Path object is returned.
            dir_path = Path(argv[1])
            found_files = scan_directory(dir_path)

            # Print to given file.
            if len(argv) > 2:
                file_path = Path(argv[2]).with_suffix('.txt')
                with file_path.open('w') as fhand:
                    print(*found_files, sep='\n', file=fhand)
            # Print to console if no file_path entered.
            else:
                print(*found_files, sep='\n')

        else:
            print('Invalid directory path!', usage.replace('%s', argv[0]))


if __name__ == "__main__":
    import sys

    main(sys.argv)


# TODO:
# - arrange_widgets()
# from tkinter import messagebox
# messagebox.showinfo(title='12345', message='About')
# =messagebox.askquestion("Simple Question", "Do you love Python?")

# - scan_directory()
# - if posiible do scan recursively
# - maxdepth
