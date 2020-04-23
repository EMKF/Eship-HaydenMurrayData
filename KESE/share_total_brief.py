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



def racer(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/data/KESE/kese_change_share_demo.xlsx'
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
    # create new column that is % of total
    demo = ('White', 'Black', 'Latino', 'Asian')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['White', 'Black', 'Latino', 'Asian'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.merge(df, on='year')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
racer('rne', 'Total', "Share of New Entrepreneurs by Race and Ethnicity (1996-2019)")
racer('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Race and Ethnicity (1996-2019)")



def genderer(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='Male') | (df['demographic'] =='Female') | (df['demographic'] ==filt)].reset_index(drop=True)
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
    # create new column that is % of total
    demo = ('Male', 'Female')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['Male', 'Female'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
genderer('rne', 'Total', "Share of New Entrepreneurs by Gender (1996-2019)")
genderer('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Gender (1996-2019)")



def nativitier(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='Native-Born') | (df['demographic'] =='Immigrant') | (df['demographic'] ==filt)].reset_index(drop=True)
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
    # create new column that is % of total
    demo = ('Native-Born', 'Immigrant')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['Native-Born', 'Immigrant'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
nativitier('rne', 'Total', "Share of New Entrepreneurs by Nativity (1996-2019)")
nativitier('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Nativity (1996-2019)")



def ager(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/data/KESE/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='Ages 20-34') | (df['demographic'] =='Ages 35-44') | (df['demographic'] =='Ages 45-54') |\
                 (df['demographic'] =='Ages 55-64') | (df['demographic'] ==filt)].reset_index(drop=True)
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
    # create new column that is % of total
    demo = ('Ages 20-34', 'Ages 35-44', 'Ages 45-54', 'Ages 55-64')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['Ages 20-34', 'Ages 35-44', 'Ages 45-54', 'Ages 55-64'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
ager('rne', 'Total', "Share of New Entrepreneurs by Age (1996-2019)")
ager('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Age (1996-2019)")



def educator(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/data/KESE/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='Less than High School') | (df['demographic'] =='High School Graduate') | (df['demographic'] =='College Graduate') |\
                 (df['demographic'] =='Some College') | (df['demographic'] ==filt)].reset_index(drop=True)
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
    # create new column that is % of total
    demo = ('Less than High School', 'High School Graduate', 'Some College', 'College Graduate')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['Less than High School', 'High School Graduate', 'Some College', 'College Graduate'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
educator('rne', 'Total', "Share of New Entrepreneurs by Education (1996-2019)")
educator('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Education (1996-2019)")


def veteraner(sheet, filt, title):
    # define directory
    df = '/Users/hmurray/Desktop/KESE/KESE_2019_Update/hm_drafts/kese_change_share_demo.xlsx'
    # read in data
    df = pd.read_excel(df, sheet_name=sheet)
    # subset based on columns with counts
    df = df[df.columns[pd.Series(df.columns).str.startswith(('demo', 'n'))]]
    # filter for relevant demographics
    df = df[(df['demographic'] =='Veterans') | (df['demographic'] =='Non-Veterans') | (df['demographic'] ==filt)].reset_index(drop=True)
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
    # create new column that is % of total
    demo = ('Veterans', 'Non-Veterans')
    for x in demo:
        df[x] = (df[x]/df[filt])*100
    df.plot(x='year', y=['Veterans', 'Non-Veterans'])
    plt.title("\n".join(wrap(title, 35)))
    legend = plt.legend(title=None,
                        loc=6, fontsize='medium', fancybox=True)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/share_total/plots/separate/' + str(title) + '.png')
    df.to_excel('/Users/hmurray/Desktop/data/KESE/share_total/tables/individual/' + str(title) + '.xlsx', index=False)
veteraner('rne', 'Total', "Share of New Entrepreneurs by Veteran Status (1996-2019)")
veteraner('ose', '3YR MA', "Share of Opportunity Entrepreneurs by Veteran Status (1996-2019)")

# plt.show()