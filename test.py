from pypdf import PdfReader, PdfWriter

reader = PdfReader("output_25.pdf")
writer = PdfWriter()

def rotatePages(num_pages, angle):
    for i in range(num_pages+1):
        writer.add_page(reader.pages[i])
        writer.pages[i].rotate(angle)
    with open("output.pdf", "wb") as fp:
        writer.write(fp)


rotatePages(2, 90)