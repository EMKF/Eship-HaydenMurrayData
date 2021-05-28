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
    # pull from local excel file
    df = pd.read_excel('/Users/hmurray/Desktop/data/presentation/data/bfs_presentation_explorer.xlsx')
    df = df[['region', 'time', 'BA_BA', 'BA_WBA']]
    return df

def plotter_1(df, query, title):
    df2 = df.query(query).reset_index()
    df2.plot(x='time', y=['BA_BA', 'BA_WBA'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.ylabel('Count')
    plt.ylim(0, 600000)
    # plt.yticks(np.arange(0, 1150, step=100), rotation=45)
    leg_1_labels = ['Business Applications', 'Business Applications with Planned Wages']
    plt.legend(labels=leg_1_labels)
    title = (title)
    plt.title("\n".join(wrap(title, 50)))
    plt.tight_layout()
    plt.grid()

    plt.savefig('/Users/hmurray/Desktop/data/presentation/plots/' + str(title) + '_monthly_apps.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = plotter_1(df, '20071201 <= time < 20090101', 'Great Recession')
    df = plotter_1(df, '20191201 <= time < 20210101', 'Covid-19')

sys.exit()