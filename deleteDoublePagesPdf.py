from PyPDF2 import PdfFileReader, PdfFileWriter
from fuzzywuzzy import fuzz

def deletedoublepages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdf_path)
    # Rotate page 90 degrees to the right

    i = 0
    j = 1

    while True:
        try:
            page_1 = pdf_reader.getPage(i)
            page_2 = pdf_reader.getPage(i + j)
            
            text_1 = page_1.extractText()
            text_2 = page_2.extractText()
            print(i)         
            #print(text_1)
            print(i + j)
            #print(text_2)
            fuzzratio = fuzz.ratio(text_1.lower(), text_2.lower())
            print(fuzzratio)
            duplicate = False
            
            if fuzzratio > 80:
                duplicate = True

            print(duplicate)

            if not duplicate:
                pdf_writer.addPage(page_1)
                i = i + j
                j = 1

            if duplicate:
                j = j + 1
        except:
            break

    with open('noduplicates.pdf', 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    path = 'buch.pdf'
    deletedoublepages(path)

