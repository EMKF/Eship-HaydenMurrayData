import pandas as pd
import matplotlib.pyplot as plt
import requests
import seaborn as ax
import numpy as np
import zipfile
import urlopen
from textwrap import wrap
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull in data
df = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/db_1_raw.xlsx', sheet_name='KESE_NEB_merge (1)',\
                   usecols=['state', 'year', 'ba', 'nets_new_establishments'])
print(df.head())

# figure_1
figure_1 = df.groupby(df['year'])[['ba', 'nets_new_establishments']].median().reset_index()
print(figure_1)
# plot figure_1
figure_1.plot(x='year', y=['ba', 'nets_new_establishments'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 1: BA and NETS Medians Over Time, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_1.png')
plt.show()

# figure_2
figure_2 = df.groupby(df['year'])[['ba', 'nets_new_establishments']].min().reset_index()
print(figure_2)
# plot figure_2
figure_2.plot(x='year', y=['ba', 'nets_new_establishments'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 2. BFS and NETS Minimums Over Time, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_2.png')
plt.show()

# figure_3
figure_3 = df.groupby(df['year'])[['ba', 'nets_new_establishments']].max().reset_index()
print(figure_3)
# plot figure_3
figure_3.plot(x='year', y=['ba', 'nets_new_establishments'])
plt.xticks(rotation=45)
plt.title("\n".join(wrap('Figure 3. BFS and NETS Maximums Over Time, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_3.png')
plt.show()

# figure_4
figure_4 = df[df['year'] == 2016]
print(figure_4)
# plot figure_4
figure_4.sort_values("ba", ascending=False).plot(x="state", y=["ba", "nets_new_establishments"], kind="bar")
plt.title("\n".join(wrap('Figure 4. BFS and NETS Counts of New Establishments by State, 2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_4.png')
plt.show()

# figure_5
figure_5 = df.groupby(df['state'])[['ba', 'nets_new_establishments']].sum().reset_index()
print(figure_5)
# plot figure_5
figure_5.sort_values("ba", ascending=False).plot(x='state', y=['ba', 'nets_new_establishments'], kind="bar")
plt.title("\n".join(wrap('Figure 5. Summed BFS and NETS Counts of New Establishments by State, 2005-2016', 50)))
plt.tight_layout()
plt.grid()
plt.savefig('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/figure_5.png')
plt.show()

sys.exit()