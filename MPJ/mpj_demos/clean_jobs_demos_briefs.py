import pandas as pd
import os
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

def startup_data_create():
    s_sex = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_sex.csv')
    s_race_eth = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_race_ethnicity.csv')
    s_edu = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_education.csv')
    s_age = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_agegrp.csv')
    s_ind = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/mpj_us_industry.csv')
    return s_sex, s_race_eth, s_edu, s_age, s_ind

def overall_data_create():
    o_sex = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_sex_overall.csv')
    o_race_eth = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_race_ethnicity_overall.csv')
    o_edu = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_education_overall.csv')
    o_age = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_agegrp_overall.csv')
    o_ind = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/mpj_us_industry_overall.csv')
    return o_sex, o_race_eth, o_edu, o_age, o_ind

def industry_replacer(df):
    df = df[(df.industry == 'Health Care and Social Assistance') |\
            (df.industry == 'Administrative and Support and Waste Management and Remediation Services') |\
            (df.industry == 'Professional, Scientific, and Technical Services') |\
            (df.industry == 'Retail Trade') |\
            (df.industry == 'Construction')].reset_index(drop=True)
    return df

def time_plotter(df, demo_col):
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
        plt.xlim(1993, 2019)
        plt.ylabel(indicator)
        leg_1_labels = unique_demos
        plt.legend(labels=leg_1_labels, loc='best', fontsize='small')
        title = (str(indicator) + ' by ' + str(demo_col) + ' for startups in the United States between 1993 and 2019')
        plt.title("\n".join(wrap(title, 40)))
        plt.subplots_adjust(bottom=.6, top=1)
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/startups/startup_plots/' + str(indicator) + '_' + str(demo_col) + '.png')
        # plt.show()
    return df

def ind_label_shortener(df):
    df['industry'] = df['industry'].replace({'Health Care and Social Assistance': 'HCSA',
                                             'Administrative and Support and Waste Management and Remediation Services': 'ASWMRS',
                                             'Professional, Scientific, and Technical Services': 'PSTS'})
    return df

def re_label_shortener(df):
    df['race_ethnicity'] = df['race_ethnicity'].replace({'Two or more race groups': '2+ Races',
                                                         'Pacific Islander': 'P.Islander'})
    return df

def edu_label_shortener(df):
    df['education'] = df['education'].replace({'Less than high school': '<H.S.',
                                             'High school or equivalent, no college': '=H.S.(No Col)',
                                             'Some college or Associate degree': 'Some Col/Ass.',
                                             'Bachelor\'s degree or advanced degree': 'B.A./B.S./Adv.',
                                             'Not available': 'NA',})
    return df

def comparer_plot(s_df, o_df, demo):
    indicators = ['contribution', 'creation', 'constancy']
    o_df['contribution'] = o_df['contribution'] * 100
    merge = pd.merge(o_df, s_df, on=['time', 'fips', 'region', demo])
    merge = merge[(merge.time == 2019).reset_index(drop=True)]
    # print(merge.head())
    for indicator in indicators:
        merge.plot(x=demo, y=[indicator + str('_x'), indicator + str('_y')], kind="bar")
        leg_1_labels = (indicator + str('_overall'), indicator + str('_startups'))
        plt.legend(labels=leg_1_labels, loc='best', fontsize='small')
        title = (str(indicator) + ' by ' + str(demo) + ' for startups and the overall workforce in 2019')
        plt.title("\n".join(wrap(title, 40)))
        plt.xticks(rotation=0, wrap=True)
        plt.subplots_adjust(bottom=0.6)
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/overalls/comparer_plots/' + str(indicator) + '_' + str(demo) + '.png')
        # plt.show()
    return s_df, o_df

if __name__ == '__main__':
    s_sex, s_race_eth, s_edu, s_age, s_ind = startup_data_create()
    o_sex, o_race_eth, o_edu, o_age, o_ind = overall_data_create()

    s_ind = industry_replacer(s_ind)
    o_ind = industry_replacer(o_ind)

    s_sex = time_plotter(s_sex, 'sex')
    s_race_eth = time_plotter(s_race_eth, 'race_ethnicity')
    s_edu = time_plotter(s_edu, 'education')
    s_age = time_plotter(s_age, 'agegrp')
    s_ind = time_plotter(s_ind, 'industry')

    s_ind = ind_label_shortener(s_ind)
    o_ind = ind_label_shortener(o_ind)

    s_race_eth = re_label_shortener(s_race_eth)
    o_race_eth = re_label_shortener(o_race_eth)

    s_edu = edu_label_shortener(s_edu)
    o_edu = edu_label_shortener(o_edu)

    s_sex, o_sex = comparer_plot(s_sex, o_sex, 'sex')
    s_race_eth, o_race_eth = comparer_plot(s_race_eth, o_race_eth, 'race_ethnicity')
    s_edu, o_edu = comparer_plot(s_edu, o_edu, 'education')
    s_age, o_age = comparer_plot(s_age, o_age, 'agegrp')
    s_ind, o_ind = comparer_plot(s_ind, o_ind, 'industry')