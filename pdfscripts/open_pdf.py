import os, argparse

# Change library path
library = 'PATH/TO/LIBRARY/{}.pdf'

def run():
	parser=argparse.ArgumentParser(description='''Open PDF(s) from library folder using Bibtex citation keys.''')
	parser.add_argument('pdf', nargs='*', help='PDF files')
	parser.add_argument('-l', '--library', help='Library folder', type=str, default=library)

	args=parser.parse_args()
	for pdf in args.pdf:
		try:
			os.startfile(library.format(pdf))
		except FileNotFoundError:
			print("{}.pdf does not exist".format(pdf))

if __name__ == "__main__":
	run()