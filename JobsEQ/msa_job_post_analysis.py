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

# fill naics NaNs with earlier naics columns
df['naics02'] = df['naics02'].mask(pd.isnull, df['naics01'])
df['naics03'] = df['naics03'].mask(pd.isnull, df['naics02'])
df['naics04'] = df['naics04'].mask(pd.isnull, df['naics03'])
df['naics05'] = df['naics05'].mask(pd.isnull, df['naics04'])

# subset
# df = df[['id', 'title', 'company', 'year_established', 'dateStart', 'location', 'physical_city', 'physical_state', 'physical_zip', 'naics01', 'naics01_description', 'sic01']]
# df = df[['id', 'title', 'company', 'year_established', 'dateStart', 'physical_city', 'physical_state', 'physical_zip', 'naics01', 'naics01_description', 'naics02', 'naics02_description', 'naics03', 'naics03_description', 'naics04', 'naics04_description', 'naics05', 'naics05_description']]

# create age column
df['age'] = df['year_established']
df.loc[(df['year_established'] >= 2019), 'age'] = 'new'
df.loc[(df['year_established'] >= 2015) & (df['year_established'] <= 2018), 'age'] = 'young'
df.loc[(df['year_established'] <= 2014), 'age'] = 'mature'

def replacer(col):
    df[col] = df[col].astype(str).str[:-6]
    df['naics01'].replace({'45': '44', '33': '31', '42': '44', '32': '31'}, inplace=True)
    keepers = ['31', '44', '62', '72']
    df.loc[~df["naics01"].isin(keepers), "naics01"] = df[col]
    df['naics01'].replace({'45': '44', '33': '31', '42': '44', '32': '31'}, inplace=True)
    # print(df['naics01'].value_counts())
industries = ('naics01', 'naics02', 'naics03', 'naics04', 'naics05')
for col in industries:
    replacer(col)

# recode to NAICS categories
naics_categories = {
    '31': 'Manufacturing',
    '44': 'Retail Trade',
    '62': 'Health Care and Social Assistance',
    '72': 'Accommodation and Food Services'
}

# replace age number with string
df["naics01"].replace(naics_categories, inplace=True)

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
plt.title('Freq 2020 Online Job Postings for All Businesses in MINK MSAs')
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
plt.title('Freq 2020 Online Job Postings by Business Age in MINK MSAs')
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
naics_post_month = pd.crosstab(df['month_post_start'], df['naics01'], margins=False).reset_index(drop=False)
naics_post_month.to_excel('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/tables/naics_post_month.xlsx')
print(naics_post_month)
# plot
naics_post_month.plot(x='month_post_start', y=['Accommodation and Food Services', 'Health Care and Social Assistance', 'Retail Trade', 'Manufacturing'])
plt.xticks(rotation=45)
plt.title('Freq 2020 Online Job Postings by Industry in MINK MSAs')
plt.tight_layout()
plt.savefig('/Users/hmurray/Desktop/data/jobsEQ/job_posts/job_post_analysis/plots/naics01_post_month.png')
plt.show()
sys.exit()












