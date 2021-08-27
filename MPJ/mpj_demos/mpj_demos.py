import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

def plotter(df, demo):
    df_temp = df[(df.firmage == '0-1 years').reset_index(drop=True)]
    print(df_temp.head())
    indicators = ['contribution', 'constancy', 'creation']
    #     for indicator in indicators:
    #         df_temp = df_temp.pivot_table(index=['time'], columns=[demo], values=indicator).reset_index()
    #         print(df_temp.head())
    #     #     df_temp.plot(x='year', y=[state, 'United States'])
    #     #     plt.xlim(1996, 2020)
    #     #     plt.xlabel('time')
    #     #     plt.xticks(rotation=45)
    #     #     plt.ylabel(indicator)
    #     #     leg_1_labels = [state, 'United States']
    #     #     plt.legend(labels=leg_1_labels)
    #     #     title = (str(state) + ' ' + (indicator))
    #     #     plt.title("\n".join(wrap(title, 70)))
    #     #     plt.tight_layout()
    #     #     plt.grid()
    #     #     plt.savefig('/Users/hmurray/Desktop/data/KESE/state_factsheet/maddi_copy_creation/plots/' + str(state) + '_' + str(indicator) + '.png')
    #     # return df

if __name__ == '__main__':
    # mpj_dict = data_create()
    # print(mpj_dict['mpj_sex.csv'].head())
    # print(mpj_dict['mpj_race_ethnicity.csv'].head())
    # print(mpj_dict['mpj_education.csv'].head())
    # print(mpj_dict['mpj_agegrp.csv'].head())
    path = '/Users/hmurray/Desktop/Jobs_Indicators/demos/demos_data/'
    csv_names = []
    for csv in os.listdir(path):
        df = pd.read_csv(str(path) + str(csv))
        plotter(df, 'sex')



