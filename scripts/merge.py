from PyPDF2 import PdfMerger, PdfReader
import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]
outfile = sys.argv[3]

def merge():
    merger = PdfMerger()

    merger.append(PdfReader(open(infile1, "rb")))
    merger.append(PdfReader(open(infile2, "rb")))

    merger.write(outfile)

if __name__ == "__main__":
    merge()