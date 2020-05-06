import os
from PyPDF2 import PdfFileMerger, PdfFileWriter

#Ucitavanje pdf-ova iz foldera
path = "C:\\Users\\strahinja.soskic\\Desktop\\BackUP\\Programiranje\\Python\\CSV_python\\"
pdfs = []
# r=root, d=directories, p = pdfs
for r, d, p in os.walk(path):
    for pdf in p:
        if ('.pdf' and 'Report_VPNmodify') in pdf:
                pdfs.append(os.path.join(r, pdf))
for p in pdfs:
    print(p)

pdfs.sort(reverse=True)
montly_pdfs = pdfs[:2]


#Spajanje pdf-ova
merger = PdfFileMerger()

for pdf in montly_pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()



