# data downloaded from csv link at the bottom of this webpage: https://www.census.gov/econ/bfs/data.html
# csv link: https://www.census.gov/econ/bfs/csv/bfs_quarterly.csv
# pulling from Kauffman library

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
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
    df = df[(df['time'] >= '2019-01-01') & (df['time'] < '2021-01-01')]
    # create year and month column
    df['year'] = pd.DatetimeIndex(df['time']).year
    df['month'] = pd.DatetimeIndex(df['time']).month
    df['year_month'] = df['time'].dt.strftime('%Y-%m')
    return df

def bar_plotter(df, var):
    # filter out all NAICS sectors category
    df_temp = df[(df['industry'] == 'All NAICS Sectors')]
    # subset df for columns of interest
    df_temp = df_temp[['month', 'year', var]]
    # create pivot table
    df_temp = df_temp.pivot_table(index=['month'], columns=['year'], values=var)
    # reset index for plotting
    df_temp = df_temp.reset_index()
    # plot
    df_temp.plot(x='month', y=[2019, 2020], kind="bar")
    # set legend
    # plt.legend(fontsize='small', bbox_to_anchor=(1.05, 1.0), loc='upper left')
    title = (str(var) + ' in the US: 2019 vs 2020')
    plt.title("\n".join(wrap(title, 40)))
    plt.xticks(rotation=0, wrap=True)
    plt.ylabel('Business Applications for an EIN')
    plt.xlabel('Month')
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/plots/industry_plots/bar_plotter_' + str(var) + '_ba_covid.png')
    plt.show()
    return df

def ind_table(df, var):
    # filter out all NAICS sectors category
    df_temp = df[(df['industry'] != 'All NAICS Sectors')]
    # subset df for columns of interest
    df_temp = df_temp[['month', 'year', 'industry', var]]
    # create pivot table
    df_temp = df_temp.pivot_table(index=['industry'], columns=['month', 'year'], values=var)
    # reset index for plotting
    df_temp = df_temp.reset_index()
    print(df_temp)
    df_temp.to_excel('/Users/hmurray/Desktop/data/BFS/ba_wba_4bf_8bf/2021/updated_data/19_20_table_' + str(var) + '_covid.xlsx')
    return df


if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    df = bar_plotter(df, 'BA_BA')
    df = ind_table(df, 'BA_BA')