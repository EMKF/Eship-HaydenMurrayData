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
    # pull kese, subet
    kese = pd.read_csv('/Users/hmurray/Desktop/data/presentation/data/puller/kese_download.csv')
    kese = kese.loc[(kese['type'] == 'Total')]

    # pull neb
    neb = pd.read_csv('/Users/hmurray/Desktop/data/presentation/data/puller/neb_download.csv')

    # pull bfs, subset, rename, strip time
    bfs = kauffman.bfs(['BA_BA', 'BA_WBA'], 'us', annualize=True)
    bfs['percent_wba'] = bfs['BA_WBA'] / bfs['BA_BA']
    bfs.rename(columns={"region": "name", "time": "year"}, inplace=True)
    bfs = bfs[['name', 'year', 'BA_BA', 'BA_WBA', 'percent_wba']]
    # # pull locally for quicker runtime
    # bfs = pd.read_excel('/Users/hmurray/Desktop/data/presentation/data/puller/annual_bfs.xlsx')
    # bfs['year'] = bfs['time'].dt.year

    # merge kese and neb, subset
    data = pd.merge(kese, neb, on=['name', 'year'], how='outer')
    data = data[['name', 'year', 'sjc', 'ssr', 'velocity', 'actualization']]

    # merge kese+neb with bfs
    df = pd.merge(data, bfs, on=['name', 'year'], how='outer')
    df = df.loc[(df['name'] == 'United States')]
    df.rename(columns={"sjc": "Startup Job Creation", "ssr": "Startup Survival Rate", "actualization": "New Employer Business Actualization",\
                       "BA_BA": "Business Applications", "BA_WBA": "Business Applications with Planned Wages",\
                       "percent_wba": "Share of Business Applications with Planned Wages", "velocity": "New Employer Business Velocity"}, inplace=True)
    print(df)
    df.to_excel('/Users/hmurray/Desktop/data/presentation/data/pres_data.xlsx')
    return df

def plotter_1(df, key, value):
    # df2 = df.pivot_table(index=['year'], columns='name', values=key).reset_index()
    df2 = df[['name', 'year', key]]
    df2 = df2[df2[key].notna()]
    df2.plot(x='year', y=[key])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    ylabel = value
    plt.ylabel("\n".join(wrap(ylabel, 52)))
    ymin, ymax = plt.ylim()
    plt.ylim(ymin * .75, ymax * 1.2)
    # leg_1_labels = (str(key) + ' in the United States')
    # plt.legend(labels=leg_1_labels)
    # title = (str(key) + ' in the United States')
    # plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/' + str(key) + '.png')
    plt.show()
    return df

def plotter_2(df):
    df2 = df.pivot_table(index=['year'], columns='name', values=['Business Applications', 'Business Applications with Planned Wages']).reset_index()
    df2.plot(x='year', y=['Business Applications', 'Business Applications with Planned Wages'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    ylabel = 'Count of applications'
    plt.ylabel("\n".join(wrap(ylabel, 52)))
    ymin, ymax = plt.ylim()
    plt.ylim(ymin * .75, ymax * 1.2)
    leg_1_labels = ['Business Applications', 'Business Applications with Planned Wages']
    plt.legend(labels=leg_1_labels)
    # title = ('Business Applications and Business Applications with Planned Wages in the United States')
    # plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/ba_wba_combined.png')
    plt.show()
    return df

def plotter_3(df):
    df2 = df.pivot_table(index=['year'], columns='name', values=['Share of Business Applications with Planned Wages', 'New Employer Business Actualization']).reset_index()
    print(df2)
    df2.plot(x='year', y=['Share of Business Applications with Planned Wages', 'New Employer Business Actualization'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    ylabel = 'Share of Business Applications'
    plt.ylabel("\n".join(wrap(ylabel, 52)))
    ymin, ymax = plt.ylim()
    plt.ylim(ymin * .75, ymax * 1.2)
    leg_1_labels = ['Share of Business Applications with Planned Wages', 'New Employer Business Actualization']
    plt.legend(labels=leg_1_labels)
    # title = ('Share of Business Applications with Planned Wages vs Share of Business Applications that become Employers with Eight Quarters')
    # plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/wba_actualization.png')
    plt.show()
    return df



if __name__ == '__main__':
    df = data_create()
    # create dict of vars and labels to loop over and plot
    var_list = {
        'Business Applications with Planned Wages': 'Count of applications',
        'Share of Business Applications with Planned Wages': 'Percent',
        'New Employer Business Velocity': 'Quarters',
        'Startup Job Creation': 'Jobs per 1,000 people',
        'Startup Survival Rate': 'Percent',
    }
    for key, value in var_list.items():
        df = plotter_1(df, key, value)
    df = plotter_2(df)
    df = plotter_3(df)
sys.exit()