# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# csv link: https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv
# pulling from Kauffman library

import sys
import pandas as pd
from kauffman.data import bfs
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
    return pd.read_excel('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/industry_covid_intent_hire.xlsx')

def filterer(df):
    # filter for dates
    df = df[(df['time'] >= '2020-01-01') & (df['time'] <= '2021-11-01')]
    df = df[(df['industry'] != 'All NAICS Sectors')]
    print(df.head())
    return df

def plotter(df, var):
    # create pivot table
    df_temp = df.pivot_table(index=['time'], columns=['industry'], values=var)
    # replace long column names with acronyms
    df_temp.columns = (['.'.join(filter(str.isupper, name)) for name in df_temp.columns])
    # get list of column names
    cols = df_temp.columns
    # reset index for plotting
    df_temp = df_temp.reset_index()
    # plot
    df_temp.plot(x='time', y=cols)
    plt.legend(labels=cols, fontsize='small', bbox_to_anchor=(1.05, 1.0), loc='upper left')
    title = (str(var) + ' by Industry in the US from January 2020 to November 2021')
    plt.title("\n".join(wrap(title, 40)))
    plt.xticks(rotation=0, wrap=True)
    # plt.subplots_adjust(bottom=0.6)
    plt.ylabel('Business Applications for an EIN')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/plots/industry_plots/' + str(var) + '_ind_ba_covid.png')
    plt.show()
    return df

def bar_plotter(df, var):
    # create pivot table
    df_temp = df.pivot_table(index=['time'], columns=['industry'], values=var)
    print(df_temp)
    sys.exit()
    # replace long column names with acronyms
    df_temp.columns = (['.'.join(filter(str.isupper, name)) for name in df_temp.columns])
    # get list of column names
    cols = df_temp.columns
    # reset index for plotting
    df_temp = df_temp.reset_index()
    # plot
    df_temp.plot(x='time', y=cols)
    plt.legend(labels=cols, fontsize='small', bbox_to_anchor=(1.05, 1.0), loc='upper left')
    title = (str(var) + ' by Industry in the US from January 2020 to November 2021')
    plt.title("\n".join(wrap(title, 40)))
    plt.xticks(rotation=0, wrap=True)
    # plt.subplots_adjust(bottom=0.6)
    plt.ylabel('Business Applications for an EIN')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/plots/industry_plots/bar_plotter' + str(var) + '_ind_ba_covid.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    # df = plotter(df, 'BA_BA')
    # df = plotter(df, 'BA_CBA')
    # df = plotter(df, 'BA_WBA')
    df = bar_plotter(df, 'BA_BA')
    df = bar_plotter(df, 'BA_CBA')
    df = bar_plotter(df, 'BA_WBA')