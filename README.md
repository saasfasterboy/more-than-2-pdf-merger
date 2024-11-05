PDF Merger
Overview
This project provides a simple Python script to merge multiple PDF files into a single PDF document using the PyPDF2 library. It allows users to combine multiple PDFs easily by specifying their filenames.

Features
Merge multiple PDF files into one.
Simple and easy-to-use implementation.
Supports any number of PDF files.
Requirements
Python 3.x
PyPDF2 library
Installation
You can install the required library using pip:

pip install PyPDF2
Code Implementation
The following code demonstrates how to merge multiple PDFs:

import PyPDF2

pdf = ['1.pdf', '2.pdf', '3.pdf']  # You can add many PDFs with their correct names
merger = PyPDF2.PdfMerger()

for file in pdf:
    with open(file, 'rb') as a:
        pdfread = PyPDF2.PdfReader(a)
        merger.append(pdfread)

merger.write('merged.pdf')
How to Use
Add the PDF files you want to merge to the list in the pdf variable.
Run the script.
The merged PDF will be saved as merged.pdf in the same directory.
Example
To merge PDF files named 1.pdf, 2.pdf, and 3.pdf, simply add their names to the pdf list:

python
Copy code
pdf = ['1.pdf', '2.pdf', '3.pdf']
Run the script, and a new file named merged.pdf will be created containing the combined content of the specified PDFs.
