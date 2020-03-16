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

# add options to the end of location to avoid using too much memory
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
print(df_agg['B2'].value_counts(normalize=True, sort=False))
status_own = (pd.crosstab(df_agg['B2'], df_agg['D3A'], normalize='columns')).round(4)*100
print(status_own)
sys.exit()


# keep vars
df_agg = df_agg[['ppagecat', 'ppinccat6', 'D3A', 'D3B', 'SL3', 'SL4', 'FS20_b', 'E4_a']]

# Rename columns
df_agg.rename(columns={"ppagecat": "age_categories", "ppinccat6": "income_categories", "D3A": "Business_Ownership", \
                       "D3B": "Full_Part_Time", "SL3": "Total_Student_Loans", "SL4": "Monthly_Student_Loan_Payment" ,\
                       "FS20_b": "Help_with_Student_Loan_Payments", "E4_a": "Emp_Health_Insurance", "E4_b": "Private_Health_Insurance"},inplace=True)

# drop unnecessary responses + rename
# df_agg = df_agg[df_agg.Monthly_Student_Loan_Payment != 'Don\'t know']
# df_agg = df_agg[df_agg.Monthly_Student_Loan_Payment != 'Refused']
# df_agg = df_agg[df_agg.Business_Ownership != 'Other (Please specify):']
# df_agg = df_agg[df_agg.Business_Ownership != 'Refused']
df_agg["Monthly_Student_Loan_Payment"] = df_agg["Monthly_Student_Loan_Payment"].str.replace("I am currently not required to make any payments on these loans", "No payment required", case = True)


# arrange student loan categories
Monthly_Student_Loan_Payment_ordering = ["No student loan debt","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","I am currently not required to make any payments on these loans",\
                "Refused","Don't know"]
df_agg.loc[:, ("Monthly_Student_Loan_Payment")] = pd.Categorical(df_agg.loc[:, ("Monthly_Student_Loan_Payment")], categories=Monthly_Student_Loan_Payment_ordering)

# arrange income categories
inc_ordering = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]
df_agg.loc[:, ("income_categories")] = pd.Categorical(df_agg.loc[:, ("income_categories")], categories=inc_ordering)



# aggregate dataframe of 3 analyses below
df1 = df_agg[['Monthly_Student_Loan_Payment','age_categories','income_categories', 'Business_Ownership',]]
df1.to_excel('/Users/Hmurray/Desktop/data/SHED/student_loans/manipulater.xlsx', index=False)

# Replace NaN
df1['Monthly_Student_Loan_Payment'].fillna('No student loan debt', inplace=True)

# value counts
def valuer1(df, var, save=None):
    print()
    print(df1[var].value_counts(normalize=True))
    print()
    (df1[var].value_counts(normalize=True).plot(kind='bar'))
    if save:
        plt.xticks(fontsize=10, rotation=30)
        plt.tight_layout()
        plt.savefig(save)
    # plt.show()

valuer1(df1, 'Business_Ownership', '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership_1.png')
valuer1(df1, 'Monthly_Student_Loan_Payment', '/Users/Hmurray/Desktop/data/SHED/student_loans/Monthly_Student_Loan_Payment_1.png')
valuer1(df1, 'age_categories', '/Users/Hmurray/Desktop/data/SHED/student_loans/age_categories_1.png')
valuer1(df1, 'income_categories', '/Users/Hmurray/Desktop/data/SHED/student_loans/income_categories_1.png')


# debt * age
ct_sl_age = (pd.crosstab(df1['Monthly_Student_Loan_Payment'], df1['age_categories'], normalize='columns')).round(4)*100
ct_sl_age.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_age.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(df1['Monthly_Student_Loan_Payment'], df1['income_categories'], normalize='columns')).round(4)*100
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_inc.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(df1['Monthly_Student_Loan_Payment'], df1['Business_Ownership'], normalize='columns')).round(4)*100
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/ct_sl_eship.csv')
print(ct_sl_eship)


sys.exit()








# rerun analysis by dropping NaN




# aggregate dataframe of 3 analyses below
df2 = df_agg[['Monthly_Student_Loan_Payment','age_categories','income_categories', 'Business_Ownership',]]

# Drop NaN
df2 = df2[df2['Monthly_Student_Loan_Payment'].notna()]
# df['Business_Ownership'].fillna('No student loan debt', inplace=True)
print(df2.head())

def valuer2(df, var, save=None):
    print()
    print(df[var].value_counts(normalize=True).plot(kind='bar'))
    print()
    if save:
        plt.xticks(fontsize=10, rotation=30)
        plt.tight_layout()
        plt.savefig(save)
    # plt.show()

valuer2(df2, 'Business_Ownership', '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership.png')
valuer2(df2, 'Monthly_Student_Loan_Payment', '/Users/Hmurray/Desktop/data/SHED/student_loans/Monthly_Student_Loan_Payment.png')
valuer2(df2, 'age_categories', '/Users/Hmurray/Desktop/data/SHED/student_loans/age_categories.png')
valuer2(df2, 'income_categories', '/Users/Hmurray/Desktop/data/SHED/student_loans/income_categories.png')


# debt * age
ct_sl_age = (pd.crosstab(df2['Monthly_Student_Loan_Payment'], df2['age_categories'], normalize='columns')).round(4)*100
ct_sl_age.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/drafts/ct_sl_age2.csv')
print(ct_sl_age)

# debt * income
ct_sl_inc = (pd.crosstab(df2['Monthly_Student_Loan_Payment'], df2['income_categories'], normalize='columns')).round(4)*100
ct_sl_inc.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/drafts/ct_sl_inc2.csv')
print(ct_sl_inc)

# debt * eship or ownership
ct_sl_eship = (pd.crosstab(df2['Monthly_Student_Loan_Payment'], df2['Business_Ownership'], normalize='index')).round(4)*100
ct_sl_eship.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/drafts/ct_sl_eship2.csv')
print(ct_sl_eship)


