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
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None


# DRAFT 2 (MULTIPLE SCRIPTS IN THIS .py FILE)


# pull,
df_agg = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
print(df_agg.head())
sys.exit()

# replace "Refused" with NaN
df_agg.replace('Refused', np.nan, inplace=True)
df_agg.replace('Other (Please specify):', np.nan, inplace=True)

# shorten strings
df_agg['D3A'] = df_agg['D3A'].str.replace("For a single company or employer", "Employed", case = True)
df_agg['D3A'] = df_agg['D3A'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)

# draft
df = pd.DataFrame()
def crosser(var, save=None):
    df = (pd.crosstab([var], df_agg['D3A'], normalize='columns')).round(4) * 100
    print(df)
    if save:
        df.to_excel(save, index=True)


crosser(df_agg['EF5A'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF5A.xlsx')
crosser(df_agg['EF6A_a'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_a.xlsx')
crosser(df_agg['EF6A_b'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_b.xlsx')
crosser(df_agg['EF6A_c'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_c.xlsx')
crosser(df_agg['EF6A_d'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_d.xlsx')
crosser(df_agg['EF6A_e'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_e.xlsx')
crosser(df_agg['EF6A_f'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_f.xlsx')
crosser(df_agg['EF6A_g'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6A_g.xlsx')
crosser(df_agg['EF1'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF1.xlsx')
print(df_agg['EF1'].value_counts(normalize=True))
crosser(df_agg['EF2'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF2.xlsx')
print(df_agg['EF2'].value_counts(normalize=True))
crosser(df_agg['EF3_a'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_a.xlsx')
print(df_agg['EF3_a'].value_counts(normalize=True))
crosser(df_agg['EF3_b'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_b.xlsx')
print(df_agg['EF3_b'].value_counts(normalize=True))
crosser(df_agg['EF3_c'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_c.xlsx')
print(df_agg['EF3_c'].value_counts(normalize=True))
crosser(df_agg['EF3_d'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_d.xlsx')
print(df_agg['EF3_d'].value_counts(normalize=True))
crosser(df_agg['EF3_e'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_e.xlsx')
print(df_agg['EF3_e'].value_counts(normalize=True))
crosser(df_agg['EF3_f'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_f.xlsx')
print(df_agg['EF3_f'].value_counts(normalize=True))
crosser(df_agg['EF3_g'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_g.xlsx')
print(df_agg['EF3_g'].value_counts(normalize=True))
crosser(df_agg['EF3_h'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF3_h.xlsx')
print(df_agg['EF3_h'].value_counts(normalize=True))
crosser(df_agg['EF5B'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF5B.xlsx')
print(df_agg['EF5B'].value_counts(normalize=True))
crosser(df_agg['EF6B_a'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_a.xlsx')
print(df_agg['EF6B_a'].value_counts(normalize=True))
crosser(df_agg['EF6B_b'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_b.xlsx')
print(df_agg['EF6B_b'].value_counts(normalize=True))
crosser(df_agg['EF6B_c'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_c.xlsx')
print(df_agg['EF6B_c'].value_counts(normalize=True))
crosser(df_agg['EF6B_d'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_d.xlsx')
print(df_agg['EF6B_d'].value_counts(normalize=True))
crosser(df_agg['EF6B_e'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_e.xlsx')
print(df_agg['EF6B_e'].value_counts(normalize=True))
crosser(df_agg['EF6B_f'], '/Users/hmurray/Desktop/Data_Briefs/SHED/vulnerability_bus_own/xtabs/D3A_EF6B_f.xlsx')
print(df_agg['EF6B_f'].value_counts(normalize=True))


# plot for brief
df_agg['D3A'] = df_agg['D3A'].str.replace("For a single company or employer", "Employed", case = True)
df_agg['D3A'] = df_agg['D3A'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)
df_agg.groupby('D3A').SL6.value_counts(normalize=True).unstack(0).plot(kind='bar')
title = 'Would you partially pay or skip student loan payment if $400 emergency expense occurred?'
plt.title('\n'.join(wrap(title,60)), fontsize=14)
plt.xticks(fontsize=10, rotation=0)
plt.tight_layout()
plt.xlabel('')
plt.savefig('/Users/hmurray/Desktop/data/SHED/student_loans/skip_pay.png')
plt.show()



sys.exit()



###################################################### DRAFT BELOW ######################################################

# subset by business ownership and EF-
df1 = df_agg['D3A']
df2 = df_agg[df_agg.columns[pd.Series(df_agg.columns).str.startswith('EF')]]
df = pd.concat([df1, df2], axis=1)


# crosstab function
def crosstab_all(dataset, attributelist):
    for v in var:
        print()
        name = pd.crosstab(dataset["D3A"],dataset[v], normalize='index', margins=False)
        name = np.transpose(name)
        print(name)

var = df_agg[df_agg.columns[pd.Series(df_agg.columns).str.startswith('EF')]]
crosstab_all(df_agg, var)


sd = pd.crosstab(df_agg["D3A"], df_agg['FS40'], normalize='index', margins=False)
sd = np.transpose(sd)
print(sd)

E4_a = pd.crosstab(df_agg["D3A"], df_agg['E4_a'], normalize='index', margins=False)
E4_a = np.transpose(E4_a)
print(E4_a)

E4_b = pd.crosstab(df_agg["D3A"], df_agg['E4_b'], normalize='index', margins=False)
E4_b = np.transpose(E4_b)
print(E4_b)
