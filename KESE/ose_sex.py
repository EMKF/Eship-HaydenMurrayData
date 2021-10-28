import pandas as pd
import os
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.dates as mdates
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    df = pd.read_csv('/Users/hmurray/Desktop/KESE/KESE_2020/data_files/kese_download.csv')
    return df

def filterer(df):
    df = df[(df.type == 'Sex').reset_index(drop=True)]
    return df

def pivoter(df):
    df = df.pivot_table(index=['year'], columns=['category'], values='ose').reset_index()
    return df

def bar_plotter(df):
    df_temp = df[(df.year == 2020).reset_index(drop=True)]
    df_temp.plot(x='year', y=['Men', 'Women'], kind="bar")
    leg_1_labels = ['Men', 'Women']
    plt.legend(labels=leg_1_labels, loc='best', fontsize='small')
    title = ('Opportunity Share Entrepreneurship by Sex in the United States in 2020')
    plt.title("\n".join(wrap(title, 40)))
    plt.xticks(rotation=0, wrap=True)
    plt.subplots_adjust(bottom=0.6)
    plt.ylabel('Opportunity Share Entrepreneurship')
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/ose_sex/plots/ose_sex_bar_plot.png')
    plt.show()
    return df

def plotter(df):
    # df_temp = df
    df.to_excel('/Users/hmurray/Desktop/data/KESE/ose_sex//ose_sex_table.xlsx', index=False)
    df['year'] = pd.to_datetime(df['year'], format='%Y')
    df.plot(x='year', y=['Men', 'Women'])
    # plt.xlim(1997, 2021)
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.ylabel('Opportunity Share Entrepreneurship')
    leg_1_labels = ['Men', 'Women']
    plt.legend(labels=leg_1_labels)
    title = ('Opportunity Share Entrepreneurship by Sex in the United States between 1998 and 2020')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/KESE/ose_sex/plots/ose_sex_plot.png')
    plt.show()
    return df


if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    df = pivoter(df)
    df = bar_plotter(df)
    df = plotter(df)
