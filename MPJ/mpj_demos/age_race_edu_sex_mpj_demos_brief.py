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
    sex = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/mpj_sex.csv')
    race_eth = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/mpj_race_ethnicity.csv')
    edu = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/mpj_education.csv')
    age = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/mpj_agegrp.csv')
    return sex, race_eth, edu, age

def plotter(df, demo_col):
    df = df[(df.firmage == '0-1 years').reset_index(drop=True)]
    df['contribution'] = df['contribution'] * 100
    # print(df.head())
    unique_demos = (df[demo_col].unique())
    indicators = ['contribution', 'creation', 'constancy']
    for indicator in indicators:
        df_temp = df.pivot_table(index=['time'], columns=[demo_col], values=indicator).reset_index()
        print(df_temp)
        df_temp.plot(x='time', y=unique_demos)
        plt.xlabel('time')
        plt.xticks(rotation=45)
        plt.xlim(2003, 2019)
        plt.ylabel(indicator)
        leg_1_labels = unique_demos
        plt.legend(labels=leg_1_labels, loc='upper left', fontsize='small', bbox_to_anchor=(1.05, 1))
        title = (str(indicator) + ' by ' + str(demo_col) + ' for startups in the United States between 1993 and 2019')
        plt.title("\n".join(wrap(title, 40)))
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/plots/' + str(indicator) + '_' + str(demo_col) + '.png')
        # plt.show()
    return df

if __name__ == '__main__':
    sex, race_eth, edu, age = data_create()
    # mpj_files = [sex, race_eth, edu, age]
    # for df in mpj_files:
    #     print(df.head())
    sex = plotter(sex, 'sex')
    race_eth = plotter(race_eth, 'race_ethnicity')
    edu = plotter(edu, 'education')
    age = plotter(age, 'agegrp')


    #     df = filterer(df)
    #     df = plotter(df, 'sex')
        # demo_col = ['sex', 'race_ethnicity', 'education', 'agegrp']
        # for demo in demo_col:
        #     df = plotter(df, demo)