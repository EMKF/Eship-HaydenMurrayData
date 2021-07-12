# URL for BDS data: https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html

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
    # pull BDS firm age one way dataset
    df = pd.read_csv('http://www2.census.gov/programs-surveys/bds/tables/time-series/bds2018_fage.csv', usecols=['year', 'fage', 'firms', 'estabs'])
    return df

def data_manipulator(df):
    # remove first three characters of firm age column
    df['fage'] = df['fage'].str[3:]
    # subset df by latest year (or change to earlier years
    df = df[(df.year >= 2018)].reset_index(drop=True)
    # print unique values in firm age column
    print(df['fage'].unique())
    return df

def filterer(df):
    # drop 'left censored' value in firm age column and check to see if it worked
    df = df[(df.fage != 'Left Censored')].reset_index(drop=True)
    return df

def collapser(df):
    # replace 4 with 3 and 5 with 3
    df['fage'] = df['fage'].replace({'4': '3', '5': '3'})
    # replace 3 with 3-5
    df['fage'] = df['fage'].replace({'3': '3-5'})
    print(df)
    return df

def grouper_and_plotter(df, bus):
    # convert estabs and firms column to numeric so it can sum in the groupby below
    df[bus] = pd.to_numeric(df[bus])
    # groupby firm age and get counts of firms
    temp_df = df.groupby(['year', 'fage'])[bus].sum().apply(pd.to_numeric).reset_index()
    # plot establishment counts by firm age
    temp_df = temp_df.pivot_table(index='year', columns='fage', values=bus).reset_index()
    temp_df.plot(x='year', y=['0', '1', '2', '3-5', '6 to 10', '11 to 15', '16 to 20', '21 to 25', '26+'], kind='bar')
    plt.xlabel('time')
    plt.xticks(rotation=45)
    plt.ylabel('count of ' + str(bus))
    leg_1_labels = ['0', '1', '2', '3-5', '6 to 10', '11 to 15', '16 to 20', '21 to 25', '26+']
    plt.legend(labels=leg_1_labels)
    title = ('Distribution of ' + str(bus) + ' Across ' + str(bus) +  ' Age')
    plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/data/BDS/firm_estab_dist_by_age/plots/' + str(bus) + '_age_dist.png')
    plt.show()
    return df


if __name__ == '__main__':
    df = data_create()
    df = data_manipulator(df)
    df = filterer(df)
    df = collapser(df)
    variables = ['firms', 'estabs']
    for bus in variables:
        df = grouper_and_plotter(df, bus)

sys.exit()