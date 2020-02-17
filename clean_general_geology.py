import pandas as pd
import numpy as np

geology = pd.read_excel('general_geology_01212020.xlsx')
geology = geology.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df=pd.DataFrame(geology)

#create "id"column
for index, row in df.iterrows():
    value = "geo" + "%04d" % (index,)
    df.at[index, 'id'] = value
    
#rename columns
df=df.rename(columns={'AREA':'index_location','TITLE':'title','DATE':'date','NOTES':'notes','UTMN_NAD27':'latitude','UTME_NAD27':'longitude','ITEM':'item','AUTHOR':'author','PAGES':'pages'})

#remove "NUM" column
df = df.drop(["longitude"], axis=1)
df = df.drop(["latitude"], axis=1)
df = df.drop(["NUM"],axis=1)


#reorder columns to put 'id' first
cols = df.columns.tolist()
cols.insert(0, cols.pop(cols.index('id')))
df = df.reindex(columns= cols)

coordinates= pd.read_excel(r'/Users/LoganWeeks/Desktop/NBMG work stuff/Converted Coordinates.xlsx')

df1=pd.DataFrame(coordinates)

df1 = df1.drop(["UTME NAD27"], axis=1)
df1 = df1.drop(["UTMN NAD27"], axis=1)

final_spreadsheet = [df, df1]

#for some reason I have a syntax error at "sort= True"
final = (pd.concat(final_spreadsheet), sort= True)
