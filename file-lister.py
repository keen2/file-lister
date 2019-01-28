#!/usr/bin/env python
"""Script scans for files and subfolders in a directory and writes to
file a list of data structured by hierarchy.
Requires Python 3.4 for pathlib module.
"""

__author__ = "Andrei Ermishin"
__copyright__ = "Copyright (c) 2019"
__credits__ = []
__license__ = "MIT"
__version__ = "1.1.6"
__maintainer__ = "Andrei Ermishin"
__email__ = "andrey.yermishin@gmail.com"
__status__ = "Prototype"


import tkinter as tk
# Explicitly import some submodules:
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

# For low-level path manipulation on strings: import os.
# New module offers classes representing filesystem paths.
from pathlib import Path

from datetime import date
from threading import Thread


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

# 4 x 3
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

DEF_FNAME = 'FileLister'
LBL_TEXT_MAX = 75

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

def merged_glob(path, subdirs, types):
    """Yield all files/directories matching the given pattern."""
    pattern = '**/' * subdirs + '*.' * (types!=ALL)
    patterns = (pattern + ext for ext in FILE_TYPES[types])
    yield from (p for i in patterns for p in path.glob(i))

def dir_size(path, subdirs, include_dir, types):
    """Return size of a directory in bytes for a given file types."""
    total = 0
    # directories
    if not subdirs and include_dir:
        for item in (x for x in path.iterdir() if x.is_dir()):
            for p in merged_glob(item, True, types):
                total += p.stat().st_size
    # files
    total += sum(p.stat().st_size for p in merged_glob(path, subdirs, types))
    return total

