# data downloaded from https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html
# methods: https://www2.census.gov/programs-surveys/bds/updates/bds2019-release-note.pdf
# definitions: https://www.census.gov/programs-surveys/bds/documentation/methodology.html
# API documentation: https://api.census.gov/data/timeseries/bds/variables.html
# Possible metro/nonmetro population data? https://www.census.gov/data/datasets/time-series/demo/popest/2010s-total-metro-and-micro-statistical-areas.html
# Possible metro/nonmetro population data?https://www.census.gov/programs-surveys/metro-micro/about.html

import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

def data_create():
    return pd.read_csv('https://www2.census.gov/programs-surveys/bds/tables/time-series/bds2019_met.csv')

def filterer(df):
    df = df[['year', 'metro', 'estabs', 'estabs_entry', 'estabs_exit']]
    df = df[(df.metro == 'M') | (df.metro == 'N')].reset_index(drop=True)
    return df

def calculator(df):
    # change to integers
    df['estabs_entry'] = (df['estabs_entry']).astype(int)
    df['estabs_exit'] = (df['estabs_exit']).astype(int)
    # find totals and merge
    total = df.groupby(['year']).agg({'estabs':'sum', 'estabs_entry':'sum', 'estabs_exit':'sum'})
    total = total.add_prefix('total_').reset_index()
    data = pd.merge(df, total, on=['year'])
    # calculate trends
    data['per_births'] = (data['estabs_entry'] / data['total_estabs_entry'])
    data['per_exits'] = (data['estabs_exit'] / data['total_estabs_exit'])
    data['births_to_exits_ratio'] = (data['estabs_entry'] / data['estabs_exit'])
    data.to_excel('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2021/metro_nonmetro_table.xlsx')
    return data

def plotter(data):
    data['per_births'] = (data['per_births'] * 100)
    data['per_exits'] = (data['per_exits'] * 100)
    # birth = data.pivot_table(index=['year'], columns=['metro'], values='per_births').reset_index()
    # exit = data.pivot_table(index=['year'], columns=['metro'], values='per_exits').reset_index()
    # ratio = data.pivot_table(index=['year'], columns=['metro'], values='births_to_exits_ratio').reset_index()
    # estabs = data.pivot_table(index=['year'], columns=['metro'], values='estabs').reset_index()

    vars_list = ('estabs', 'estabs_entry', 'estabs_exit', 'per_births', 'per_exits', 'births_to_exits_ratio')
    for var in vars_list:
        temp_df = data.pivot_table(index=['year'], columns=['metro'], values=var).reset_index()
        temp_df.rename({'M': 'metro_' + str(var), 'N': 'nonmetro_' + str(var)}, axis=1, inplace=True)
        temp_df.plot(x='year', y=['metro_' + str(var), 'nonmetro_' + str(var)])
        leg_1_labels = ['Metro', 'Nonmetro']
        plt.legend(labels=leg_1_labels, loc='best', fontsize='small')
        title = (str(var) + ' in Metro and Nonmetro Areas')
        plt.title("\n".join(wrap(title, 40)))
        plt.xticks(rotation=0, wrap=True)
        plt.subplots_adjust(bottom=0.6)
        plt.ylabel('Percent')
        plt.xlabel('Year')
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2021/plots/' + str(var) + '_plot.png')
        temp_df.to_excel('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2021/tables/' + str(var) + '_table.xlsx')
        plt.show()
    return data

if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    data = calculator(df)
    print(data.head())
    data = plotter(data)
    # print(df.head())