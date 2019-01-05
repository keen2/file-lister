#!/usr/bin/env python
"""Script scans for files and subfolders in a directory and writes to file 
a list of data structured by hierarchy.
Requires Python 3.4 for pathlib module.
"""

__author__ = "Andrei Ermishin"
__copyright__ = "Copyright (c) 2019"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.4"
__maintainer__ = "Andrei Ermishin"
__email__ = "andrey.yermishin@gmail.com"
__status__ = "Prototype"


usage = '\nNote, usage: %s dir_path file_path\n'
usage += 'Shortly for current directory: %s . file_name\n'
usage += 'Print to the console if no file_path is given: %s .\n'


import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# For low-level path manipulation on strings: import os.
# New module offers classes representing filesystem paths.
from pathlib import Path

from datetime import date

# 16 x 9
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 360

DEF_FNAME = 'FileLister'


def scan_directory(dir_path):
    """Return strings of files and directories in tree-like manner.
    Recursively yield all entries in dir_path Path object with rglob().
    """
    yield '+ {}'.format(dir_path.resolve())

    for path in sorted(dir_path.rglob('*')):
        depth = len(path.relative_to(dir_path).parts)
        indent = '|   ' * depth
        yield '{}+ {}'.format(indent, path.name)
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
        
        self.create_widgets()
        self.arrange_widgets()
    
    def create_widgets(self):
        """Create widgets within main frame (self)."""
        # dir_frame
        self.dir_frame = ttk.Labelframe(self.master, text='Directory to scan')
        self.choose_dir_btn = ttk.Button(self.dir_frame, text='Open...',
                                    command=self.open_dir_dlg)
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
        self.options_frame = ttk.Labelframe(self.master,
                                            text='Options to run')
        self.scan_subfolders = tk.BooleanVar()
        self.scan_subfolders.set(True)
        self.scan_subf_chk = ttk.Checkbutton(self.options_frame,
                                text='Scan subfolders',
                                variable=self.scan_subfolders, onvalue=True)
        self.include_dirs = tk.BooleanVar()
        self.include_dirs.set(True)
        self.incl_dirs_chk = ttk.Checkbutton(self.options_frame,
                                text='Include directories',
                                variable=self.include_dirs, onvalue=True)
        self.run_btn = ttk.Button(self.options_frame, text='Run',
                                    command=self.run_scan_dir)
        self.progressbar = ttk.Button(self.options_frame, text='Progressbar',
                                    command=self.master.destroy)
        
        # bottom_frame
        self.bottom_frame = ttk.Frame(self.master)
        self.about_btn = ttk.Button(self.bottom_frame, text='About',
                                    command=self.about_dlg)
        self.quit_btn = ttk.Button(self.bottom_frame, text='Exit',
                                    command=self.master.destroy)

    def arrange_widgets(self):
        """Organaze and show widgets."""

        frame_x = 20
        frame_y = 5
        btn_x = 20
        btn_y = 10

        self.dir_frame.pack(fill='x', padx=frame_x, pady=frame_y)
        self.choose_dir_btn.pack(side='left', padx=btn_x, pady=btn_y+5)
        self.dir_lbl.pack(side='right', padx=btn_x, pady=btn_y+5)

        self.file_frame.pack(fill='x', padx=frame_x, pady=frame_y)
        self.save_file_btn.pack(side='left', padx=btn_x, pady=btn_y+5)
        self.file_lbl.pack(side='right', padx=btn_x, pady=btn_y+5)

        self.options_frame.pack(fill='x', padx=frame_x, pady=frame_y+10)
        self.scan_subf_chk.pack(side='left', padx=btn_x)
        self.incl_dirs_chk.pack(side='left', padx=btn_x)
        self.run_btn.pack(anchor='ne', padx=btn_x, pady=btn_y)
        self.progressbar.pack(anchor='se')

        self.bottom_frame.pack(side='bottom', fill='x',
                                padx=frame_x, pady=frame_y)
        self.about_btn.pack(side='left', padx=btn_x, pady=btn_y)
        self.quit_btn.pack(side='right', padx=btn_x, pady=btn_y)
    
    def open_dir_dlg(self):
        """Open dialog window for choosing a directory to scan."""

        dir_name = filedialog.askdirectory(initialdir=str(self.dir_path))
        if dir_name:
            self.dir_path = Path(dir_name)
            self.dir_lbl_text.set(dir_name)

    def save_file_dlg(self):
        """Open dialog window which allows to choose a path for saving."""

        fname = filedialog.asksaveasfilename(defaultextension='.txt',
                    filetypes=[('Text files', '.txt'), ('All files', '.*')],
                    initialdir=self.file_path.parent,
                    initialfile=self.file_path.stem)
        if fname:
            self.file_path = Path(fname)
            self.file_lbl_text.set(fname)
    
    def run_scan_dir(self):
        """Write scanning results of selected directory to a given file."""

        found_files = scan_directory(self.dir_path)
        with self.file_path.open('w') as fhand:
            print(*found_files, sep='\n', file=fhand)

    def about_dlg(self):
        """Open window with an info about the application"""

        msg = '{}\nversion: {}\n\n{} by {}'.format(DEF_FNAME,
                        __version__, __copyright__, __author__)
        messagebox.showinfo('About ' + DEF_FNAME, msg)


def main(argv):
    """Uses GUI class or console to scan folders depending on arguments."""
    # Run GUI.
    if len(argv) == 1:
        # Create a toplevel widget of tkinter as main window of application.
        root = tk.Tk()
        app = Window(root)
        app.master.title('FileLister ' + __version__[:-2])
        # Center the window to be right under an appearing messagebox.
        window_x = int(root.winfo_screenwidth()/2 - WINDOW_WIDTH/2)
        window_y = int(root.winfo_screenheight()*2/5 - WINDOW_HEIGHT/2)
        app.master.geometry('{}x{}+{}+{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT,
                                                 window_x, window_y))
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
            print('Invalid directory path!!!\n', usage.replace('%s', argv[0]))


if __name__ == "__main__":
    import sys

    main(sys.argv)


# TODO:
# view/structure
# stats
# maxdepth
