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
ba = bfs.get_data(['BA_BA', 'BA_WBA'], 'state', 2004, annualize=True)

print(ba.head())
sys.exit()

# merge ba and pep
ba['percent_wba'] = ba['BA_WBA']/ba['BA_BA']
print(ba.head())

# Create a Pandas Excel writer using XlsxWriter as the engine.
loc = '/Users/hmurray/Desktop/Contractors/data_brief_contractors/data_brief_contractors/Jonathon_Galpern/spring_2020/factsheet/factsheet_data/bfs_applications.xlsx'
writer = pd.ExcelWriter(loc, engine='xlsxwriter')

# export each df to sepeerate sheet
ba.to_excel(writer, sheet_name='ba_wba', index=False)

# save to excel
writer.save()