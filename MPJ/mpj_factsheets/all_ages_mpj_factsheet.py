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

def harry_plotter(df, key):
    # plot KS and US contribution/compensation/constance/creation aka 'x' over time
    temp_df = df.pivot_table(index='year', columns='category', values=key).reset_index()
    temp_df.plot(x='year', y=['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+'], kind='bar')
    plt.xlabel('time')
    plt.xticks(rotation=45)
    # plt.xlim(2004, 2019)
    plt.ylabel(key)
    leg_1_labels = ['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+']
    plt.legend(labels=leg_1_labels)
    # title = (value)
    # plt.title("\n".join(wrap(title, 70)))
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/factsheets/plots/ages_KS' + str(key) + '.png')
    temp_df.to_excel('/Users/hmurray/Desktop/Jobs_Indicators/factsheets/tables/ages_KS' + str(key) + '.xlsx')
    plt.show()
    return df

def rec_year_harry_plotter(df, key):
    # plot KS and US contribution/compensation/constance/creation aka 'x' over time
    df = df.query('year == 2019').reset_index(drop=True)
    temp_df = df.pivot_table(index='year', columns='category', values=key).reset_index()
    temp_df.plot(x='year', y=['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+'], kind='bar')
    plt.ylabel(key)
    leg_1_labels = ['Ages 0 to 1', 'Ages 2 to 3', 'Ages 4 to 5', 'Ages 6 to 10', 'Ages 11+']
    plt.legend(labels=leg_1_labels)
    plt.tight_layout()
    plt.grid()
    plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/factsheets/plots/rec_year_ages_KS' + str(key) + '.png')
    plt.show()
    return df

#loop to do this for every indicator x out of contribution, compensation, constancy, and creation
if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    print(df.head(25))
#     vars_titles = {'contribution': 'Between 2004 and 2019, the share of private sector employment attributable to firms \
# 11+ years has steadily increased while each other category of business age has steadily decreased.',
#                    'compensation': 'Since 2004, an average worker in Kansas, regardless of business age, earned less \
# than an average worker at the national level. In Kansas in 2019, an average worker in a firm 0-1 years earned 53.2% of \
# average private worker earnings across firms regardless of firm age, up nearly 10 percentage points over the past 3 years.',
#                    'constancy': 'In Kansas in 2019, 54.3% of jobs in firms 0-1 years lasted at least three quarters, \
# compared to 76.04% in firms 11+ years.',
#                    'creation': 'In 2019, firms 0-1 years in Kansas created on average 4.1 jobs per 1,000 people, more \
# than any other category of business age. Firms 0-1 years in Kansas have created at least 3 jobs per 1,000 people every year since 2004.'}
#     for key, value in vars_titles.items():
#         df = harry_plotter(df, key, value)
    variables = ['contribution', 'compensation', 'constancy', 'creation']
    for key in variables:
        df = harry_plotter(df, key)
    for key in variables:
        df = rec_year_harry_plotter(df, key)