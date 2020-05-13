import pandas
import argparse
import tabula
import os


# Definisanje potrebnih argumenata

parser = argparse.ArgumentParser(description = 'Argumenti')
parser.add_argument ("-u", "-user", nargs="+", help = "Filter output by one or more space separated users", metavar='')
parser.add_argument ("-l", "-last", action='store_true', help = "Display last log for each user")
parser.add_argument ("-i", required = True, help = "Import pdf or csv file", metavar='')
parser.add_argument ("-o", help = "Output to csv file", metavar='')

args = parser.parse_args()

users = None
if args.u:
	users = args.u

last_login = False
if args.l:
	last_login = True

if (not args.u and not args.l):
	print("\nPotrebno je definisati parametar -u ili -l.\n")
	parser.print_help()
	exit(0)

if args.o and ".csv" not in args.o:
	print ("Output file mora biti u csv formatu")
	exit(0)

# Ucitavanje csv fajla

file = args.i
tmp = "temp.csv"

if ".pdf" in args.i:
	tabula.convert_into(args.i, tmp, output_format="csv", pages='all')
	file = tmp

df = pandas.read_csv(file, 
	header = 0,
	names = ["Time", "SourceUser", "VPNGroup"])


# Filtriranje csv fajla

if users:
	df = (df[df.SourceUser.isin(users)])

if last_login:
	df = df.drop_duplicates(subset=['SourceUser'], keep = 'last')


# ispis u fajl ili na konzolu

if args.o:
	with open (args.o, 'w') as output_file:
		df.to_csv(output_file, index=False, line_terminator='\n')
else:
	print(df.reset_index(drop=True))


# Delete tmp ako postoji

if os.path.isfile(tmp):
	os.remove(tmp)
