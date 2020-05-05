import tabula
 
file = "C:\\Data\\Git\\wso-skripte\\Skritpta-za-Wiener\\Report_VPN.pdf"

tables = tabula.read_pdf(file, pages = "all")

# convert PDF into CSV file
tabula.convert_into(file, "oldPDF.csv", output_format="csv", pages='all')