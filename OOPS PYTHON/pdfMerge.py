from PyPDF2 import PdfWriter
import os

merger=PdfWriter()

files=[file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
    print(pdf)

merger.write("Merge.pdf")
merger.close()