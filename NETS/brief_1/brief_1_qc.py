# NETS2017_Misc.txt - use 'firstyear' as business age
# NETS2017_Emp.txt - emp90 and empc90 tells you

import pandas as pd
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# # pull from S3
df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt',\
                 sep='\t', na_values=' ', lineterminator='\r', error_bad_lines=False, encoding='latin1')

# df = pd.read_csv('s3://emkf.data.research/other_data/nets/NETS_2017/NETS2017_Misc/NETS2017_Misc.txt',\
#                  sep='\t', na_values=' ', lineterminator='\r', nrows=500, error_bad_lines=False, encoding='latin1', low_memory=False)
print(df.head(500))

# subset
df = df[['DunsNumber', 'FipsCounty', 'FirstYear']]

# create state_fips
df['hm_county_fips'] = df['FipsCounty'].astype(str).str.zfill(5)
df['state_fips'] = df['hm_county_fips'].astype(str).str[:2].astype(int)

# state_codes dict, reverse dict, and recode fips to strings
state_codes = {
    'WA': 53, 'DE': 10, 'DC': 11, 'WI': 55, 'WV': 54, 'HI': 15,
    'FL': 12, 'WY': 56, 'PR': 72, 'NJ': 34, 'NM': 35, 'TX': 48,
    'LA': 22, 'NC': 37, 'ND': 38, 'NE': 31, 'TN': 47, 'NY': 36,
    'PA': 42, 'AK': 2, 'NV': 32, 'NH': 33, 'VA': 51, 'CO': 8,
    'CA': 6, 'AL': 1, 'AR': 5, 'VT': 50, 'IL': 17, 'GA': 13,
    'IN': 18, 'IA': 19, 'MA': 25, 'AZ': 4, 'ID': 16, 'CT': 9,
    'ME': 23, 'MD': 24, 'OK': 40, 'OH': 39, 'UT': 49, 'MO': 29,
    'MN': 27, 'MI': 26, 'RI': 44, 'KS': 20, 'MT': 30, 'MS': 28,
    'SC': 45, 'KY': 21, 'OR': 41, 'SD': 46
}
inv_state_codes = {v: k for k, v in state_codes.items()}
df["state_fips"].replace(inv_state_codes, inplace=True)

# value_counts
print(df['state_fips'].value_counts())
counts = (df.groupby(["state_fips", "FirstYear"]).size())
counts = counts.reset_index()
counts.rename(columns = {0:'est_count'}, inplace = True)
print(counts)
counts.to_excel('/Users/hmurray/Desktop/data/NETS/st_est_counts.xlsx', index=False)
sys.exit()

#########################################################################################################################
################################################# Danny's Files #########################################################
#########################################################################################################################

# pull in data
df = pd.read_excel('/Users/hmurray/Desktop/data/NETS/Danny_Smith_briefs/Four_Brief_Assignments/Brief_1/qc/db_1_raw.xlsx',\
                   sheet_name='KESE_NEB_merge (1)', usecols=['state', 'year', 'ba', 'nets_new_establishments'])
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