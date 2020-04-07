import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None


# pull,
df_all = pd.read_csv('/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/pull/median_earnings_2005_2018_gender.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# rename strings
df_all['employment_type'] = df_all['employment_type'].str.replace("private_self_employed", "inc_self", case = True)
df_all['employment_type'] = df_all['employment_type'].str.replace("self_employed_not_inc", "uninc_self", case = True)

# filter for overall and gender
df_all = df_all[(df_all.employment_type == 'inc_self') | (df_all.employment_type == 'uninc_self') | (df_all.employment_type == 'total')].reset_index(drop=True)
print(df_all.head(100))
gender = df_all[(df_all.gender == 'male') | (df_all.gender == 'female')].reset_index(drop=True)
overall = df_all[(df_all.gender == 'overall')].reset_index(drop=True)

# concatenate columns and then plot overall and gender
def con_plot_saver(df, save1, title, save2):
       df['type'] = df['gender'] + str('_') + df['employment_type']
       df.drop(['gender', 'employment_type'], axis=1, inplace=True)
       df.to_excel(save1, index=False)
       df.pivot_table(index=['year'], columns=['type'], values='median_earnings').plot()
       plt.title("\n".join(wrap(title, 50)))
       plt.savefig(save2)
       plt.show()

# define paths to shorten function inputs
gender_save1 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/gender_se_earnings.xlsx'
gender_save2 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/gender_se_earnings.png'
overall_save1 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/overall_se_earnings.xlsx'
overall_save2 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/overall_se_earnings.png'
df_all1 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/gender+overall__se_earnings.xlsx'
df_all2 = '/Users/hmurray/Desktop/data/ACS/uninc_inc_self_emp/gender+overall_se_earnings.png'

# define titles
title_overall = "Figure 1: US Median Earnings for Incorporated and Unincorporated Self-Employed"
title_gender = "Figure 2: US Median Earnings for Incorporated and Unincorporated Self-Employed by Gender"
title_all = "US Median Earnings for Incorporated and Unincorporated Self-Employed"

# call concatenate, plotter, and saver function
con_plot_saver(overall, overall_save1, title_overall, overall_save2)
con_plot_saver(gender, gender_save1, title_gender, gender_save2)
con_plot_saver(df_all, df_all1, title_all, df_all2)

sys.exit()