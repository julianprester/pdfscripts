import argparse
import PyPDF2

def delete():
    parser=argparse.ArgumentParser(description='''Delete extra pages in a PDF.''')
    parser.add_argument('pdf', nargs=1, help='PDF file')
    parser.add_argument('--pages', nargs='*', type=int, help='Page numbers to delete')

    args=parser.parse_args()
    try:
        with open(args.pdf[0], 'rb') as pdf:
            in_file = PyPDF2.PdfFileReader(pdf)
            out_file = PyPDF2.PdfFileWriter()
            for index, _ in enumerate(in_file.pages):
                if(index not in args.pages):
                    out_file.addPage(in_file.getPage(index))
            with open('out.pdf', 'wb') as f: 
                out_file.write(f)
    except OSError:
        print("Could not read pdf")
    except PyPDF2.utils.PdfReadError:
        print("Could not read pdf")

if __name__ == "__main__":
    delete()
