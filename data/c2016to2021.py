import csv
import pandas as pd

# the apportionment table
crosswalk_csv = 'cw20162021.csv'

# the csv with source tract data to apportioned
data_csv = 'clean2016.csv'

# the name of the field pertaining to the ctuid in data_csv
ctuidcol = "ctuid"

# names of columns we ewant ot apportion
fields = [
    ["pop2016","w_pop",None],
    ["pop2011","w_pop",None],
    ["dwe","w_dwe",None],
	["dwe_occ","w_dwe",None],
	["hhlds","w_dwe",None],
	["hhld_size","w_dwe","hhlds"],
	["avg_inc_ind","w_pop","pop2016"],
	["avg_inc_hhld","w_dwe","hhlds"],
	["lim_at","w_dwe","hhlds"],
	["lico_at","w_dwe","hhlds"],
]

# output file name
output_file_name = 'data_from_2016_into_2021_CTs.csv'

# read in the data
df = pd.read_csv(data_csv, dtype = {ctuidcol: str})

# read in crosswalk table
cw = pd.read_csv(crosswalk_csv, dtype = {"source_ctuid": str, "target_ctuid": str})

# joining the two input tables
merge_cw_df = cw.merge(df, how = "inner", left_on = "source_ctuid", right_on = ctuidcol)

# loop over each field, multiplying by the apportionment weight
output_fields = []
for f in fields:
	name = f[0]
	weight = f[1]
	mult = f[2]
	if f[2] is None:
		merge_cw_df[name + "_" + weight] = merge_cw_df[weight] * merge_cw_df[name]
		output_fields.append(name + "_" + weight)
	else:
		merge_cw_df[name + "_" + weight] = merge_cw_df[weight] * merge_cw_df[name] * merge_cw_df[mult]
		output_fields.append(name + "_" + weight)
	
# group by the target census tracts, summing by the wanted fields
output_data = merge_cw_df.groupby(["target_ctuid"]).sum()
output_data = output_data[output_fields]

for f in fields:
	name = f[0]
	weight = f[1]
	mult = f[2]
	if mult is not None:
		output_data[name + "_" + weight] = output_data[name + "_" + weight] / output_data[mult + "_" + weight]

print(output_data)

# write to file
output_data.to_csv(output_file_name)

