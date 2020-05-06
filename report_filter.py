import pandas
import argparse

# Definisanje potrebnih argumenata

parser = argparse.ArgumentParser(description = 'Argumenti')
parser.add_argument ("-u", "-user", nargs="+", help = "Filter output by one or more space separated users", metavar='')
parser.add_argument ("-l", "-last", action='store_true', help = "Display last log for each user")

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

		#Za vise informacija, pogledajte --help")
	exit(0)

# Ucitavanje csv fajla

df = pandas.read_csv("oldPDF.csv", 
	header = 0,
	names = ["Time", "SourceUser", "VPNGroup"])

# Filtriranje csv fajla

if users:
	df = (df[df.SourceUser.isin(users)])

if last_login:
	df = df.drop_duplicates(subset=['SourceUser'], keep = 'last')

print(df.reset_index(drop=True))

	
	