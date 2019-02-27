# FileLister

Scans for files and subfolders in a directory and writes to
file a list of data structured by hierarchy.

<p align="center">
  <img src="./images/app80_lossy.png" alt="FileLister">
</p>
<br></br>
<p><b>Txt:</b>
  <img src="./images/out_txt.png" alt="Resulting .txt" width="449" height="225" align="middle">
  <b>Html:</b>
  <img src="./images/out_htm.png" alt="Resulting .html" width="280" height="320" align="middle">
</p>


## Usage

GUI version if no arguments given, console otherwise:
```
file-lister.py [-h] [-f FILEPATH] [-s] [-d] [-i] dirpath

Print list of files of a given directory.

positional arguments:
  dirpath               Directory path to scan

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        File path to save scanning results
  -s, --subdirs         Disable subdirectories scanning
  -d, --includedirs     Disable of printing directory info
  -i, --indent          Disable depth indentation
```

## Authors

**Andrei Ermishin**

## License

![GitHub](https://img.shields.io/github/license/keen2/file-lister.svg)

See [LICENSE](LICENSE) for more information.

Copyright 2019 © Andrei Ermishin
