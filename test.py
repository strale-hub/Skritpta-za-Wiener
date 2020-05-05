import pandas
import argparse

parser = argparse.ArgumentParser(description = 'Argumenti')
parser.add_argument ("-u", help = "This is a filtered user")


df = pandas.read_csv("oldPDF.csv", 
	header = 0,
	names = ["Time", "SourceUser", "VPNGroup"])

#user = input("unesi usera:\n")

args = parser.parse_args()
user = args.u

print(df[df.SourceUser.eq(user)])

#df = df.drop_duplicates(subset=['SourceUser'], keep = 'last')
#print(df.reset_index(drop=True))