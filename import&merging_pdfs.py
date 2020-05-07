import os
import tabula
import csv
from PyPDF2 import PdfFileMerger, PdfFileWriter

#Otvaranje text file-a u kojem se nalaze prethodno uneti pdf-ovi
array_checker = []
array_new = []
csv_read = open("output.csv", "r")
for line in csv_read:
    array_checker.append(line)
csv_read.close()
#print(array_checker)

#Ucitavanje pdf-ova iz foldera
path = "C:\\Users\\strahinja.soskic\\Desktop\\BackUP\\Programiranje\\Python\\CSV_python\\"
pdfs = []
# r=root, d=directories, p = pdfs
for r,d,p in os.walk(path):
    for pdf in p:
        if ('.pdf' and 'Report_Name_Montly' in pdf):
            if pdf not in array_checker:
                pdfs.append(os.path.join(r, pdf))
                array_new.append(os.path.join(r, pdf))

print(array_new)

#Ovaj me deo nesto zezao, nisam uspeo lepo da nadovezem csv file
#stoji "a" zbog append, ali i sa "w" mi nije radilo
#nekad ne upise nista, a nekad je mi izbaci gresku permission denied
#nisam ni stigao da se probam spojim pdf-ove#
with open("output.csv", "a",newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in array_checker:
        writer.writerow([i])
     
for p in pdfs:
    print(p)


#Spajanje pdf-ova
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)
    

merger.write("result.pdf")
merger.close()
