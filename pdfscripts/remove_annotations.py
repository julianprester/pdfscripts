import argparse, PyPDF2, shutil

def run():
    parser=argparse.ArgumentParser(description='''Remove annotations from PDF(s).''')
    parser.add_argument('pdf', nargs='*', help='PDF files')

    args=parser.parse_args()
    for pdf in args.pdf:
        try:
            with open(pdf, 'rb') as pdf_obj:
                in_file = PyPDF2.PdfFileReader(pdf_obj)
                out_file = PyPDF2.PdfFileWriter()
                for page in in_file.pages:
                    out_file.addPage(page)
                    out_file.removeLinks()
                with open('temp.pdf', 'wb') as f: 
                    out_file.write(f)
            shutil.move('temp.pdf', pdf)
        except OSError:
            print("Could not read {}".format(pdf))
        except PyPDF2.utils.PdfReadError:
            print("Could not read {}".format(pdf))

if __name__ == "__main__":
    run()