import pandas as pd

engineering = pd.read_excel('G:\\datasets\\engineering\\engineering_1220219.xlsx')
engineering = engineering.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Create one column for the historic ID value
engineering["old_id"] = engineering.file.str.cat(engineering.item, sep="_")

# Drop the old columns
engineering = engineering.drop(["file", "item"], axis=1)

# Create a column with a new id
for index, row in engineering.iterrows():
    value = "eng" + "%04d" % (index,)
    engineering.at[index, 'id'] = value

# Parse out and replace keyword abbreviations with actual keywords
engineering.replace(to_replace='EA', value='Environmental assessment', regex=True, inplace=True)
engineering.replace(to_replace='EAR', value='Environmental Analysis Report', regex=True, inplace=True)
engineering.replace(to_replace='EIS', value='Environmental Impact Statement', regex=True, inplace=True)
engineering.replace(to_replace='ENG', value='Engineering', regex=True, inplace=True)
engineering.replace(to_replace='ENV', value='Environmental', regex=True, inplace=True)
engineering.replace(to_replace='EQ', value='Earthquake', regex=True, inplace=True)
engineering.replace(to_replace='FF', value='Fossil Fuels', regex=True, inplace=True)
engineering.replace(to_replace='GEOCHEM', value='Geochemistry', regex=True, inplace=True)
engineering.replace(to_replace='GEOL', value='Geology', regex=True, inplace=True)
engineering.replace(to_replace='GEOPHYS', value='Geophysics', regex=True, inplace=True)
engineering.replace(to_replace='GEOTHERM', value='Geothermal', regex=True, inplace=True)
engineering.replace(to_replace='HYDRO', value='Hydrology', regex=True, inplace=True)
engineering.replace(to_replace='MIL', value='Military', regex=True, inplace=True)
engineering.replace(to_replace='MIN RES', value='Mineral Resources', regex=True, inplace=True)
engineering.replace(to_replace='NTS', value='Nevada Test Site', regex=True, inplace=True)
engineering.replace(to_replace='NWR', value='Nuclear Waste Repository', regex=True, inplace=True)
engineering.replace(to_replace='PRESS', value='Press clippings', regex=True, inplace=True)
engineering.replace(to_replace='RR', value='Railroad', regex=True, inplace=True)
engineering.replace(to_replace=';', value=",", regex=True, inplace=True)

# Change all caps to title case
engineering.authors = engineering.authors.str.title()
engineering.quad_name = engineering.quad_name.str.title()
engineering.comments = engineering.comments.str.title()

# Write to a csv without rownames
engineering.to_csv('G:\\datasets\\engineering\\engineering_01312020.csv', index=False)

