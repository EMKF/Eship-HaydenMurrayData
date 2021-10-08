import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    sex = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_sex.csv')
    race_eth = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_race_ethnicity.csv')
    edu = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_education.csv')
    age = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_agegrp.csv')
    ind = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_us_industry.csv')
    return sex, race_eth, edu, age, ind

def filterer(df):
    df = df[(df.firmage == '0-1 years')].reset_index(drop=True)
    df = df[(df.industry == 'Health Care and Social Assistance') |\
            (df.industry == 'Administrative and Support and Waste Management and Remediation Services') |\
            (df.industry == 'Professional, Scientific, and Technical Services') |\
            (df.industry == 'Retail Trade') |\
            (df.industry == 'Construction')].reset_index(drop=True)
    return df


def plotter(df, demo_col):
    df = df[(df.firmage == '0-1 years').reset_index(drop=True)]
    df['contribution'] = df['contribution'] * 100
    # print(df.head())
    unique_demos = (df[demo_col].unique())
    indicators = ['contribution', 'creation', 'constancy']
    for indicator in indicators:
        df_temp = df.pivot_table(index=['time'], columns=[demo_col], values=indicator).reset_index()
        # print(df_temp)
        df_temp.plot(x='time', y=unique_demos)
        plt.xlabel('time')
        plt.xticks(rotation=45)
        plt.xlim(2003, 2019)
        plt.ylabel(indicator)
        leg_1_labels = unique_demos
        plt.legend(labels=leg_1_labels, loc='upper left', fontsize='small', bbox_to_anchor=(0, -.3))
        title = (str(indicator) + ' by ' + str(demo_col) + ' for startups in the United States between 1993 and 2019')
        plt.title("\n".join(wrap(title, 40)))
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/plots/' + str(indicator) + '_' + str(demo_col) + '.png')
        # plt.show()
    return df

def comparer(demo_df, demo):
    overall = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_' + str(demo) + '_overall.csv')
    if demo == 'race_ethnicity':
        races = {
            'A1A1': 'White, not Hispanic',
            'A1A2': 'White, Hispanic',
            'A2A1': 'Black, not Hispanic',
            'A2A2': 'Black, Hispanic',
            'A3A1': 'American Indian, not Hispanic',
            'A3A2': 'American Indian, Hispanic',
            'A4A1': 'Asian, not Hispanic',
            'A4A2': 'Asian, Hispanic',
            'A5A1': 'Pacific Islander, not Hispanic',
            'A5A2': 'Pacific Islander, Hispanic',
            'A7A1': 'Two or more Race Groups, not Hispanic',
            'A7A2': 'Two or more Race Groups, Hispanic',
        }
        overall['race_ethnicity'] = overall['race_ethnicity'].map(races)
    print(overall.head())

    demo_df = demo_df[(demo_df.firmage == '0-1 years').reset_index(drop=True)]
    indicators = ['contribution', 'creation', 'constancy']
    merge = pd.merge(overall, demo_df, on=['time', 'fips', 'region', demo])
    merge = merge[(merge.time == 2019).reset_index(drop=True)]
    print(merge.head())
    for indicator in indicators:
        merge.plot(x=demo, y=[indicator + str('_x'), indicator + str('_y')], kind="bar")
        leg_1_labels = (indicator + str('_overall'), indicator + str('_startups'))
        plt.legend(labels=leg_1_labels, loc='upper left', fontsize='small', bbox_to_anchor=(1.05, 1))
        plt.tight_layout()
        plt.grid()
        # title = (str(indicator) + ' by ' + str(demo_col) + ' for startups in the United States between 1993 and 2019')
        # plt.title("\n".join(wrap(title, 40)))
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/overalls_plots' + str(indicator) + '_' + str(demo) + '.png')
        plt.show()
    return demo_df

if __name__ == '__main__':
    sex, race_eth, edu, age, ind = data_create()

    ind = filterer(ind)

    # sex = plotter(sex, 'sex')
    # race_eth = plotter(race_eth, 'race_ethnicity')
    # edu = plotter(edu, 'education')
    # age = plotter(age, 'agegrp')
    # ind = plotter(ind, 'industry')

    sex = comparer(sex, 'sex')
    race_eth = comparer(race_eth, 'race_ethnicity')
    edu = comparer(edu, 'education')
    age = comparer(age, 'agegrp')
    ind = comparer(ind, 'industry')

    #     df = filterer(df)
    #     df = plotter(df, 'sex')
        # demo_col = ['sex', 'race_ethnicity', 'education', 'agegrp']
        # for demo in demo_col:
        #     df = plotter(df, demo)