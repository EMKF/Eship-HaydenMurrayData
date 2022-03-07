import sys
import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import kauffman.constants as c
from kauffman.data import acs, bfs, bds, pep, bed, qwi, shed

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 40000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def data_create():
    return pd.read_excel('/Users/hmurray/Desktop/data/BFS/industry/test_industry.xlsx')

def filterer(df):
    df = df[['industry', 'time', 'BF_DUR8Q']]
    df = df.pivot_table(index=['time'], columns=['industry'], values='BF_DUR8Q')
    return df

def plotter(df):
    # save for excel analysis
    df_save = df
    df_save = df.reset_index()
    df_save.to_excel('/Users/hmurray/Desktop/data/BFS/industry/plotter_test_industry.xlsx')
    # replace long column names with acronyms
    df.columns = (['.'.join(filter(str.isupper, name)) for name in df.columns])
    cols = df.columns
    # reset index for plotting
    df = df.reset_index()
    # plot
    df.plot(x='time', y=cols)
    plt.legend(labels=cols, fontsize='small', bbox_to_anchor=(1.05, 1.0), loc='upper left')
    title = ('Velocity by Industry in the US from 2005-2017')
    plt.title("\n".join(wrap(title, 40)))
    plt.xticks(rotation=0, wrap=True)
    # plt.subplots_adjust(bottom=0.6)
    plt.ylabel('DUR8Q')
    plt.xlabel('Year')
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/BFS/industry/dur8q_ind_plot.png')
    plt.show()

if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    df = plotter(df)

sys.exit()