def scan_directory(dir_path, subdirs, include_dir, is_indent,
                                                types=ALL, console=False):
    """Return strings of files and directories in tree-like manner.
    Recursively yield entries in dir_path if subdirs is True.
    """
    dir_path_str = str(dir_path.resolve())
    str_date = date.today().strftime('%d.%m.%Y')
    header = 'Listing on {} for {} files in:\n'.format(str_date, types)
    stars = '*' * len(dir_path_str) + '\n'
    try:
        size = 'Size of {} files: {}\n\n'.format(types,
                    size2str(dir_size(dir_path, subdirs, include_dir, types)))
        yield header + stars + dir_path_str + '\n' + stars + size

        prev_depth = 0
        for path in sorted(merged_glob(dir_path, subdirs, types)):
            depth = len(path.relative_to(dir_path).parts)
            indent = ' ' * 5 * (depth-1)
            name = indent * is_indent + path.name
            v_ind = '\n' if depth != prev_depth and not path.is_dir() else ''
            dot1 = '-'
            dot2 = ' '
            prev_depth = depth
            if path.is_dir():
                if not include_dir: continue
                size = size2str(dir_size(path, subdirs, include_dir, types))
                data = '\n{:{fill}<130}[{}]'.format(name, size, fill=dot1)
            else:
                size = size2str(path.stat().st_size)
                data = '{:{fill}<120}{}'.format(name, size, fill=dot2)
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
    """Class is used to create GUI for scanning files in directory."""

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
        self.dir_lbl_text = tk.StringVar()
        self.dir_lbl = ttk.Label(self.dir_frame,
                                textvariable=self.dir_lbl_text)

        # file_frame
        self.file_frame = ttk.Labelframe(self.master, text='File to save')
        self.save_file_btn = ttk.Button(self.file_frame, text='Save as...',
                                    command=self.save_file_dlg)
        self.file_lbl_text = tk.StringVar()
        self.file_lbl = ttk.Label(self.file_frame,
                                textvariable=self.file_lbl_text)

        
        # options_frame
        self.options_frame = ttk.Labelframe(self.master,
                                            text='Options to run')
        self.opt_chk_frame = ttk.Frame(self.options_frame)
        self.opt_ftype_frame = ttk.Frame(self.options_frame)
        self.opt_file_frame = ttk.Frame(self.options_frame)
        self.opt_run_frame = ttk.Frame(self.options_frame)
        
        self.scan_subdirs = tk.BooleanVar()
        self.scan_subf_chk = ttk.Checkbutton(self.opt_chk_frame,
                                text='Scan subfolders',
                                variable=self.scan_subdirs, onvalue=True,
                                command=self.set_indentation)
        self.include_dir = tk.BooleanVar()
        self.incl_dirs_chk = ttk.Checkbutton(self.opt_chk_frame,
                                text='Include directories',
                                variable=self.include_dir, onvalue=True)
        self.indent_levels = tk.BooleanVar()
        self.ind_levels_chk = ttk.Checkbutton(self.opt_chk_frame,
                                text='Indent levels',
                                variable=self.indent_levels, onvalue=True)
        
        self.sep1 = ttk.Separator(self.options_frame, orient='vertical')
        self.ftype = tk.StringVar()
        self.ftype_rbtns = []
        for typ in FILE_TYPES:
            rbtn = ttk.Radiobutton(self.opt_ftype_frame, text=typ,
                                    variable=self.ftype, value=typ,
                                    command=self.set_ftype_to_scan)
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
        self.complete_txt = ttk.Label(self.opt_run_frame, text='Complete!')
        
        
        # bottom_frame
        self.bottom_frame = ttk.Frame(self.master)
        self.about_btn = ttk.Button(self.bottom_frame, text='About',
                                    command=self.about_dlg)
        self.quit_btn = ttk.Button(self.bottom_frame, text='Exit',
                                    command=self.master.destroy)

    def arrange_widgets(self):
        """Organaze and show widgets."""
        
        btn_x = 20
        btn_y = 10

        self.dir_frame.pack(fill='x', padx=btn_x, pady=btn_y)
        self.choose_dir_btn.pack(side='left', padx=10, pady=2*btn_y)
        self.dir_lbl.pack(side='right', padx=10, pady=2*btn_y)

        self.file_frame.pack(fill='x', padx=btn_x, pady=btn_y)
        self.save_file_btn.pack(side='left', padx=10, pady=2*btn_y)
        self.file_lbl.pack(side='right', padx=10, pady=2*btn_y)

        
        self.options_frame.pack(fill='x', padx=btn_x, pady=2*btn_y)
        
        self.opt_chk_frame.pack(side='left')
        self.scan_subf_chk.pack(padx=btn_x, pady=btn_y, anchor='w')
        self.incl_dirs_chk.pack(padx=btn_x, pady=btn_y, anchor='w')
        self.ind_levels_chk.pack(padx=btn_x, pady=btn_y, anchor='w')

        self.sep1.pack(side='left', fill='y')
        self.opt_ftype_frame.pack(side='left')
        self.ftype_rbtns[0].pack(padx=btn_x+10, pady=(btn_y, 0), anchor='w')
        for rbtn in self.ftype_rbtns[1:-1]:
            rbtn.pack(padx=btn_x+10, anchor='w')
        self.ftype_rbtns[-1].pack(padx=btn_x+10, pady=(0, btn_y), anchor='w')
        
        self.sep2.pack(side='left', fill='y')
        self.opt_file_frame.pack(side='left')
        self.to_file_lbl.pack(padx=btn_x+10, pady=btn_y)
        self.txt_rbtn.pack(padx=btn_x+10, pady=btn_y, anchor='w')
        self.htm_rbtn.pack(padx=btn_x+10, pady=btn_y, anchor='w')

        self.sep3.pack(side='left', fill='y')
        self.opt_run_frame.pack(side='left')
        self.run_btn.pack(padx=4*btn_x, pady=(btn_y, 0))
        self.progressbar.pack()

        
        self.bottom_frame.pack(side='bottom', fill='x',
                                padx=btn_x, pady=btn_y)
        self.about_btn.pack(side='left', padx=btn_x, pady=btn_y)
        self.quit_btn.pack(side='right', padx=btn_x, pady=btn_y)
    
    def cut_lbl_text(self, text):
        """Cut the left side of text to make the right side visible."""
        if len(text) > LBL_TEXT_MAX:
            text = '... ' + text[-LBL_TEXT_MAX :]
        return text
    
    def set_defaults(self):
        """Set default values for widgets."""
        self.file_lbl_text.set(self.cut_lbl_text(str(self.file_path)))
        self.dir_lbl_text.set(self.cut_lbl_text(str(self.dir_path)))

        self.scan_subdirs.set(True)
        self.include_dir.set(True)
        self.indent_levels.set(True)
        self.ftype.set(ALL)
        self.to_file.set(TXT)
        self.htm_rbtn.config(state='disabled')
    
    def set_ftype_to_scan(self):
        """Set a pattern for scanning. When ftype is not All
        include_dir will be disabled due to input pattern of glob().
        """
        is_all_types = self.ftype.get() == ALL
        self.include_dir.set(is_all_types)
        incl_dirs_state = 'normal' if is_all_types else 'disabled'
        self.incl_dirs_chk.config(state=incl_dirs_state)
    
    def set_ext(self):
        """Update extension of file_path and its label."""
        self.file_path = self.file_path.with_suffix(self.to_file.get())
        self.file_lbl_text.set(str(self.file_path))
    
    def set_indentation(self):
        """Enable or disable indentation basing on subdirs var."""
        ind_levels_state = 'normal' if self.scan_subdirs.get() else 'disabled'
        self.ind_levels_chk.config(state=ind_levels_state)
    
    def open_dir_dlg(self):
        """Open dialog window for choosing a directory to scan."""

        dir_name = filedialog.askdirectory(initialdir=str(self.dir_path))
        if dir_name:
            self.dir_path = Path(dir_name)
            self.dir_lbl_text.set(self.cut_lbl_text(dir_name))

    def save_file_dlg(self):
        """Open dialog window to choose a path for saving."""

        fname = filedialog.asksaveasfilename(defaultextension=TXT,
                            filetypes=[('Text File', TXT), ('Web Page', HTM)],
                            initialdir=self.file_path.parent,
                            initialfile=self.file_path.stem)
        if fname:
            self.file_path = Path(fname)
            ext = self.file_path.suffix
            if ext in [TXT, HTM]:
                self.file_lbl_text.set(self.cut_lbl_text(fname))
                self.to_file.set(ext)
            else:
                self.file_path = self.file_path.with_suffix(TXT)
                self.file_lbl_text.set(self.cut_lbl_text(str(self.file_path)))
                self.to_file.set(TXT)
    
    def run_scan_dir(self):
        """Start new thread for showing animation of progressbar."""
        self.run_btn.state(['disabled'])
        if self.complete_txt.winfo_manager():
            self.complete_txt.pack_forget()
        Thread(target=self.scan_dir_thread, daemon=True).start()
    
    def scan_dir_thread(self):
        """Write scanning results of selected directory to a file."""
        num_items = 0
        for item in merged_glob(self.dir_path, self.scan_subdirs.get(),
                                                        self.ftype.get()):
            num_items += 1
        
        self.progressbar["maximum"] = num_items if num_items > 0 else 100
        self.progressbar.start()
        with open(str(self.file_path), 'w', encoding='utf-8') as fhand:
            found_items = scan_directory(self.dir_path,
                                        self.scan_subdirs.get(),
                                        self.include_dir.get(),
                                        self.indent_levels.get(),
                                        types=self.ftype.get())
            for item in found_items:
                print(item, sep='\n', file=fhand)
                self.progressbar.step()
        self.run_btn.state(['!disabled'])
        self.progressbar.stop()
        self.progressbar["value"] = self.progressbar["maximum"]
        self.complete_txt.pack()

    def about_dlg(self):
        """Open window with info about the application."""
        git_url = 'https://github.com/keen2/file-lister'
        msg = '{}\nversion: {}\n{}\n\n{} by {}'.format(DEF_FNAME,
                        __version__, git_url, __copyright__, __author__)
        messagebox.showinfo('About ' + DEF_FNAME, msg)


