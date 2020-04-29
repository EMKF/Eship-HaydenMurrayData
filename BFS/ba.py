import sys
import pandas as pd
from kauffman_data import bfs, pep

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None


# get ba
ba = bfs.get_data(['BA_BA'], 'state', 2004, annualize=True)

# rename Period to year
ba.rename( columns={'Period':'year'}, inplace=True )
print(ba.head())

# get pep
pep = pep.get_data('state', 2005, 2018)
print(pep.head())

# merge ba and pep
adj_ba = pd.merge(ba, pep, on=['region', 'year'])

# calculate ba/population
adj_ba['ba_pop'] = (adj_ba['BA_BA']/adj_ba['population'])*100
print(adj_ba.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/BFS/BA/ba.xlsx', engine='xlsxwriter')

# export each df to sepeerate sheet
ba.to_excel(writer, sheet_name='state_BA', index=False)
adj_ba.to_excel(writer, sheet_name='adj_ba', index=False)

# save to excel
writer.save()

sys.exit()