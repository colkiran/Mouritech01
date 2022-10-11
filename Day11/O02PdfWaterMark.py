
import PyPDF2

def insert_watermark(wmfile, pageObj):
    PDFR = open("data.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(PDFR)

    pageObj.mergePage(pdfReader.getPage(0))
    PDFR.close()
    return pageObj

def main():
    wtrmrkFile = "WaterMark.pdf"

    srcFile = "data.pdf"

    nwFile = "WaterMrkEx.pdf"

    PDFR1 = open(srcFile, "rb")

    pdfReader = PyPDF2.PdfFileReader(PDFR1)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader.numPages):
        wmpageobj = insert_watermark(wtrmrkFile, pdfReader.getPage(page))

        pdfWriter.addPage(wmpageobj)

        PDFR2 = open("C:\\Training\\PycharmProjects\\Mouritech01\\Day11\\WaterMrkEx.pdf", "wb")
        pdfWriter.write(nwFile)

        PDFR1.close()
        PDFR2.close()

if __name__ == '__main__':
    main()

