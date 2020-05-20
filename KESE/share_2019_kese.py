# Rob Fairlie provided data files on

import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull raw data
age = pd.read_excel('/Users/hmurray/Desktop/data/KESE/share_total/RF_pull/entage9619.xlsx', sheet_name='Shares', skiprows=3)
imm = pd.read_excel('/Users/hmurray/Desktop/data/KESE/share_total/RF_pull/entimmigrant9619.xlsx', sheet_name='Shares', skiprows=3)
race = pd.read_excel('/Users/hmurray/Desktop/data/KESE/share_total/RF_pull/entrace9619.xlsx', sheet_name='Shares', skiprows=3)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/KESE/share_total/share_clean.xlsx', engine='xlsxwriter')

# subset, clean
def cleaner(df, cat, tab):
    df = df[cat]
    df = df.set_index('Time').transpose().drop(['Year'], axis=1)
    df = df.loc[:, df.columns.notnull()]
    print(' ')
    print(df)
    df.to_excel(writer, sheet_name=str(tab), index=True)
    return df

ages = ['Time', 'Ages 20-34', 'Ages 35-44', 'Ages 45-54', 'Ages 55-64']
imms = ['Time', 'Native-Born', 'Immigrant']
races = ['Time', 'White', 'Black', 'Latino', 'Asian']
age = cleaner(age, ages, 'age')
imm = cleaner(imm, imms, 'imm')
race = cleaner(race, races, 'race')
writer.close()