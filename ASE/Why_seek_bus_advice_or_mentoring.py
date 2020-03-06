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
         'SEEKADV.display-label', 'FIRMPDEMP_PCT']]
# Rename columns
reasons.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "SEEKADV.display-label": "reason", "FIRMPDEMP_PCT": "percent"},
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
         'PROVADV.display-label', 'FIRMPDEMP_PCT']]
# Rename columns
source.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "PROVADV.display-label": "source", "FIRMPDEMP_PCT": "percent"},
    inplace=True)
source = source[source.source != 'Item not reported']
source = source[source.source != 'Not applicable']
source = source[source.source != 'All firms']



# OUTCOME OF BUSINESS ADVICE OR MENTORING
outcome = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/ASE_2016_00CSCB37_with_ann.csv')
# keep vars
outcome = outcome[['GEO.display-label', 'NAICS.display-label', 'ASECB.display-label', 'YIBSZFI.display-label',
         'ADVOUTCOME.display-label', 'FIRMPDEMP_PCT']]
# Rename columns
outcome.rename(
    columns={"GEO.display-label": "region", "NAICS.display-label": "industry", "ASECB.display-label": "demographic" \
        , "YIBSZFI.display-label": "firm_age", "ADVOUTCOME.display-label": "outcome", "FIRMPDEMP_PCT": "percent"},
    inplace=True)
outcome = outcome[outcome.outcome != 'Item not reported']
outcome = outcome[outcome.outcome != 'Not applicable']
outcome = outcome[outcome.outcome != 'All firms']
outcome = outcome[outcome.outcome != 'Total reporting']



# FILTER FUNCTION
def filterer(df):
    df = df[df['region'] == 'United States']
    df = df[df['industry'] == 'Total for all sectors']
    df = df[(df.demographic == 'All firms') | (df.demographic == 'Male')\
            | (df.demographic == 'Female') | (df.demographic == 'Hispanic') | (df.demographic == 'White')\
            | (df.demographic == 'Asian') | (df.demographic == 'Black or African American')]
    df = df[(df.firm_age == 'All firms') | (df.firm_age == 'Firms with less than 2 years in business')]
    df.reset_index(inplace=True, drop=True)
    df.drop(df.columns[0:2], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    print(df)
    return df


reasons = filterer(reasons)
source = filterer(source)
outcome = filterer(outcome)

# unstack reasons
reasons['all_firms'] = reasons['percent'].iloc[0:15].reset_index(drop=True)
reasons['less_2_years'] = reasons['percent'].iloc[15:30].reset_index(drop=True)
reasons['Hispanic'] = reasons['percent'].iloc[30:45].reset_index(drop=True)
reasons['White'] = reasons['percent'].iloc[45:60].reset_index(drop=True)
reasons['Black'] = reasons['percent'].iloc[60:75].reset_index(drop=True)
reasons['Asian'] = reasons['percent'].iloc[75:90].reset_index(drop=True)
reasons.drop(reasons.index[15: ], inplace=True)
reasons.drop(['percent'], axis=1, inplace=True)
print(reasons)
#
# unstack sources
source['all_firms'] = source['percent'].iloc[0:10].reset_index(drop=True)
source['less_2_years'] = source['percent'].iloc[10:20].reset_index(drop=True)
source['Hispanic'] = source['percent'].iloc[20:30].reset_index(drop=True)
source['White'] = source['percent'].iloc[30:40].reset_index(drop=True)
source['Black'] = source['percent'].iloc[40:50].reset_index(drop=True)
source['Asian'] = source['percent'].iloc[50:60].reset_index(drop=True)
source.drop(source.index[10: ], inplace=True)
source.drop(['percent'], axis=1, inplace=True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from family", "family", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from friends", "friends", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from professional colleagues", "colleagues", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from employees", "employees", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from legal and professional advisors", "legal and professional advisors", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from customers", "customers", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from suppliers", "suppliers", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from government-supported technical assistance program", "government-supported technical assistance program", case = True)
source["source"]= source["source"].str.replace("Business sought advice or mentoring from other source", "other", case = True)
print(source)

# unstack outcomes
outcome['all_firms'] = outcome['percent'].iloc[0:2].reset_index(drop=True)
outcome['less_2_years'] = outcome['percent'].iloc[2:4].reset_index(drop=True)
outcome['Hispanic'] = outcome['percent'].iloc[4:6].reset_index(drop=True)
outcome['White'] = outcome['percent'].iloc[6:8].reset_index(drop=True)
outcome['Black'] = outcome['percent'].iloc[8:10].reset_index(drop=True)
outcome['Asian'] = outcome['percent'].iloc[10:12].reset_index(drop=True)
outcome.drop(outcome.index[2: ], inplace=True)
outcome.drop(['percent'], axis=1, inplace=True)
outcome["outcome"]= outcome["outcome"].str.replace("Advice or mentoring led to positive business outcomes or anticipated positive changes in business operations", "positive", case = True)
outcome["outcome"]= outcome["outcome"].str.replace("Advice or mentoring did not lead to positive business outcomes or anticipated positive changes in business operations", "not positive", case = True)
print(outcome)

def saver(df, save=None):
    if save:
        df.to_excel(save, index=False)

saver(reasons,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/reasons_mentor.xlsx')
saver(source,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/sources_mentor.xlsx')
saver(outcome,'/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/outcomes_mentor.xlsx')

sys.exit()

