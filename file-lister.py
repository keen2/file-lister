#!/usr/bin/env python
"""Script scans for files and subfolders in a directory and writes to file 
a list of data structured by hierarchy.
Requires Python 3.4 for pathlib module.
"""

__author__ = "Andrei Ermishin"
__copyright__ = "Copyright (c) 2019"
__credits__ = []
__license__ = "MIT"
__version__ = "1.1.2"
__maintainer__ = "Andrei Ermishin"
__email__ = "andrey.yermishin@gmail.com"
__status__ = "Prototype"


usage = '\nNote, usage: %s dir_path file_path\n'
usage += 'Shortly for current directory: %s . file_name\n'
usage += 'Print to the console if no file_path is given: %s .\n'


# ICON_GIF = 'documents-icon24.png'
# # This will convert a GIF/PNG to python source code.
# import base64
# with open(ICON_GIF, 'rb') as f_icon:
#     print("icon='''\\\n", base64.encodebytes(f_icon.read()).decode(), "'''")
ICON24 = '''
iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAFMUlEQVR42oVWa2xUVRCembv3Ltsu
xbbbVheE0gIhMSAKUeODxMQEMRilUEUkQY3a0AUSDJjgK1HBYCSCsMXyw58kxAA+kGgNBMH4A0IU
E0ikCAWqlhar9kH3ce8945xz77ZLETxpes9jZr6Z78zMWYRwuMefXcu5zApQ3mQk2bCQgRiQfJQ1
yxrMPiLKfwZmZF++SqZK5kp2fTmynA6wSz62Z+/arO2iMf594z6v76+FYFnGCBEotHzKUiX4VQ8r
JptI7DIaDW1KQypUipTelLkAipYH1PMdxLxuwLLEZ/b9exrw/J4FDyWd7FGFpIh8sSP65Ku/sY68
O7cAshcoj4wAoPA1ARX2ZI4RBSfXUjV0QFcuNhd3rZ+1ofGBqtc9z2WvtJ5VzYMStcLB+L0ciSW0
bkDJyCiskWXkclmwbWdYRkjFXN9lrmlfQ20nhzbipuVT0+sWTUz1lsxR7sw3iL2MFlNCMIU6BY//
MwJ9JWfO/CLRWyR4kEwmFTlxsg4vgb0/XG7BDcvq0+ueHJ/6/a5PhCWbgoivMXpTAG00m80oyQQD
pmRAJEb+t8tg/4kQINUwI9U9czt72T7u6enRiYI6MUZREg5GscT6K7Z4woQJ4ObzePHiRY7YNlRX
V6MVjTMefI4O/NgjAE8n082N96UuTd+k0M9QLu+LbpcQzzeIgJXrl1JpSZV4Hch4nqc6Oy+R40Sh
srJSKCol52gTHDh2QQAWVaZffnx66vyMVqXyWYpmDsPdFd9I5lijALCwVJLO9FXnGmVbQIlEAjzX
Va7nCsAYOfUVWzGKti2GtlP9ArA4kX5pfl3q57qPOJ/N8Hg+CLNqfkKfdZUVKBKiBYPCNVKO955r
llWEKyorwHdd7O7uZhSfym8ZhxQt4YrDz9Ch9mwA8PwjdakjiVdV3dgTVOuchmqrU4qrhMCKit2o
Aq1pcjwIgcCnc95sBcolIUy8zilfItBODLhlqmPoHpp44hU48mumBd9tSKSXL6xPJeuF9OyguBqR
69Nlqy+WtVFtmU1BmV4RRETsoqlns4FaKkwEub7YWD51fIg+P/RHC77ZmGx5Z3Wy2R3Ky4k0CQp5
ZyiaczA3vUK6DqHmT1GxDIRwpOUVWaVj4K0POnfgh6n61jVPxJtyHlyrcN080DZ9J1jdVD7iAGzb
d3Unbl1R27p6QVmTZKfSN0nDXoyOIEyq/wMw59IeIwTpL/sEoGlS66rHDIA2zSZfKCyuAAzN7ghA
gXvpRXJvFGYaG4hwzuw4ROn9ArDlxdrWVfPjJoKg9IN2fQ2nuuiYYMTDoFUY2OsokjsSWEcoSh8Y
EIAXJraufHRsU94NAQI71ykM13IRgJa5kbwG2P51/07cuPTWlnULKpo1RWz+wrKlkCJdXsPzkLKA
PtOQtHBQklxEEQlFQJu/6N2BbzeUb39t4W0rM748TwWiR7yEAhVBFmniUT+SuqyV4W2YRgqrIrhk
Ry75/T1daVw6d9yqXe/N2TZw+jd5JtE4r19YLGrXqMGkBUlFa9fDelEBdYZZMLURNl55r5jid9TC
8vXHVqMTtRKnttZ1TJkUj/dfligob9o1m4xC8BWY19+ungPen6dFfShs37q0pa+V3C4rFznbxezr
bcJ4uY2XBrzBWSvbJ5vuUhXDeQfT0z6d1nulLH81A3bctIsgD3XCa71oHDg/FBZt0SA7yF3fg2yv
CyXVpdAeL++ft/b8U92Dqg2LRGumVNlL6ipwqvxEQRg9OHT6BkOfKJf5wj989uwVd7csu/X+v4fr
vDwfoGHwAAAAAElFTkSuQmCC
'''


