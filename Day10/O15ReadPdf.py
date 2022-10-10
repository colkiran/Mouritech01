
import PyPDF2

PDFR = open("data.pdf",  "rb")

pdfReader = PyPDF2.PdfFileReader(PDFR)

print("Page Count :", pdfReader.numPages)

for cntr in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(cntr)
    print(pageObj.extractText())

PDFR.close()
