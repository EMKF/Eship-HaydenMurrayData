# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you

import pandas as pd
import numpy as np
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull from S3
df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Move/NETS2017_Move.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1')

# logic check
df['left'] = np.where(df['OriginState'] == df['DestState'], 'stayed', 'left')

# subset by move-outs
df = df[df['left'] == 'left'].reset_index()

# subset by active
df = df[df['Active'] == 'Yes'].reset_index()

# value_counts
move_in = df.groupby(['OriginState', 'MoveYear']).size().reset_index()
move_in.rename(columns={"OriginState": "region"}, inplace=True)
move_out = df.groupby(['DestState', 'MoveYear']).size().reset_index()
move_out.rename(columns={"DestState": "region"}, inplace=True)

# merge value_counts and rename columns
in_out = move_in.merge(move_out, on=['region', 'MoveYear'])

# rename
in_out.rename(columns={"0_x": "move_out", "0_y": "move_in" }, inplace=True)

# calculate ratio
in_out['ratio'] = in_out['move_in'] / in_out['move_out']

# check and export to excel
print(in_out)
# in_out.to_excel('/Users/hmurray/Desktop/data/NETS/in_out.xlsx', index=False)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/NETS/in_out.xlsx', engine='xlsxwriter')

# export each question to a different tab
def exporter(df, tab):
    df.to_excel(writer, sheet_name=tab, index=False)

exporter(move_in, 'move_in')
exporter(move_out, 'move_out')
exporter(in_out, 'in_out_ratio')

writer.save()
sys.exit()