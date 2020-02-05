import pandas as pd
import numpy as np

geology = pd.read_excel('general_geology_01212020.xlsx')
geology = geology.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df=pd.DataFrame(geology)

#plug in new id numbers
for index, row in df.iterrows():
    value = "geo" + "%04d" % (index,)
    df.at[index, 'id'] = value

#rename new columns, column 'id' was automatically moved to front
df=df.rename(columns={'AREA':'index_location','TITLE':'title','DATE':'date','NOTES':'notes','UTMN_NAD27':'latitude','UTME_NAD27':'longitude','ITEM':'item','AUTHOR':'author','PAGES':'pages'})
