import os
import pandas as pd

path = "C:\\Users\\eodean\\OneDrive - University of Nevada, Reno\\Documents\\projects\\oil_gas\\OIL01162020.xls"

inweb = os.listdir("U:\\public\\OilGas\\Logs")
oil = pd.read_excel(path)
apis = oil['-API'].tolist()

df = pd.DataFrame(inweb)

inwebnotinspreadsheet = set(inweb) - set(apis) # correct elements, but not yet in sorted order
print(sorted(inwebnotinspreadsheet))


inspreadsheetnotinweb = set(apis) - set(inweb)
print(sorted(inspreadsheetnotinweb))



df.to_excel(r'C:\\Users\\eodean\\OneDrive - University of Nevada, Reno\\Documents\\projects\\oil_gas\\oilinweb.xlsx')