def main(argv):
    """Uses GUI or console to scan folders depending on arguments."""
    # Run GUI.
    if len(argv) == 1:
        root = tk.Tk()
        # Pass a toplevel widget as main window of the application.
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
    else:
        import argparse

        parser = argparse.ArgumentParser(
                    description='Print list of files of a given directory.')
        parser.add_argument('dirpath', help='Directory path to scan')
        parser.add_argument('-f', '--filepath',
                            help='File path to save scanning results')
        parser.add_argument('-s', '--subdirs', action='store_false',
                            help='Disable subdirectories scanning')
        parser.add_argument('-d', '--includedirs', action='store_false',
                            help='Disable of printing directory info')
        parser.add_argument('-i', '--indent', action='store_false',
                            help='Disable depth indentation')
        args = parser.parse_args()
        
        if Path(args.dirpath).is_dir():

            found_files = scan_directory(Path(args.dirpath), args.subdirs,
                                        args.includedirs, args.indent,
                                        console=True)
            # Print to a given file.
            # In Windows cmd:
            # powershell -command "iex \"tree d:\m /F\" > \"d:\t.txt\""
            if args.filepath:
                print('\nScanning...')
                file_path = Path(args.filepath).with_suffix(TXT)
                # open() for Python 3.4, 3.5:
                with open(str(file_path), 'w', encoding='utf-8') as fhand:
                    print(*found_files, sep='\n', file=fhand)
                print('\nData is written to: ' + file_path.name)
            # Print to console if no filepath entered.
            else:
                print(*found_files, sep='\n')
                # In Windows cmd: tree d:\movies /F
        else:
            print('\nThere is no directory with path:', args.dirpath)


if __name__ == "__main__":
    import sys

    main(sys.argv)


# TODO:
# .htm -> (tree) -> 1.2

# (D:\Programming\Study\Git)add instruction how to add and 
# add screen: ![#2](screenshots/example-2.png?raw=true)
# "Production"
