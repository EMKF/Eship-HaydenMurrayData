# data downloaded from https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html
# methods: https://www2.census.gov/programs-surveys/bds/updates/bds2019-release-note.pdf
# definitions: https://www.census.gov/programs-surveys/bds/documentation/methodology.html
# API documentation: https://api.census.gov/data/timeseries/bds/variables.html
# Possible metro/nonmetro population data? https://www.census.gov/data/datasets/time-series/demo/popest/2010s-total-metro-and-micro-statistical-areas.html
# Possible metro/nonmetro population data?https://www.census.gov/programs-surveys/metro-micro/about.html

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

def data_create():
    # read in BDS, filter, subset columns
    bds = pd.read_csv('https://www2.census.gov/programs-surveys/bds/tables/time-series/bds2019_met.csv')
    bds = bds[['year', 'metro', 'estabs', 'estabs_entry', 'estabs_exit']]
    bds = bds[(bds.metro == 'M') | (bds.metro == 'N')].reset_index(drop=True)
    # read in pop estimates, filter, lowercase
    pop = pd.read_excel('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/pep_est/ME_KFN_PopulationEstimates_MetroNonMetro_19702019_vShare.xlsx',
                        sheet_name='Summary_Metro_vs_NonMetroPop',
                        skiprows=7,
                        usecols=('B:D'))
    pop.columns = pop.columns.str.lower()
    pop = pop[(pop.year >= 1978)].reset_index(drop=True)
    # merge on year and metro
    df = bds.merge(pop, on=['year', 'metro'])
    return df

def calculator(df):
    # change to integers
    df['estabs_entry'] = (df['estabs_entry']).astype(int)
    df['estabs_exit'] = (df['estabs_exit']).astype(int)
    # find totals and merge
    total = df.groupby(['year']).agg({'estabs':'sum', 'estabs_entry':'sum', 'estabs_exit':'sum', 'pop_estimates': 'sum'})
    total = total.add_prefix('total_').reset_index()
    data = pd.merge(df, total, on=['year'])
    # create pop adjustment
    data['estabs_pop'] = data['estabs'] / data['pop_estimates']
    data['estabs_entry_pop'] = data['estabs_entry'] / data['pop_estimates']
    data['estabs_exit_pop'] = data['estabs_exit'] / data['pop_estimates']
    # calculate trends
    data['per_births'] = (data['estabs_entry'] / data['total_estabs_entry'])
    data['per_exits'] = (data['estabs_exit'] / data['total_estabs_exit'])
    data['births_to_exits_ratio'] = (data['estabs_entry'] / data['estabs_exit'])
    data.to_excel('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/metro_nonmetro_table.xlsx')
    return data

def plotter(data):
    data['per_births'] = (data['per_births'] * 100)
    data['per_exits'] = (data['per_exits'] * 100)
    data['estabs_pop'] = (data['estabs_pop'] * 100)
    data['estabs_entry_pop'] = (data['estabs_entry_pop'] * 100)
    data['estabs_exit_pop'] = (data['estabs_exit_pop'] * 100)
    data['test'] = (data['estabs_entry'] / data['pop_estimates']) / (data['total_estabs_entry'] / data['total_pop_estimates'])
    data['per_pop'] = (data['pop_estimates'] / data['total_pop_estimates'])
    metro = data[(data.metro == 'M')].reset_index(drop=True)
    nonmetro = data[(data.metro == 'N')].reset_index(drop=True)
    print(data.head())
    # create subplot 1
    f, a = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    metro.reset_index().pivot('year', 'metro', 'estabs_entry').plot(ax=a[0, 0], title='Metro Establishment Entries', grid=True, ylabel='Entries', legend=None)
    metro.reset_index().pivot('year', 'metro', 'pop_estimates').plot(ax=a[0, 1], title='Metro Population', grid=True, ylabel='Population', legend=None)
    nonmetro.reset_index().pivot('year', 'metro', 'estabs_entry').plot(ax=a[1, 0], title='Nonmetro Establishment Entries', grid=True, ylabel='Entries', legend=None)
    nonmetro.reset_index().pivot('year', 'metro', 'pop_estimates').plot(ax=a[1, 1], title='Nonmetro Population', grid=True, ylabel='Population', legend=None)
    # nonmetro.reset_index().pivot('year', 'metro', 'estabs_entry').plot(ax=a[1, 0], title='Nonmetro Establishment Entries', grid=True, ylabel='Establishments', legend=None)
    # nonmetro.reset_index().pivot('year', 'metro', 'pop_estimates').plot(ax=a[1, 1], title='Nonmetro Population', grid=True, ylabel='Population', legend=None)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/plots/4_estab_entry_plot.png')
    plt.show()
    # create subplot 2
    # create subplot 1
    f, a = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    metro.reset_index().pivot('year', 'metro', 'estabs_exit').plot(ax=a[0, 0], title='Metro Establishment Exits', grid=True, ylabel='Establishments', legend=None)
    metro.reset_index().pivot('year', 'metro', 'pop_estimates').plot(ax=a[0, 1], title='Metro Population', grid=True, ylabel='Population', legend=None)
    nonmetro.reset_index().pivot('year', 'metro', 'estabs_exit').plot(ax=a[1, 0], title='Nonmetro Establishment Exits', grid=True, ylabel='Establishments', legend=None)
    nonmetro.reset_index().pivot('year', 'metro', 'pop_estimates').plot(ax=a[1, 1], title='Nonmetro Population', grid=True, ylabel='Population', legend=None)
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/plots/4_estab_exit_plot.png')
    plt.show()
    vars_list = {'estabs_pop': 'Establishments per 100 people',
                 'estabs_entry_pop': 'Establishment entries per 100 people',
                 'estabs_exit_pop': 'Establishment exits per 100 people',
                 'per_births': 'Percent of all establishments that started operations in the past year',
                 'per_exits': 'Percent of all establishments that stopped operations in the past year',
                 'births_to_exits_ratio': 'Establishment births to exits ratio'}
    for var, var_title in vars_list.items():
        temp_df = data.pivot_table(index=['year'], columns=['metro'], values=var).reset_index()
        temp_df.rename({'M': 'metro_' + str(var), 'N': 'nonmetro_' + str(var)}, axis=1, inplace=True)
        temp_df.plot(x='year', y=['metro_' + str(var), 'nonmetro_' + str(var)])
        leg_1_labels = ['Metro', 'Nonmetro']
        plt.legend(labels=leg_1_labels, loc='best', fontsize='small')
        title = (str(var_title) + ' in Metro and Nonmetro Areas')
        plt.title("\n".join(wrap(title, 40)))
        plt.xticks(rotation=0, wrap=True)
        plt.subplots_adjust(bottom=0.6)
        # plt.ylabel('Percent')
        plt.xlabel('Year')
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/plots/' + str(var) + '_plot.png')
        temp_df.to_excel('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/2022_pep_est/tables/' + str(var) + '_table.xlsx')
        plt.show()
    return data

if __name__ == '__main__':
    df = data_create()
    data = calculator(df)
    data = plotter(data)
    print(df.head())
