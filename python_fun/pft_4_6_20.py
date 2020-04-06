import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xlsxwriter
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# 1) Lambda Function Review: When to use it?
    # lambda is one line function
    # use cases:
    # 1. df.rename(whatever).pipe(lambda x: print(x))
    # 2. a_lst = [1, 2, 3]
    #       a_new_lst = map(lambda x: x + 1, a_lst)
    # 3. df['new_col'] = df['col'].apply(lambda x: x + 1)
# 2) How to add formatting to excel writer?
# 3) Corona brief - How to assist?


unemp = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/DC_Abnormality/python_edits/pop_unemp_pov_NCR/pop_unemp_pov_NCR.xlsx', sheet_name='Unemployment')

year_lst = range(2010, 2019)
unemp = unemp.rename(columns=dict(zip(year_lst, map(lambda x: str(x) + 'unemp', year_lst))))



# unemp.columns = [str(col) + 'Unemployment' for col in unemp.columns]
print(unemp.head())


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/4.6_fun_time.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
unemp.to_excel(writer, sheet_name='unemployment', index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['unemployment']

# Add some cell formats.
format1 = workbook.add_format(
    {"border": 1,
     "border_color": "#000000"})

# Hide all rows without data.
worksheet.set_default_row(hide_unused_rows=True)

# Set the column width and format.
worksheet.set_column('A:M', 18, format1)


# Close the Pandas Excel writer and output the Excel file.
writer.save()

sys.exit()
