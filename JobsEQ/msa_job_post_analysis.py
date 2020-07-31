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
df = pd.read_csv('s3://emkf.data.research/other_data/chmura/rti_databaseUSA_2020-07-08.csv', low_memory=False)
print(df.head())

# subset
# df = df[['id', 'title', 'company', 'year_established', 'dateStart', 'location', 'physical_city', 'physical_state', 'physical_zip', 'naics01', 'naics01_description', 'sic01']]
# df = df[['id', 'title', 'company', 'year_established', 'dateStart', 'physical_city', 'physical_state', 'physical_zip', 'naics01', 'naics01_description', 'naics02', 'naics02_description', 'naics03', 'naics03_description', 'naics04', 'naics04_description', 'naics05', 'naics05_description']]

# create age column
df['age'] = df['year_established']
df.loc[(df['year_established'] >= 2019), 'age'] = 'new'
df.loc[(df['year_established'] >= 2015) & (df['year_established'] <= 2018), 'age'] = 'young'
df.loc[(df['year_established'] <= 2014), 'age'] = 'mature'

# reduce to 2-digit NAICS
# cols = ('naics01', 'naics02', 'naics03', 'naics04', 'naics05')
# for col in cols:
#     df['arcjve_naics1'] = df[col].astype(str).str[:-6].astype(np.int64)
df['naics01'] = df['naics01'].astype(str).str[:-6]
df['naics02'] = df['naics02'].astype(str).str[:-6]
df['naics03'] = df['naics03'].astype(str).str[:-6]
df['naics04'] = df['naics04'].astype(str).str[:-6]
df['naics05'] = df['naics05'].astype(str).str[:-6]


# copy naics01 column and recode to 4 naics categories
print(df['naics01'].value_counts())
df['naics'] = df['naics01']
df['naics'].replace({45: 44, 33: 31, 42: 44, 32: 31}, inplace=True)

# replace all naics values not equal to 31, 62, 72, and 44 with naics02
df['naics'] = df['naics'][df['naics'] !=[31, 44, 62, 72]] = df['naics02']

print(df['naics'].value_counts())
df = df[['naics01', 'naics', 'naics02', 'naics03', 'naics04', 'naics05']]
print(df.sort_values(by=['naics01'], ascending=False).head(1000))

sys.exit()

# recode to NAICS categories
naics_categories = {
    '31': 'manufacturing',
    '62': 'Health Care and Social Assistance',
    '72': 'Accommodation and Food Services',
    '44': 'Retail Trade'
}

# replace age number with string
df['naics_cat'] = df['naics'].astype(str)
df["naics_cat"].replace(naics_categories, inplace=True)

# remove time from startDate
df['month_post_start'] = df['dateStart'].str[:7]
df['year_post_start'] = df['dateStart'].str[:4]

# convert startDate to DateTime
df['dateStart'] = pd.to_datetime(df['dateStart'])
df['month_post_start'] = pd.to_datetime(df['month_post_start'])
df['year_post_start'] = pd.to_datetime(df['year_post_start'])

# filter job postings
df = df[df['month_post_start'].isin(pd.date_range(start='20200101', end='20200601'))]

### overall_post_month ###
# table
overall_post_month = df['month_post_start'].value_counts()
overall_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tables/overall_post_month.xlsx')
#plot
overall_post_month.plot()
plt.title('Freq 2020 Online Job Postings for All Businesses')
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/plots/overall_post_month.png')
plt.show()

### age_post_month ###
# table
age_post_month = pd.crosstab(df['month_post_start'], df['age'], margins=False).reset_index(drop=False)
age_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tables/age_post_month.xlsx')
# plot
age_post_month.plot(x='month_post_start', y=['mature', 'young', 'new'])
plt.xticks(rotation=45)
plt.title('Freq 2020 Online Job Postings by Business Age')
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/plots/age_post_month.png')
plt.show()

### MSA_post_month ###
# table
msa_post_month = pd.crosstab(df['month_post_start'], df['physical_state'], margins=False).reset_index(drop=False)
msa_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tables/msa_post_month.xlsx')
print(msa_post_month)
# plot
msa_post_month.plot(x='month_post_start', y=['IA', 'IL', 'KS', 'MO', 'NE', 'OK'])
plt.xticks(rotation=45)
plt.title('Freq 2020 Online Job Postings by Region')
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/plots/msa_post_month.png')
plt.show()

