import argparse
import PyPDF2

def merge():
    parser=argparse.ArgumentParser(description='''Zip merge two or more PDF(s).''')
    parser.add_argument('pdf', nargs=2, help='PDF files')

    args=parser.parse_args()
    try:
        with open(args.pdf[0], 'rb') as pdf_1, open(args.pdf[1], 'rb') as pdf_2:
            in_file_1 = PyPDF2.PdfFileReader(pdf_1)
            in_file_2 = PyPDF2.PdfFileReader(pdf_2)
            out_file = PyPDF2.PdfFileWriter()
            for i in range(max(len(in_file_1.pages), len(in_file_2.pages))):
                if i < len(in_file_1.pages):
                    out_file.addPage(in_file_1.getPage(i))
                if i < len(in_file_2.pages):
                    out_file.addPage(in_file_2.getPage(i))
            with open('zip_merged.pdf', 'wb') as f: 
                out_file.write(f)
    except OSError:
        print("Could not read pdf")
    except PyPDF2.utils.PdfReadError:
        print("Could not read pdf")

if __name__ == "__main__":
    merge()
