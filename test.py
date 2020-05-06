import pandas
import argparse

# Definisanje potrebnih argumenata i ucitavanje csv fajla

parser = argparse.ArgumentParser(description = 'Argumenti')
parser.add_argument ("-u", "-user", nargs="+", help = "Filter output by one or more space separated users", metavar='')
parser.add_argument ("-l", "-last", action='store_true', help = "Display last log for each user")

args = parser.parse_args()


df = pandas.read_csv("oldPDF.csv", 
	header = 0,
	names = ["Time", "SourceUser", "VPNGroup"])

# Filtriranje po userima

if args.u:
	df = (df[df.SourceUser.isin(args.u)])
	print(df.reset_index(drop=True))

# Filtriranje poslednjeg logovanja

elif args.l:
	df = df.drop_duplicates(subset=['SourceUser'], keep = 'last')
	print(df.reset_index(drop=True))

else: 
	print("Potrebno je definisati parametar -u ili -l.\n\nZa vise informacija, pogledajte --help")

