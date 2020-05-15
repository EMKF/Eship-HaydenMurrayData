# data downloaded manually from: https://www.federalreserve.gov/consumerscommunities/shed_data.htm

import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.options.mode.chained_assignment = None


# pull,
data = pd.read_csv('/Users/hmurray/Desktop/data/SHED/2018_SHED_data.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# subset
df = data[['ED0', 'D3A', 'SL3', 'SL4']]

# rename columns
df.rename(columns={"ED0": "edu_level", "D3A": "Business_Ownership", "SL3": "Total_Student_Loans"},inplace=True)

# rename strings
df['Business_Ownership'] = df['Business_Ownership'].str.replace("For a single company or employer", "Employed", case = True)
df['Business_Ownership'] = df['Business_Ownership'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)

# fill NaN with no student loan debt
df['Total_Student_Loans'].fillna('No student loan debt', inplace=True)
print(df.head())

# quick value count
total_loans = (df['Total_Student_Loans'].value_counts(normalize=True))
total_loans.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/anna/total_loans.xlsx')

edu_level = (df['edu_level'].value_counts(normalize=True))
edu_level.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/anna/edu_level.xlsx')

own = (df['Business_Ownership'].value_counts(normalize=True))
own.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/anna/Business_Ownership.xlsx')

# crosstabs
new = pd.DataFrame()
def crosser(var, save=None):
    print(var.value_counts(normalize=True))
    new = (pd.crosstab([var], df['Business_Ownership'], normalize='columns')).round(4) * 100
    print(new)
    return new
    if save:
        new.to_excel(save, index=True)

df1 = pd.DataFrame()
for x in df:
    df1 = df1.append(crosser(df[x], '/Users/hmurray/Desktop/data/SHED/student_loans/anna/anna' + str(x) + '.xlsx'))
print(df1)
df1.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/anna/anna.xlsx')

# edu by debt
edu_debt = (pd.crosstab(df['edu_level'], df['Total_Student_Loans'], normalize='columns')).round(4) * 100
print(edu_debt)
edu_debt.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/anna/edu_debt.xlsx')


