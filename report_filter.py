import pandas
import argparse

# Definisanje potrebnih argumenata

parser = argparse.ArgumentParser(description = 'Argumenti')
parser.add_argument ("-u", "-user", nargs="+", help = "Filter output by one or more space separated users", metavar='')
parser.add_argument ("-l", "-last", action='store_true', help = "Display last log for each user")
parser.add_argument ("-i", required = True, help = "Import csv file", metavar='')
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

# Ucitavanje csv fajla

df = pandas.read_csv(args.i, 
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
		#output_file.write("%s\n" % df)
		df = df.reset_index(drop=True)
		df.to_csv(output_file, index=False, line_terminator='\n')
else:
	print(df.reset_index(drop=True))
	