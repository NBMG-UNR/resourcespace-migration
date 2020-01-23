import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# read in both excel files into pandas dataframes
md_files = pd.read_excel('G:\\datasets\\mining_district\\mining_district_files_12202019.xlsx')
commodities = pd.read_excel('G:\\datasets\\mining_district\\nv_commodities.xlsx')

# take a look at unique values in the mining district files commodities list
comm_list = md_files.commodity.str.cat(sep="; ")
comm_list_arr = comm_list.split("; ")
comm_list_arr = np.unique(comm_list_arr, axis=0)

# identify values that are in the mining district file spreadsheet but NOT in the commodities master list

#first, change lists to sets and make them all lower case for comparison
lower_md_comm = {item.lower() for item in comm_list_arr}
lower_gen_comm = {item.lower() for item in commodities.name}

#find out what values are in the mining district files that do overlap with the commodities master list, and which ones don't
not_in = lower_md_comm.difference(lower_gen_comm)
intersection = lower_md_comm.intersection(lower_gen_comm)