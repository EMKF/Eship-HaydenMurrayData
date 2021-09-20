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
    df = pd.read_csv('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/industry/mpj_us_industry.csv')
    return df

def filterer(df):
    df = df[(df.firmage == '0-1 years')].reset_index(drop=True)
    df = df[(df.industry == 'Health Care and Social Assistance') |\
            (df.industry == 'Administrative and Support and Waste Management and Remediation Services') |\
            (df.industry == 'Professional, Scientific, and Technical Services') |\
            (df.industry == 'Retail Trade') |\
            (df.industry == 'Construction')].reset_index(drop=True)
    return df

def plotter(df):
    df['contribution'] = df['contribution'] * 100
    unique_demos = (df['industry'].unique())
    indicators = ['contribution', 'creation', 'constancy']
    for indicator in indicators:
        df_temp = df.pivot_table(index=['time'], columns=['industry'], values=indicator).reset_index()
        print(df_temp.head())
        df_temp.plot(x='time', y=unique_demos)
        plt.xlabel('time')
        plt.xticks(rotation=45)
        plt.xlim(1993, 2019)
        plt.ylabel(indicator)
        leg_1_labels = unique_demos
        plt.legend(labels=leg_1_labels, loc='upper left', fontsize='small', bbox_to_anchor=(0, -.3))
        title = (str(indicator) + ' by industry for startups in the United States between 1993 and 2019')
        plt.title("\n".join(wrap(title, 40)))
        plt.tight_layout()
        plt.grid()
        plt.savefig('/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/industry/industry_plots/' + str(indicator) + '_' + 'industry.png')
        plt.show()
    return df


if __name__ == '__main__':
    df = data_create()
    df = filterer(df)
    df = plotter(df)



