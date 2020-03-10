# reasons data downloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCB35
# source data downloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCB36
# outcome data downloaded manually from https://factfinder.census.gov/bkmk/table/1.0/en/ASE/2016/00CSCB37

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

# REASONS FOR BUSINESS ADVICE OR MENTORING
reasons = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/ASE_2016_00CSCB35_with_ann.csv')
# keep vars
reasons = reasons[['GEO.display-label', 'NAICS.display-label', 'ASECB.display-label', 'YIBSZFI.display-label',
         'SEEKADV.display-label', 'FIRMPDEMP', 'FIRMPDEMP_PCT']]
# Rename columns
reasons.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "SEEKADV.display-label": "reason", "FIRMPDEMP": "count", "FIRMPDEMP_PCT": "percent"},
    inplace=True)

reasons = reasons[reasons.reason != 'All firms']
reasons = reasons[reasons.reason != 'Other']
reasons = reasons[reasons.reason != 'Total reporting']
reasons = reasons[reasons.reason != 'Item not reported']
reasons = reasons.drop(reasons.index[0:1])
reasons.reset_index(inplace=True, drop=True)




# SOURCE OF BUSINESS ADVICE OR MENTORING
source = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/ASE_2016_00CSCB36_with_ann.csv')
# keep vars
source = source[['GEO.display-label', 'NAICS.display-label', 'ASECB.display-label', 'YIBSZFI.display-label',
         'PROVADV.display-label', 'FIRMPDEMP', 'FIRMPDEMP_PCT']]
# Rename columns
source.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "PROVADV.display-label": "source", "FIRMPDEMP": "count", "FIRMPDEMP_PCT": "percent"},
    inplace=True)
source = source[source.source != 'Item not reported']
source = source[source.source != 'Not applicable']
source = source[source.source != 'All firms']
source["source"]= source["source"].str.replace("Business sought advice or mentoring from family", "family", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from friends", "friends", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from professional colleagues", "colleagues", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from employees", "employees", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from legal and professional advisors", "legal and professional advisors", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from customers", "customers", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from suppliers", "suppliers", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from government-supported technical assistance program", "government-supported technical assistance program", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from other source", "other", case = True)



# OUTCOME OF BUSINESS ADVICE OR MENTORING
outcome = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/ASE_2016_00CSCB37_with_ann.csv')
# keep vars
outcome = outcome[['GEO.display-label', 'NAICS.display-label', 'ASECB.display-label', 'YIBSZFI.display-label',
         'ADVOUTCOME.display-label', 'FIRMPDEMP', 'FIRMPDEMP_PCT']]
# Rename columns
outcome.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "ADVOUTCOME.display-label": "outcome", "FIRMPDEMP": "count", "FIRMPDEMP_PCT": "percent"},
    inplace=True)
outcome = outcome[outcome.outcome != 'Item not reported']
outcome = outcome[outcome.outcome != 'Not applicable']
outcome = outcome[outcome.outcome != 'All firms']
outcome = outcome[outcome.outcome != 'Total reporting']
outcome["outcome"]= outcome["outcome"].str.replace("Advice or mentoring led to positive business outcomes or anticipated positive changes in business operations", "positive", case = True)
outcome["outcome"]= outcome["outcome"].str.replace("Advice or mentoring did not lead to positive business outcomes or anticipated positive changes in business operations", "not positive", case = True)


# FILTER FUNCTION
def filterer(df):
    df = df[df['region'] == 'United States']
    df = df[df['industry'] == 'Total for all sectors']
    df = df[(df.demographic == 'All firms')]
    # df = df[(df.firm_age == 'All firms') | (df.firm_age == 'Firms with less than 2 years in business')]
    df.reset_index(inplace=True, drop=True)
    df.drop(df.columns[0:2], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    print(df)
    return df


reasons = filterer(reasons)
source = filterer(source)
outcome = filterer(outcome)



# unstack reasons
df = pd.DataFrame(columns=['reason'])
for group in reasons.groupby(['demographic', 'firm_age']) :
    df_temp = group[1][['reason', 'percent']].rename(columns={'percent': ' '.join(group[0])})
    df = df_temp.merge(df, how='left', on='reason')
reasons = df
print(reasons)




# unstack sources
df = pd.DataFrame(columns=['source'])
for group in source.groupby(['demographic', 'firm_age']) :
    df_temp = group[1][['source', 'percent']].rename(columns={'percent': ' '.join(group[0])})
    df = df_temp.merge(df, how='left', on='source')
source = df
print(source)


# unstack outcomes
df = pd.DataFrame(columns=['outcome'])
for group in outcome.groupby(['demographic', 'firm_age']) :
    df_temp = group[1][['outcome', 'percent']].rename(columns={'percent': ' '.join(group[0])})
    df = df_temp.merge(df, how='left', on='outcome')
outcome = df
print(outcome)



def saver(df, save=None):
    if save:
        df.to_excel(save, index=False)

saver(reasons,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/age_reasons_mentor.xlsx')
saver(source,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/age_sources_mentor.xlsx')
saver(outcome,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/age_outcomes_mentor.xlsx')

sys.exit()

