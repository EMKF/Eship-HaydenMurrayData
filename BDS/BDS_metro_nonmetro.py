#

import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# get data
df = pd.ExcelFile('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/bds_f_metrononmetro_release.xlsx')
metro = pd.read_excel(df, 'Metro')
nonmetro = pd.read_excel(df, 'Non_Metro')


def filterer(df, save=None):
    df.columns = df.iloc[8]
    df = df.loc[9: ]
    df.reset_index(inplace=True, drop=True)
    df = df[['Year', 'Estabs', 'Estabs_Entry', 'Estabs_Exit']]
    if save:
        df.to_excel(save, index=False)
    return df

metro = filterer(metro, '/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/bds_metro.xlsx')
nonmetro = filterer(nonmetro, '/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/bds_nonmetro.xlsx')

# merge and rename columns
legacy = pd.merge(metro, nonmetro, on='Year', how='inner')
legacy.rename(
    columns={"Estabs_x": "metro_est", "Estabs_Entry_x": "metro_births", "Estabs_Exit_x": "metro_exits", \
             "Estabs_y": "nonmetro_est", "Estabs_Entry_y": "nonmetro_births", "Estabs_Exit_y": "nonmetro_exits"},
    inplace=True)


# calculate trends
legacy['total_est'] = legacy['metro_est'] + legacy['nonmetro_est']
legacy['total_births'] = legacy['metro_births'] + legacy['nonmetro_births']
legacy['total_exits'] = legacy['metro_exits'] + legacy['nonmetro_exits']
legacy['%_metro_births'] = (legacy['metro_births'] / legacy['total_births'])*100
legacy['%_nonmetro_births'] = (legacy['nonmetro_births'] / legacy['total_births'])*100
legacy['%_metro_exits'] = (legacy['metro_exits'] / legacy['total_exits'])*100
legacy['%_nonmetro_exits'] = (legacy['nonmetro_exits'] / legacy['total_exits'])*100
legacy['metro_ratio_birth_exit'] = legacy['metro_births'] / legacy['metro_exits']
legacy['nonmetro_ratio_birth_exit'] = legacy['nonmetro_births'] / legacy['nonmetro_exits']
legacy2 = legacy[['Year', '%_metro_births', '%_nonmetro_births', '%_metro_exits',\
                  '%_nonmetro_exits', 'metro_ratio_birth_exit', 'nonmetro_ratio_birth_exit']]
print(legacy2)
legacy2.to_excel('/Users/hmurray/Desktop/data/BDS/bds_metro_nonmetro_table.xlsx', index=False)

# plot births
legacy2.plot(x='Year', y=['%_metro_births', '%_nonmetro_births'], figsize=(7,5), grid=True)
plt.title('The proportion of establishment births in metro and nonmetro areas')
plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/birth_plot.png')
plt.show()

# plot exits
legacy2.plot(x='Year', y=['%_metro_exits', '%_nonmetro_exits'], figsize=(7,5), grid=True)
plt.title('The proportion of establishment exits in metro and nonmetro areas')
plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/exit_plot.png')
plt.show()

# plot ratio
legacy2.plot(x='Year', y=['metro_ratio_birth_exit', 'nonmetro_ratio_birth_exit'], figsize=(7,5), grid=True)
plt.title('The ratio of establishment births to exits in metro and nonmetro areas')
plt.savefig('/Users/hmurray/Desktop/data/BDS/metro_nonmetro/python_outputs/ratio_plot.png')
plt.show()

