import os
import sys
import shutil
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# add options to the end of location to avoid using too much memory
df = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# keep vars
df = df[['D3A', 'D3B', 'SL3', 'SL4', 'FS20_b', 'E4_a', 'E4_b']]
# Rename columns
df.rename(columns={"D3A": "Business_Ownership", "D3B": "Full_Part_Time", "SL3": "Total_Student_Loans", "SL4": "Monthly_Student_Loan_Payment"\
    ,"FS20_b": "Help_with_Student_Loan_Payments", "E4_a": "Emp_Health_Insurance", "E4_b": "Private_Health_Insurance"},inplace=True)

# drop NAN
df = df.dropna()
df.reset_index(inplace=True, drop=True)

# look at df
print(df)

# print frequencies
print(df['Business_Ownership'].value_counts())
print(df['Full_Part_Time'].value_counts())
print(df['Total_Student_Loans'].value_counts())
print(df['Monthly_Student_Loan_Payment'].value_counts())
print(df['Help_with_Student_Loan_Payments'].value_counts())

#crosstab business ownership by work status
# print(pd.crosstab(df['Business_Ownership'], df['Full_Part_Time']))

print(pd.crosstab(df['Emp_Health_Insurance'], df['Business_Ownership'], normalize='columns'))

print(pd.crosstab(df['Private_Health_Insurance'], df['Business_Ownership'], normalize='columns'))
