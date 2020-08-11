import os, argparse, csv, shutil

# Change library path
library = 'PATH/TO/LIBRARY/'

def run():
	parser=argparse.ArgumentParser(description='''Extract PDF(s) from a folder or library based on a set of Bibtex citation keys from a csv file.''')
	parser.add_argument('csv', help='Input csv file')
	parser.add_argument('-l', '--library', help='Library folder', type=str, default=library)
	parser.add_argument('-o', '--out', help='Export output folder', type=str, default='out')

	args=parser.parse_args()
	if os.path.isfile(args.csv):
		with open(args.csv, newline='') as csvfile:
			if not os.path.exists(args.out):
				os.makedirs(args.out)
			reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
			count = 0
			for row in reader:
				try:
					shutil.copy(args.library + row[0] + '.pdf', args.out)
					count += 1
				except FileNotFoundError:
					print("{}.pdf does not exist".format(row[0]))
		print("{} pdfs copied to {}".format(count, args.out))

if __name__ == "__main__":
	run()