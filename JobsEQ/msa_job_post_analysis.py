import pandas as pd
import matplotlib.pyplot as plt
import sys

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.options.mode.chained_assignment = None

# pull in merged rti job postings and employer database file
df = pd.read_csv('s3://emkf.data.research/other_data/chmura/rti_databaseUSA_2020-07-08.csv')

# remove time from startDate
df['month_post_start'] = df['dateStart'].str[:7]
df['year_post_start'] = df['dateStart'].str[:4]

# convert startDate to DateTime
df['dateStart'] = pd.to_datetime(df['dateStart'])
df['month_post_start'] = pd.to_datetime(df['month_post_start'])
df['year_post_start'] = pd.to_datetime(df['year_post_start'])
print(df.head())

# plot distribution of job postings over time
print(df['month_post_start'].value_counts())
print(df['year_post_start'].value_counts())
print(df['month_post_start'].value_counts().plot())
plt.show()
# plt.show()