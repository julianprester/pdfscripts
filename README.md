pdfscripts
==========

- **Copyright (c)** 2020 Julian Prester
- **License:** MIT
- **Description:** Small set of Python scripts for PDF library interaction and manipulation

## Features
- Open PDF(s)
- Remove annotations from PDF(s)
- Extract a subset of PDF(s) from a library

## Usage
pdfscripts consists of a set of scripts that can be called via the command line. Some of the scripts rely on a library folder that contains PDF documents that are uniquely identifiable via a Bibtex key. The description for each script is listed below.

### open_pdf

```
usage: open_pdf.py [-h] [-l LIBRARY] [pdf [pdf ...]]

Open PDF(s) from library folder using Bibtex citation keys.

positional arguments:
  pdf                   PDF files

optional arguments:
  -h, --help            show this help message and exit
  -l LIBRARY, --library LIBRARY
                        Library folder
```

### remove_annotations

```
usage: remove_annotations.py [-h] [pdf [pdf ...]]

Remove annotations from PDF(s).

positional arguments:
  pdf         PDF files

optional arguments:
  -h, --help  show this help message and exit
```

### extract_subset

```
usage: extract_subset.py [-h] [-l LIBRARY] [-o OUT] csv

Extract PDF(s) from a folder or library based on a set of Bibtex citation keys from a csv file.

positional arguments:
  csv                   Input csv file

optional arguments:
  -h, --help            show this help message and exit
  -l LIBRARY, --library LIBRARY
                        Library folder
  -o OUT, --out OUT     Export output folder
```
