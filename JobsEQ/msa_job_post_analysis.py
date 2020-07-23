import pandas as pd
import matplotlib.pyplot as plt
import requests
import numpy as np
import seaborn as sns
from textwrap import wrap
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
print(df.query('year_established <= 2019').query('year_post_start == 2020')['month_post_start'].value_counts().plot())
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
plt.show()

# TO DO - how does histogram based on year_established relate to distribution from survival data?
df['year_established'].plot.hist(bins=50)
# plt.title('Distribution of year_established for Companies in MSA Employer Job Postings Dataset')
plt.title("\n".join(wrap("Distribution of year_established for Companies in MSA Employer Job Postings Dataset", 50)))
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/year_est_hist.png')
plt.show()

# BLS Table 7
surv = pd.read_csv('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tab7bls_survival.csv')
print(surv.head(100))
surv = surv[(surv['age'] == 0)]
print(surv.head(100))

sys.exit()






