
import PyPDF2

PDFR = open("data.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(PDFR)

print(pdfReader.isEncrypted)
# pdfReader.decrypt("")

for page in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(page)
    print(pageObj.extractText())

PDFR.close()
