from pypdf import PdfWriter
import os

class Merge:
    def __init__(self):
        self.merger = PdfWriter()
    def merge(self, files, dirname, output_file):
        for pdf in files:
            self.merger.append(pdf)
        pdfs = []
        for filename in os.listdir(dirname):
            if not filename.endswith(".pdf"):
                continue
            path = os.path.join(dirname, filename)
            if os.path.isdir(path):
                continue
            self.merger.append(path)
        with open(output_file, "wb") as output:
            self.merger.write(output)

                




 
        