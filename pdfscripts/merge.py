import argparse
import PyPDF2

def merge():
    parser=argparse.ArgumentParser(description='''Merge two or more PDF(s).''')
    parser.add_argument('pdfs', metavar='pdf1 pdf2 ...', nargs='+', help='PDF files to merge')

    args=parser.parse_args()
    try:
        out_file = PyPDF2.PdfFileWriter()
        in_files = [PyPDF2.PdfFileReader(open(pdf, 'rb')) for pdf in args.pdfs]
        for f in in_files:
            for i in range(len(f.pages)):
                out_file.addPage(f.getPage(i))
        with open('combined.pdf', 'wb') as f:
            out_file.write(f)
    except OSError:
        print("Could not read pdf")
    except PyPDF2.utils.PdfReadError:
        print("Could not read pdf")

if __name__ == "__main__":
    merge()