### ind_post_month ###
# table
ind_post_month = pd.crosstab(df['month_post_start'], df['physical_state'], margins=False).reset_index(drop=False)
ind_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tables/ind_post_month.xlsx')
print(ind_post_month)
# plot
ind_post_month.plot(x='month_post_start', y=['IA', 'IL', 'KS', 'MO', 'NE', 'OK'])
plt.xticks(rotation=45)
plt.title('Freq 2020 Online Job Postings by Region')
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/plots/ind_post_month.png')
plt.show()
sys.exit()







overall_post_month = df['month_post_start'].value_counts()
overall_post_month.plot()
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
overall_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/overall_post_month.xlsx')
plt.show()

# plot distribution of job postings by state over time
overall_post_month = df.query('year_established >= 2019')['month_post_start'].value_counts()
overall_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/overall_post_month.xlsx')
overall_post_month.plot()
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/2020_job_posts.png')
plt.show()
sys.exit()









# pull in merged rti job postings and employer database file
df = pd.read_csv('s3://emkf.data.research/other_data/chmura/rti_databaseUSA_2020-07-08.csv', low_memory=False)

# convert dateStart to int
df['dateStart'] = df['dateStart'].str[:7]
df[['year_post_start', 'month_post_start']] = df.dateStart.str.split("-", expand=True,).astype(int)

# # remove time from startDate
# df['month_post_start'] = df['dateStart'].str[:7]
# df['year_post_start'] = df['dateStart'].str[:4]

# # convert startDate to DateTime
# df['dateStart'] = pd.to_datetime(df['dateStart'])
# df['month_post_start'] = pd.to_datetime(df['month_post_start'])
# df['year_post_start'] = pd.to_datetime(df['year_post_start'])

# # subset by firms with founding date between 1995-2019
# df = df.query('year_established <= 2019').query('year_established >= 1994')
#
# # subset by job postings between January 2020 and July 2020
# df = df.query('year_post_start >= 2020').query('month_post_start <= 6')

# frequencies
print(df['year_established'].value_counts())
print(df['month_post_start'].value_counts())
print(df['year_post_start'].value_counts())
print(df['physical_state'].value_counts())

# drop duplicates
unique_bus = df
unique_bus.drop_duplicates(subset ="id", inplace = True)
unique_bus = unique_bus.reset_index(drop=True)

# crosstab unique businesses by state
unique_bus = pd.crosstab(unique_bus['id'], unique_bus['physical_state'], margins=True).reset_index()
unique_bus = unique_bus[unique_bus['id'] == 'All']
print(unique_bus)

# crosstab job postings by state
post_state_month = pd.crosstab(df['month_post_start'], df['physical_state'], margins=False)
post_state_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/monthly_job_posts_state.xlsx')
print(post_state_month)

# overall plot - subset by firms with founding date in 2019
print(df.query('year_established >= 2019').query('year_post_start == 2020')['month_post_start'].value_counts().plot())
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/2020_job_posts.png')
plt.show()
sys.exit()

# state plots
post_state_month.plot()
plt.title("\n".join(wrap("Count of Online Job Postings for X Industries in X MSAs", 50)))
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/state_posts.png')
plt.show()
sys.exit()


# filter for job postings between january 2020 and June 2020
jan_june = df
jan_june = jan_june[jan_june['month_post_start'].isin(pd.date_range(start='20200101', end='20200601'))]

# plot distribution of job postings over time
jan_june = jan_june.query('year_established <= 2019')
print(df.head())
df['month_post_start'].value_counts().plot()
plt.title('Freq 2020 Online Job Postings for Companies Founded in 2019')
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/2020_job_posts.png')
plt.show()

# state plots
post_state_month.plot()
plt.title("\n".join(wrap("Count of Online Job Postings for X Industries in X MSAs", 50)))
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/state_posts.png')
plt.show()
sys.exit()


sys.exit()

