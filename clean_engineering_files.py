import pandas as pd
import numpy as np

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
engineering['keywords'] = engineering['keywords'].replace(to_replace='EA', value='Environmental assessment', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='EAR', value='Environmental Analysis Report', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='EIS', value='Environmental Impact Statement', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='ENG', value='Engineering', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='ENV', value='Environmental', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='EQ', value='Earthquake', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='FF', value='Fossil Fuels', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='GEOCHEM', value='Geochemistry', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='GEOL', value='Geology', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='GEOPHYS', value='Geophysics', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='GEOTHERM', value='Geothermal', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='HYDRO', value='Hydrology', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='MIL', value='Military', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='MIN RES', value='Mineral Resources', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='NTS', value='Nevada Test Site', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='NWR', value='Nuclear Waste Repository', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='PRESS', value='Press clippings', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace='RR', value='Railroad', regex=True)
engineering['keywords'] = engineering['keywords'].replace(to_replace=';', value=",", regex=True)

# Change all caps to title case
engineering.authors = engineering.authors.str.title()
engineering.quad_name = engineering.quad_name.str.title()
engineering.comments = engineering.comments.str.title()

# Write to a csv without rownames
engineering.to_csv('G:\\datasets\\engineering\\engineering_01312020.csv', index=False)

# Convert to ResourceSpace format
rs_engineering = pd.DataFrame(list(zip(engineering.id, engineering.old_id, engineering.document,
                                       engineering.authors, engineering.quad_name, engineering.keywords,
                                       engineering.comments,
                                       np.repeat(2, len(engineering.index)), np.repeat(5, len(engineering.index)),
                                       np.repeat(0, len(engineering.index)))),
                              columns=['id', 'legacyid', 'title',
                                       'author', 'quadrangle', 'keywords',
                                       'comments',
                                       'resource_type', 'status', 'access'])

rs_engineering.to_csv('G:\\datasets\\engineering\\rs_engineering_test.csv', index=False)

