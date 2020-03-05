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
reasons = reasons[(reasons.reason != 'Other') | (reasons.reason != 'Total reporting') | (reasons.reason != 'Item not reported')]


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
source = source[(source.source != 'Item not reported') | (source.source != 'Not applicable') | (reasons.reason != 'All firms')]


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
outcome = outcome[(outcome.outcome != 'Item not reported') | (outcome.outcome != 'Not applicable') | (outcome.outcome != 'All firms')]


# FILTER FUNCTION
def filterer(df, save=None):
    df = df[df['region'] == 'United States']
    df = df[df['industry'] == 'Total for all sectors']
    df = df[(df.demographic == 'All firms') | (df.demographic == 'Male')\
            | (df.demographic == 'Female') | (df.demographic == 'Hispanic') | (df.demographic == 'White')\
            | (df.demographic == 'Asian') | (df.demographic == 'Black or African American')]
    df = df[(df.firm_age == 'All firms') | (df.firm_age == 'Firms with less than 2 years in business')]
    df.reset_index(inplace=True, drop=True)
    df.drop(df.columns[0:2], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    if save:
        df.to_excel(save, index=False)
    print(df.head(50))

filterer(reasons, '/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/mentor_reasons.xlsx')
filterer(source, '/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/mentor_sources.xlsx')
filterer(outcome, '/Users/hmurray/Desktop/Data_Briefs/ASE/Why_seek_business_advice/Data/mentor_outcomes.xlsx')

