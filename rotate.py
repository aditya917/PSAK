from pypdf import PdfReader, PdfWriter

class Rotate:
    def __init__(self, input_file):
        self.input_file = input_file
        self.reader = PdfReader(input_file)
        self.writer = PdfWriter()

    def rotate(self, num_pages, angle, output_file):
        for i in range(min(num_pages, len(self.reader.pages))): 
            self.writer.add_page(self.reader.pages[i])
            self.writer.pages[i].rotate(angle) 
        with open(output_file, "wb") as output:
            self.writer.write(output)


        

        
            
      

