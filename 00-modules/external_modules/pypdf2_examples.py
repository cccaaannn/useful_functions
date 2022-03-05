import PyPDF2
f = open('path_to_pdf.pdf','rb')

pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())


with open("pdf_text.txt", "w") as p:
    for i in pdf_text:
        p.write(i)
