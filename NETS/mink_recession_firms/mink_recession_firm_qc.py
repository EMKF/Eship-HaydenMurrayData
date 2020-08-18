# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you

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

# pull in nets est_counts that we generated in brief_1_qc.py
nets = pd.read_csv('/Users/hmurray/Desktop/data/NETS/st_est_counts.csv')
nets.rename(columns = {'state_fips':'region', 'FirstYear':'year'}, inplace = True)

# pull in pep that we saved locally (faster)
pep =  pd.read_excel('/Users/hmurray/Desktop/data/PEP/state_pep_2004_2018/state_pep_2004_2018.xlsx')

def filterer(df):
    # subset by MINK
    df = df[\
        (df['region'] == 'MO') |\
        (df['region'] == 'IA') |\
        (df['region'] == 'NE') |\
        (df['region'] == 'KS')].reset_index(drop=True)
    # subset by 2007-2010
    df = df[(df['year'] >= 2007) &\
            (df['year'] <= 2010)].reset_index(drop=True)
    return df
nets = filterer(nets)
pep = filterer(pep)

# merge nets and pep
df = nets.merge(pep, on=['region', 'year'])

# calculate new est by pop
df['estab_rate'] = (df['est_count'] / df['population']) * 10000
print(df)

# plot
fig_2 = df.pivot_table(index='year', columns='region', values='estab_rate').reset_index()
fig_2.plot(x='year', y=['MO', 'IA', 'NE', 'KS'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 2: New Establishments by Population (per 10,000), 2007-2010', 50)))
plt.tight_layout()
plt.grid()
# plt.savefig('/Users/hmurray/Desktop/data/NETS/nets_estab_rate.png')
plt.show()