import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# For low-level path manipulation on strings: import os.
# New module offers classes representing filesystem paths.
from pathlib import Path

from datetime import date
import threading

# 4 x 3
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

DEF_FNAME = 'FileLister'

ALL = 'All'
MOVIES = 'Movies'
MUSIC = 'Music'
PHOTO = 'Photo'
BOOKS = 'Books'
CODE = 'Code'

TXT = '.txt'
HTM = '.htm'

FILE_TYPES = {
    ALL:    ['*'],
    MOVIES: ['3GP', 'ASF', 'AVI', 'FLV', 'M4P', 'M4V', 'MKV', 'MOV', 'MPG',
             'MPEG', 'MP4', 'MTS', 'M2TS', 'QT', 'TS', 'VOB', 'WEBM', 'WMV'],
    MUSIC:  ['AAC', 'DTS', 'M4A', 'MP3', 'WAV', 'WMA'],
    PHOTO:  ['BMP', 'GIF', 'JPG', 'JPEG', 'PNG', 'RAW', 'SVG'],
    BOOKS:  ['DJVU', 'DOC', 'DOCX', 'EPUB', 'FB2', 'ODT', 'PDF',
             'RTF', 'TIFF', 'TXT'],
    CODE:   ['BAT', 'C', 'CC', 'CPP', 'CS', 'GO', 'H', 'HH', 'HPP', 'IPYNB',
             'JAVA', 'JS', 'M', 'PHP', 'PL', 'PY', 'R', 'RB', 'SWIFT']
}


def size2str(num, suffix='B'):
    """Convert size from bytes to human readable string."""
    for unit in ('', 'K', 'M', 'G', 'T'):
        if abs(num) < 1024.0:
            return '{:3.1f} {}{}'.format(num, unit, suffix)
        num /= 1024.0
    return '>1000 TB'

def dir_size(dir_path):
    """Return size of a directory in bytes."""
    return sum(path.stat().st_size for path in dir_path.rglob('*'))

def scan_directory(dir_path, console=False):
    """Return strings of files and directories in tree-like manner.
    Recursively yield all entries in dir_path Path object with rglob().
    """
    dir_path_str = str(dir_path.resolve())
    str_date = date.today().strftime('%d.%m.%Y')
    header = 'File listing on {} for:\n'.format(str_date)
    stars = '*' * len(dir_path_str) + '\n'
    try:
        size = 'Size: ' + size2str(dir_size(dir_path)) + '\n\n'
        yield header + stars + dir_path_str + '\n' + stars + size

        prev_depth = 0
        for path in sorted(dir_path.rglob('*')):
            depth = len(path.relative_to(dir_path).parts)
            indent = ' ' * 5 * (depth-1)
            name = indent + path.name
            v_ind = '\n' if depth != prev_depth and not path.is_dir() else ''
            dot1 = '-'
            dot2 = ' '
            if path.is_dir():
                size = size2str(dir_size(path))
                data = '\n{:{fill}<130}[{}]'.format(name, size, fill=dot1)
            else:
                size = size2str(path.stat().st_size)
                data = '{:{fill}<120}{}'.format(name, size, fill=dot2)
            prev_depth = depth
            yield v_ind + data
    except MemoryError as m_err:
        tip = '\n\nTry folder with less depth or less small files.'
        if not console:
            messagebox.showerror(m_err.__class__.__name__, str(m_err) + tip)
        else:
            print(m_err, tip)
    except Exception as e:
        if not console:
            messagebox.showerror(e.__class__.__name__, str(e))
        else:
            print(e)


