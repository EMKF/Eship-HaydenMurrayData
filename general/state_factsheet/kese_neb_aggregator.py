# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# csv link: https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv
# pulling from Kauffman library

import sys
import pandas as pd
import kauffman
import matplotlib.pyplot as plt
import datetime
import numpy as np
from textwrap import wrap
from matplotlib.dates import date2num

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# read in ba and wba
def data_create():
    # pull from kauffman library
    kese = pd.read_csv('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/kese_download.csv')
    neb = pd.read_csv('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/neb_download.csv')
    kese = kese.loc[(kese['type'] == 'Total')]
    print(kese.head())
    print(neb.head())
    df = pd.merge(kese, neb, on=['name', 'year'], how='outer')
    print(df.head())
    df.to_excel('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/factsheet_data.xlsx')
    return df

def plotter_1(df):
    # filter for KS and US
    df2 = df.loc[(df['name'] == 'United States') | (df['name'] == 'Kansas')]
    df2 = df2.pivot_table(index=['year'], columns='name', values='rne').reset_index()
    print(df2)
    df2.plot(x='year', y=['Kansas', 'United States'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.xlim(1996, 2020)
    plt.ylabel('Rate of New Entrepreneurs')
    leg_1_labels = ['Kansas', 'United States']
    plt.legend(labels=leg_1_labels)
    title = ('The rate of new entrepreneurs in Kansas was at or above the national rate between 1998 and 2003. Since that time, the rate of new entrepreneurs in Kansas has been below the national rate.')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/plots/rne_ks_us.png')
    plt.show()
    return df

def plotter_2(df):
    # filter for KS and US
    df2 = df.loc[(df['name'] == 'United States') | (df['name'] == 'Kansas')]
    df2 = df2.pivot_table(index=['year'], columns='name', values='actualization').reset_index()
    print(df2)
    df2.plot(x='year', y=['Kansas', 'United States'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    # plt.xlim(2005, 2019)
    plt.ylabel('New Employer Business Actualization')
    leg_1_labels = ['Kansas', 'United States']
    plt.legend(labels=leg_1_labels)
    title = ('The share of new businesses that become employers within eight quarters has been higher in Kansas than in the entire United States every year every year since 2005.')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/plots/actualization_ks_us.png')
    plt.show()
    return df

def plotter_3(df):
    # filter for KS and US
    df2 = df.loc[(df['name'] == 'United States') | (df['name'] == 'Kansas')]
    df2 = df2.pivot_table(index=['year'], columns='name', values='sjc').reset_index()
    print(df2)
    df2.plot(kind='bar', x='year', y=['Kansas', 'United States'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    # plt.xlim(2005, 2019)
    plt.ylabel('Startup Job Creation')
    leg_1_labels = ['Kansas', 'United States']
    plt.legend(labels=leg_1_labels)
    title = ('Startups in Kansas created more jobs per 1,000 people compared to the national level between 1996 and 2005.\
 In recent years, this trend has reversed, with the jobs created by startups in Kansas falling below the national level.')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/plots/sjc_ks_us.png')
    plt.show()
    return df

def plotter_4(df):
    # filter for KS and US
    df2 = df.loc[(df['name'] == 'United States') | (df['name'] == 'Kansas')]
    df2 = df2.pivot_table(index=['year'], columns='name', values='ssr').reset_index()
    print(df2)
    df2.plot(kind='bar', x='year', y=['Kansas', 'United States'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    # plt.xlim(2005, 2019)
    plt.ylabel('Startup Survival Rate')
    leg_1_labels = ['Kansas', 'United States']
    plt.legend(labels=leg_1_labels)
    title = ('The share of businesses in Kansas that survived at least one year was higher than the national level between 1996 and 2003.\
 In recent years, the share of startups that survive at least one year has been lower in Kansas than at the national level.')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/general_content/state_factsheet/5.6.21/data/plots/ssr_ks_us.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = plotter_1(df)
    df = plotter_2(df)
    df = plotter_3(df)
    df = plotter_4(df)

sys.exit()