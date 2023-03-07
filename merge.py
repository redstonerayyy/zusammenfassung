from PyPDF2 import PdfMerger, PdfReader


def merge():
    merger = PdfMerger()

    merger.append(PdfReader(open("mnist_survey_accompanying_sheet.pdf", "rb")))
    merger.append(PdfReader(open("mnist_survey_sheet_filled.pdf", "rb")))

    merger.write("lehrer_document_survey.pdf")

if __name__ == "__main__":
    merge()