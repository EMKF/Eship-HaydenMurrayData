# data obtained manually from Rob Fairlie on 3.27.20 @ 12:29pm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def sharer(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='White') | (df['demographic'] =='Black') | (df['demographic'] =='Asian') |\
                 (df['demographic'] =='Latino') | (df['demographic'] ==filt)].reset_index(drop=True)
    # transpose
    df = df.transpose().reset_index(drop=False)
    # set new column headers as first row
    df.columns = df.iloc[0]
    # drop old first row
    df.drop(df.index[0], inplace=True)
    # reset index
    df.reindex()
    # trim the year strings
    df['demographic'] = df['demographic'].str.replace("n_","")
    # rename year column
    df.rename(columns={"demographic": "year"},inplace=True)
    print(df)
    # create new column that is % of total
    demo = ('White', 'Black', 'Latino', 'Asian')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['White', 'Black', 'Latino', 'Asian'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/' + str(title) + '.xlsx', index=False)


sharer('rne', 'Total', "Share of New Entrepreneurs by Race and Ethnicity (1996-2019)")
sharer('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Race and Ethnicity (1996-2019)")





# # old calculation
# fig_4 = fig_4[['demographic', 'n_1996', 'n_2019']]
# fig_4.set_index('demographic', inplace=True)
# fig_4 = fig_4.transpose().reset_index(drop=True)
# columns = list(fig_4.columns.values)
# for column_1 in columns:
#     for column_2 in columns:
#         new_column = '-'.join([column_1,column_2])
#         fig_4[new_column] = fig_4[column_1] / fig_4[column_2]
# fig_4 = fig_4[['White-Total', 'Black-Total', 'Latino-Total', 'Asian-Total']]
# fig_4 = fig_4.transpose().reset_index(drop=False)
# fig_4.rename(columns={0: "1996", 1: "2019"},inplace=True)
# fig_4['demographic'] = fig_4['demographic'].str.replace("-Total","")
# print(fig_4)
# fig_4.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/share_race_change.xlsx', index=False)





