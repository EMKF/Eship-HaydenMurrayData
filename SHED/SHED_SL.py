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

# add options to the end of location to avoid using too much memory
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# keep vars
df_agg = df_agg[['ppagecat', 'ppinccat6', 'D3A', 'D3B', 'SL3', 'SL4', 'FS20_b', 'E4_a']]

# Rename columns
df_agg.rename(columns={"ppagecat": "age_categories", "ppinccat6": "income_categories", "D3A": "Business_Ownership", \
                       "D3B": "Full_Part_Time", "SL3": "Total_Student_Loans", "SL4": "Monthly_Student_Loan_Payment" ,\
                       "FS20_b": "Help_with_Student_Loan_Payments", "E4_a": "Emp_Health_Insurance", "E4_b": "Private_Health_Insurance"},inplace=True)

# aggregate dataframe of 3 analyses below
df = df_agg[['Monthly_Student_Loan_Payment','age_categories','income_categories', 'Business_Ownership',]]

# Convert rows of student loans with NaN to 'None' since NaN represents people with no student loan debt
df['Monthly_Student_Loan_Payment'] = df['Monthly_Student_Loan_Payment'].astype(object).replace(np.nan, 'No student loan debt')
df.Monthly_Student_Loan_Payment = df.Monthly_Student_Loan_Payment.fillna('No student loan debt')
print(df.head())

# arrange student loan categories
Monthly_Student_Loan_Payment_ordering = ["No student loan debt","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","I am currently not required to make any payments on these loans",\
                "Refused","Don't know"]
df.loc[:, ("Monthly_Student_Loan_Payment")] = pd.Categorical(df.loc[:, ("Monthly_Student_Loan_Payment")], categories=Monthly_Student_Loan_Payment_ordering)

# arrange income categories
inc_ordering = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]
df.loc[:, ("income_categories")] = pd.Categorical(df.loc[:, ("income_categories")], categories=inc_ordering)

# debt * age
ct_sl_age = (pd.crosstab(df['Monthly_Student_Loan_Payment'], df['age_categories'], normalize='columns'))\
    .round(4)*100
ct_sl_age.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_age.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(df['Monthly_Student_Loan_Payment'], df['income_categories'], normalize='columns'))\
    .round(4)*100
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_inc.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(df['Monthly_Student_Loan_Payment'], df['Business_Ownership'], normalize='columns'))\
    .round(4)*100
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_eship.csv')
print(ct_sl_eship)

# plots