class Window(ttk.Frame):
    """Class is used to create GUI for scanning files in directories."""

    def __init__(self, master=None):
        """Construct a Ttk Frame."""
        # The class instance (=self) will be content=ttk.Frame(root)
        super().__init__(master)
        self.master = master    # it's root=tk.TK()
        self.dir_path = Path.cwd()
        self.file_path = self.dir_path.joinpath(DEF_FNAME
                                                + str(date.today()) + TXT)
        
        self.create_widgets()
        self.arrange_widgets()
        self.set_defaults()
    
    def create_widgets(self):
        """Create widgets within main frame (self)."""
        # dir_frame
        self.dir_frame = ttk.Labelframe(self.master, text='Directory to scan')
        self.choose_dir_btn = ttk.Button(self.dir_frame, text='Open...',
                                    command=self.open_dir_dlg)
        self.dir_lbl = ttk.Label(self.dir_frame)
        self.dir_lbl_text = tk.StringVar()
        self.dir_lbl['textvariable'] = self.dir_lbl_text

        # file_frame
        self.file_frame = ttk.Labelframe(self.master, text='File to save')
        self.save_file_btn = ttk.Button(self.file_frame, text='Save as...',
                                    command=self.save_file_dlg)
        self.file_lbl = ttk.Label(self.file_frame)
        self.file_lbl_text = tk.StringVar()
        self.file_lbl['textvariable'] = self.file_lbl_text

        
        # options_frame
        self.options_frame = ttk.Labelframe(self.master,
                                            text='Options to run')
        self.opt_chk_frame = ttk.Frame(self.options_frame)
        self.opt_ftype_frame = ttk.Frame(self.options_frame)
        self.opt_file_frame = ttk.Frame(self.options_frame)
        self.opt_run_frame = ttk.Frame(self.options_frame)
        
        self.scan_subfolders = tk.BooleanVar()
        self.scan_subf_chk = ttk.Checkbutton(self.opt_chk_frame,
                                text='Scan subfolders',
                                variable=self.scan_subfolders, onvalue=True)
        self.include_dirs = tk.BooleanVar()
        self.incl_dirs_chk = ttk.Checkbutton(self.opt_chk_frame,
                                text='Include directories',
                                variable=self.include_dirs, onvalue=True)
        
        self.sep1 = ttk.Separator(self.options_frame, orient='vertical')
        self.ftype = tk.StringVar()
        self.ftype_rbtns = []
        for typ in FILE_TYPES:
            rbtn = ttk.Radiobutton(self.opt_ftype_frame, text=typ,
                                    variable=self.ftype, value=typ)
                                    # command=self.set_ftype_to_scan)
            self.ftype_rbtns.append(rbtn)
        
        self.sep2 = ttk.Separator(self.options_frame, orient='vertical')
        self.to_file_lbl = ttk.Label(self.opt_file_frame, text='Output:')
        self.to_file = tk.StringVar()
        self.txt_rbtn = ttk.Radiobutton(self.opt_file_frame, text=TXT,
                                        variable=self.to_file, value=TXT,
                                        command=self.set_ext)
        self.htm_rbtn = ttk.Radiobutton(self.opt_file_frame, text=HTM,
                                        variable=self.to_file, value=HTM,
                                        command=self.set_ext)
        
        self.sep3 = ttk.Separator(self.options_frame, orient='vertical')
        self.run_btn = ttk.Button(self.opt_run_frame, text='Run',
                                    command=self.run_scan_dir)
        self.progressbar = ttk.Progressbar(self.opt_run_frame,
                                            orient='horizontal',
                                            length=WINDOW_WIDTH//5,
                                            mode='determinate')
        
        
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

        self.dir_frame.pack(fill='x', padx=frame_x, pady=frame_y+10)
        self.choose_dir_btn.pack(side='left', padx=btn_x, pady=btn_y+5)
        self.dir_lbl.pack(side='right', padx=btn_x, pady=btn_y+5)

        self.file_frame.pack(fill='x', padx=frame_x, pady=frame_y)
        self.save_file_btn.pack(side='left', padx=btn_x, pady=btn_y+5)
        self.file_lbl.pack(side='right', padx=btn_x, pady=btn_y+5)

        
        self.options_frame.pack(fill='x', padx=frame_x, pady=frame_y+10)
        
        self.opt_chk_frame.pack(side='left')
        self.scan_subf_chk.pack(padx=btn_x, pady=btn_y/2, anchor='w')
        self.incl_dirs_chk.pack(padx=btn_x, pady=btn_y/2, anchor='w')

        self.sep1.pack(side='left', fill='y')
        self.opt_ftype_frame.pack(side='left')
        self.ftype_rbtns[0].pack(padx=btn_x+10, pady=(btn_y, 0), anchor='w')
        for rbtn in self.ftype_rbtns[1:-1]:
            rbtn.pack(padx=btn_x+10, anchor='w')
        self.ftype_rbtns[-1].pack(padx=btn_x+10, pady=(0, btn_y), anchor='w')
        
        self.sep2.pack(side='left', fill='y')
        self.opt_file_frame.pack(side='left')
        self.to_file_lbl.pack(padx=btn_x+10, pady=btn_y/2)
        self.txt_rbtn.pack(padx=btn_x+10, pady=btn_y/2, anchor='w')
        self.htm_rbtn.pack(padx=btn_x+10, pady=btn_y/2, anchor='w')

        self.sep3.pack(side='left', fill='y')
        self.opt_run_frame.pack(side='left')
        self.run_btn.pack(padx=3*btn_x, pady=(btn_y, 0))
        self.progressbar.pack(pady=(0, btn_y))

        
        self.bottom_frame.pack(side='bottom', fill='x',
                                padx=frame_x, pady=frame_y)
        self.about_btn.pack(side='left', padx=btn_x, pady=btn_y)
        self.quit_btn.pack(side='right', padx=btn_x, pady=btn_y)
    
    def set_defaults(self):
        """Set default values for widgets."""
        self.file_lbl_text.set(str(self.file_path))
        self.dir_lbl_text.set(str(self.dir_path))

        self.scan_subfolders.set(True)
        self.include_dirs.set(True)
        self.ftype.set(ALL)
        for rbtn in self.ftype_rbtns[1:]:
            rbtn.config(state='disabled')
        self.to_file.set(TXT)
        self.htm_rbtn.config(state='disabled')
    
    # def set_ftype_to_scan(self):
    #     self.ftype.get()
    
    def set_ext(self):
        """Set extension of file_path and its label."""
        self.file_path = self.file_path.with_suffix(self.to_file.get())
        self.file_lbl_text.set(str(self.file_path))
    
    def open_dir_dlg(self):
        """Open dialog window for choosing a directory to scan."""

        dir_name = filedialog.askdirectory(initialdir=str(self.dir_path))
        if dir_name:
            self.dir_path = Path(dir_name)
            self.dir_lbl_text.set(dir_name)

    def save_file_dlg(self):
        """Open dialog window which allows to choose a path for saving."""

        fname = filedialog.asksaveasfilename(defaultextension=TXT,
                            filetypes=[('Text File', TXT), ('Web Page', HTM)],
                            initialdir=self.file_path.parent,
                            initialfile=self.file_path.stem)
        if fname:
            self.file_path = Path(fname)
            ext = self.file_path.suffix
            if ext in [TXT, HTM]:
                self.file_lbl_text.set(fname)
                self.to_file.set(ext)
            else:
                self.file_path = self.file_path.with_suffix(TXT)
                self.file_lbl_text.set(str(self.file_path))
                self.to_file.set(TXT)
    
    def run_scan_dir(self):
        """Start new thread for showing animation of progressbar."""
        self.run_btn.state(['disabled'])
        threading.Thread(target=self.scan_dir_thread, daemon=True).start()
    
    def scan_dir_thread(self):
        """Write scanning results of selected directory to a given file."""
        num_items = 0
        for item in self.dir_path.rglob('*'):
            num_items += 1
        
        self.progressbar["maximum"] = num_items
        self.progressbar.start()
        with self.file_path.open('w', encoding='utf-8') as fhand:
            for item in scan_directory(self.dir_path):
                print(item, sep='\n', file=fhand)
                self.progressbar.step()
        self.run_btn.state(['!disabled'])
        self.progressbar.stop()
        self.progressbar["value"] = num_items

    def about_dlg(self):
        """Open window with info about the application."""

        msg = '{}\nversion: {}\n\n{} by {}'.format(DEF_FNAME,
                        __version__, __copyright__, __author__)
        messagebox.showinfo('About ' + DEF_FNAME, msg)


