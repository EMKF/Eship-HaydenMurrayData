# data download: https://www2.census.gov/programs-surveys/acs/data/pums/2018/5-Year/
# data dictionary: https://www.census.gov/programs-surveys/acs/technical-documentation/pums/documentation.html

import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import os
import time
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None

# time
start = time.time()

# writer
writer = pd.ExcelWriter('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_mink/mink_p90_p10.xlsx', engine='xlsxwriter')

def data_create():
    df = pd.DataFrame()
    for csv in os.listdir('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_mink/mink_raw_pulls'):
        print(csv)
        data = pd.read_csv('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_mink/mink_raw_pulls/' + str(csv), low_memory=False,\
                           usecols=['SERIALNO', 'ST', 'PINCP', 'PERNP', 'ADJINC', 'COW', 'ESR', 'SEMP'])
        df = df.append(data, sort=False)
        print(df.shape[0])
    return df

def data_manipulator(df):
    # convert columns to lowercase
    df.columns = map(str.lower, df.columns)
    # drop working without pay in fam business and unemployed from worker status
    df = df[df.cow != 8]
    df = df[df.cow != 9]
    # create new column to recode class of worker
    df['cow_recode'] = df['cow']
    df['cow_recode'].replace({2: 1, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2}, inplace=True)
    # recode to cow categories
    cow_cats = {
        1: 'Employee',
        2: 'Self_Employed'
    }
    # replace age number with string
    df["cow_recode"].replace(cow_cats, inplace=True)
    print(df[df.pernp < 0])
    return df

def unstacker(df):
    # create unique ID column and unstack cow
    df = df.reset_index()
    df["id"] = df.index + 1
    df = df.pivot_table(index=['id', 'st'], columns='cow_recode', values='pernp')
    return df

def calculator(df):
    #give df a name
    df.name = 'MINK'
    # subset for each state
    mo = df.query('st == 29')
    mo.name = 'Missouri'
    ia = df.query('st == 19')
    ia.name = 'Iowa'
    ne = df.query('st == 31')
    ne.name = 'Nebraska'
    ks = df.query('st == 20')
    ks.name = 'Kansas'
    frames = (df, mo, ia, ne, ks)
    for df in frames:
        print('')
        # employee mean and quantiles
        print(df.name + str('_Employee_mean'))
        print(df['Employee'].mean())
        test1 = (df['Employee'].quantile([.001, .1, .2, .3, .4, .5, .6, .7, .8, .9]))
        # self_employed mean and quantiles
        print(df.name + str('_Self_Employed_mean'))
        print(df['Self_Employed'].mean())
        test2 = (df['Self_Employed'].quantile([.001, .1, .2, .3, .4, .5, .6, .7, .8, .9]))
        # concat the quantiles for each df
        test = pd.concat([test1, test2], axis=1)
        test.rename(columns={"Employee": "Employee_" + str(df.name), "Self_Employed": "Self_Employed_" + str(df.name)}, inplace=True)
        print(test)
        # export each df quantiles to a tab in excel
        test.to_excel(writer, sheet_name=str(df.name), index=True)
        # plot one histogram for each cow
        df['Employee'].hist(bins=50, alpha=.4, align='mid', histtype='stepfilled', density=True)
        df['Self_Employed'].hist(bins=50, alpha=.4, align='mid', histtype='stepfilled', density=True)
        title = 'Histograms of Self_Employed (orange) and Employed (blue) Income in ' + str(df.name)
        plt.title("\n".join(wrap(title, 50)))
        plt.xlim(xmin=-10000, xmax=350000)
        plt.savefig('/Users/hmurray/Desktop/data/PUMS/p90_p10/csv_mink/hists/cow_his_' + str(df.name) + '.png')
        plt.show()
    return df


if __name__ == '__main__':
    df = data_create()
    df = data_manipulator(df)
    df = unstacker(df)
    df = calculator(df)
    # print('')
    # print(df.head())

writer.close()
end = time.time()
print((end/60) - (start/60))
sys.exit()