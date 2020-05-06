import os
import re
from PyPDF2 import PdfFileMerger, PdfFileWriter

#Ucitavanje pdf-ova iz foldera
path = "C:\\Users\\strahinja.soskic\\Desktop\\BackUP\\Programiranje\\Python\\CSV_python\\"
pdfs = []
# r=root, d=directories, p = pdfs
for r, d, p in os.walk(path):
    for pdf in p:
        if ('.pdf' and 'Report_VPNmodify') in pdf:
            if re.search('2020_.._06', pdf):
                pdfs.append(os.path.join(r, pdf))
for p in pdfs:
    print(p)




#Spajanje pdf-ova
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()



