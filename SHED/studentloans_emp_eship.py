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



# pull, subset, and rename
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)
df_agg = df_agg[['ppagecat', 'ppinccat6', 'D3A', 'SL4']]
df_agg.rename(columns={"ppagecat": "age_categories", "ppinccat6": "income_categories", "D3A": "Business_Ownership", \
                       "SL4": "Monthly_Student_Loan_Payment"},inplace=True)
df_agg["Monthly_Student_Loan_Payment"] = df_agg["Monthly_Student_Loan_Payment"].str.replace("I am currently not required to make any payments on these loans",\
                                                                                            "none required", case = True)


# export the subset df to excel
# df_agg.to_excel('/Users/Hmurray/Desktop/data/SHED/student_loans/manipulater.xlsx', index=False)

df_agg["Business_Ownership"] = df_agg["Business_Ownership"].astype('category')

# frequencies and plots function. Can pass through 3 arguments but unable to pass argument for categories
def valuer1(df, var, order, save=None):
    print()
    df[var] = pd.Categorical(df[var], categories=order, ordered=False)
    print(df[var].value_counts(normalize=True, sort=False))
    print()
    df[var].value_counts(normalize=True, sort=False).plot(kind='bar')
    if save:
        plt.xticks(fontsize=10)
        plt.tight_layout()
        plt.savefig(save)
    plt.show()

business_ownership = ["For a single company or employer","For yourself or your family business","Refused","Other (Please specify)"]
monthly_payments = ["No student loan debt","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","I am currently not required to make any payments on these loans",\
                "Refused","Don't know"]
age_categories = ["18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
income_categories = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]

valuer1(df_agg, 'Business_Ownership', business_ownership, '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership.png')
valuer1(df_agg, 'Monthly_Student_Loan_Payment', monthly_payments, '/Users/Hmurray/Desktop/data/SHED/student_loans/Monthly_Student_Loan_Payment.png')
valuer1(df_agg, 'age_categories', age_categories, '/Users/Hmurray/Desktop/data/SHED/student_loans/age_categories.png')
valuer1(df_agg, 'income_categories', income_categories, '/Users/Hmurray/Desktop/data/SHED/student_loans/income_categories.png')


sys.exit()


# attempting to order categories of frequencies and plots. Example of one of the four below:
print(df_agg.income_categories.value_counts(normalize=True).loc[["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]])
df_agg.income_categories.value_counts().loc[["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]].plot(kind="bar")
plt.xticks(fontsize=10, rotation=30)
plt.tight_layout()
plt.show()
