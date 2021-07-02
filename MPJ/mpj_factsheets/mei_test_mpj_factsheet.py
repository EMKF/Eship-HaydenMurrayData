import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # import MPJ download file
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/factsheets/factsheet_mpj_download.csv')
    return df

def filterer(df):
    # # FILTER OPTION #1: QUERY the fips column for KS (20)
    # df = df.query('fips == 20').reset_index(drop=True)
    # FILTER OPTION #2: FILTER THE fips column for Kansas and United States
    #df = df[(df.name == 'Kansas') | (df.name == 'United States')].reset_index(drop=True)
    df = df[(df.name == 'Kansas')].reset_index(drop=True)
    # filter the category column for businesses age 0-1
    #df = df[df['category'] == 'Ages 0 to 1'].reset_index(drop=True)
    df = df[df['category'] != 'Total'].reset_index(drop=True)
    return df

def harry_plotter(df, x):
    # plot KS and US contribution/compensation/constance/creation aka 'x' over time
    contribution = df.pivot_table(index='year', columns='category', values=x).reset_index()
    contribution.plot(x='year', y=['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+'])
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.xlim(2004, 2020)
    plt.ylabel(x)
    leg_1_labels = ['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+']
    plt.legend(labels=leg_1_labels)
    title = (str(x) + ' for each business age category between 2004 and 2020')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/factsheets/plots/ages_KS' + str(x) + '.png')
    plt.show()
    return df

#loop to do this for every indicator x out of contribution, compensation, constancy, and creation
if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    print(df.head(25))
    variables = ['contribution', 'compensation', 'constancy', 'creation']
    for x in variables:
        df = harry_plotter(df, x)