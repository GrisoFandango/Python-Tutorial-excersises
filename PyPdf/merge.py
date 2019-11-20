import PyPDF2

merger = PyPDF2.PdfFileMerger()
file_names = ["first.pdf", "second.pdf"]
for file_names in file_names:
    merger.append(file_names)
merger.write("combined.pdf")