def main(argv):
    """Uses GUI class or console to scan folders depending on arguments."""
    # Run GUI.
    if len(argv) == 1:
        root = tk.Tk()
        # Pass a toplevel widget of tkinter as main window of the application.
        app = Window(root)
        app.master.title('FileLister ' + __version__[:-2])
        # Set the icon (must keep a reference from destroying by GC).
        img = tk.PhotoImage(data=ICON24)
        app.master.tk.call('wm', 'iconphoto', app.master._w, img)
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
            dir_path = Path(argv[1])

            # Print to given file.
            # In Windows cmd:
            # powershell -command "iex \"tree d:\movies /F\" > \"d:\123.txt\""
            if len(argv) > 2:
                print('Scanning...\n')
                file_path = Path(argv[2]).with_suffix(TXT)
                with file_path.open('w', encoding='utf-8') as fhand:
                    print(*scan_directory(dir_path, console=True),
                            sep='\n', file=fhand)
                print('\n\nData is written to: ' + file_path.name)
            # Print to console if no file_path entered.
            else:
                print(*scan_directory(dir_path, console=True), sep='\n')
                # In Windows cmd: tree d:\movies /F
        else:
            print('Invalid directory path!!!\n', usage.replace('%s', argv[0]))


if __name__ == "__main__":
    import sys

    main(sys.argv)


# TODO:
# make padx,pady unified
# option-> music,photo,text/books, code
# .htm -> (tree)

# (D:\Programming\Study\Git)add instruction how to add and 
# add screen: ![#2](screenshots/example-2.png?raw=true)
