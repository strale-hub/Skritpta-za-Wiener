import tabula
 
file = "C:\\Data\\Git\\wso-skripte\\Skritpta-za-Wiener\\result.pdf"

tables = tabula.read_pdf(file, pages = "all")

# convert PDF into CSV file
tabula.convert_into(file, "mergedPDF.csv", output_format="csv", pages='all')