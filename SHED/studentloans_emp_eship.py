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



# pull, subset, add column, and rename stuff
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
df_agg = df_agg[['ppagecat', 'ppinccat6', 'D3A', 'SL4']]
df_agg.rename(columns={"ppagecat": "age_categories", "ppinccat6": "income_categories", "D3A": "Business_Ownership", \
                       "SL4": "Monthly_Student_Loan_Payment"},inplace=True)
df_agg['nan'] = df_agg['Monthly_Student_Loan_Payment']
df_agg['Monthly_Student_Loan_Payment'].fillna('No student loan debt', inplace=True)
df_agg['Monthly_Student_Loan_Payment'] = df_agg['Monthly_Student_Loan_Payment'].str.replace("I am currently not required to make any payments on these loans", "None required", case = True)
df_agg['nan'] = df_agg['nan'].str.replace("I am currently not required to make any payments on these loans", "None required", case = False)
# export the subset df to excel
df_agg.to_excel('/Users/Hmurray/Desktop/data/SHED/student_loans/manipulater.xlsx', index=False)
# define the order of columns
business_ownership = ["For a single company or employer","For yourself or your family business","Refused","Other (Please specify)"]
monthly_payments = ["No student loan debt","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","none required",\
                "Refused","Don't know"]
nan = ["$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","none required",\
                "Refused","Don't know"]
age_categories = ["18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
income_categories = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]



# frequencies and plots function
def valuer1(df, var, order, save=None):
    print()
    df[var] = pd.Categorical(df[var], categories=order, ordered=False)
    print(df[var].value_counts(normalize=True, sort=False))
    print()
    df[var].value_counts(normalize=True, sort=False).plot(kind='bar')
    if save:
        plt.xticks(fontsize=10)
        plt.tight_layout()
        # plt.gcf().subplots_adjust(bottom=0.20)
        plt.savefig(save)
    plt.show()
valuer1(df_agg, 'Business_Ownership', business_ownership, '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership.png')
valuer1(df_agg, 'Monthly_Student_Loan_Payment', monthly_payments, '/Users/Hmurray/Desktop/data/SHED/student_loans/Monthly_Student_Loan_Payment.png')
valuer1(df_agg, 'nan', nan, '/Users/Hmurray/Desktop/data/SHED/student_loans/Monthly_Student_Loan_Payment.png')
valuer1(df_agg, 'age_categories', age_categories, '/Users/Hmurray/Desktop/data/SHED/student_loans/age_categories.png')
valuer1(df_agg, 'income_categories', income_categories, '/Users/Hmurray/Desktop/data/SHED/student_loans/income_categories.png')


# cross tabs
# HOW DO I SAVE EACH CROSSTAB SEPERATELY???
def crosstab_all(dataset, attributelist, save=None,):
    for v in attributelist:
        print()
        name = pd.crosstab(dataset[v],dataset["Business_Ownership"], normalize=True, margins=True)
        print(name)
        print()

attributelist=["Monthly_Student_Loan_Payment",'age_categories','income_categories']
crosstab_all(df_agg, attributelist, '/Users/Hmurray/Desktop/data/SHED/student_loans/xtab.csv')



sys.exit()
