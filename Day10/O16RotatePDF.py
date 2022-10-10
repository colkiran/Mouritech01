
import PyPDF2

def pdfRotate(oldflname, newflname, rotation):

    PDFR = open(oldflname, "rb")

    pdfReader = PyPDF2.PdfFileReader(PDFR)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader.numPages):

        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotation)

        pdfWriter.addPage(pageObj)

    PDFW = open(newflname, "wb")

    pdfWriter.write(PDFW)

    PDFR.close()
    PDFW.close()

def main():

    oldflname = "data.pdf"

    newflname = "rotated_data.pdf"

    rotation = 270

    pdfRotate(oldflname, newflname, rotation)

if __name__ == '__main__':
    main()

