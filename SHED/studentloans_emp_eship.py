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
df_agg = pd.read_csv('/Users/hmurray/Downloads/public2018.csv',header=0,encoding = 'unicode_escape', dtype={'user_id': int}, low_memory=False)

# subset
df_agg = df_agg[['ppagecat', 'ppinccat6', 'D3A', 'SL3', 'SL4']]

# rename
df_agg.rename(columns={"ppagecat": "age_categories", "ppinccat6": "income_categories", "D3A": "Business_Ownership", "SL3": "Total_student_loan", "SL4": "Monthly_Student_Loan_Payment"},inplace=True)

# fill NaN
df_agg['Monthly_Student_Loan_Payment'].fillna('No student loan debt', inplace=True)
df_agg['Total_student_loan'].fillna('No student loan debt', inplace=True)

# replace strings
df_agg['Monthly_Student_Loan_Payment'] = df_agg['Monthly_Student_Loan_Payment'].str.replace("I am currently not required to make any payments on these loans", "None required", case = True)

# turn garbage categories to NaN
def disposer(df, var):
    df[var].replace('Refused', np.nan, inplace=True)
    df[var].replace('Other (Please specify)', np.nan, inplace=True)
    df[var].replace('Don\'t know', np.nan, inplace=True)
    return df
disposer(df_agg, 'Monthly_Student_Loan_Payment')
disposer(df_agg, 'Total_student_loan')

# export the subset df to excel
df_agg.to_excel('/Users/Hmurray/Desktop/data/SHED/student_loans/manipulater.xlsx', index=False)

# define the order of columns
business_ownership = ["For a single company or employer","For yourself or your family business"]
monthly_payments = ["No student loan debt","None required","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above","Refused","Don't know"]
monthly_nan = ["$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above"]
total = ["No student loan debt", "Less than $5,000", "$5,000 to $9,999","$10,000 to $14,999","$15,000 to $19,999","$20,000 to $24,999",\
                "$25,000 to $29,999","$30,000 to $39,999","$40,000 to $49,999","$50,000 to $74,999", "$75,000 to $99,999", "$100,000 or above"]
total_nan = ["Less than $5,000", "$5,000 to $9,999","$10,000 to $14,999","$15,000 to $19,999","$20,000 to $24,999",\
                "$25,000 to $29,999","$30,000 to $39,999","$40,000 to $49,999","$50,000 to $74,999", "$75,000 to $99,999", "$100,000 or above"]
age_categories = ["18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
income_categories = ["<$25,000","$25-49,999","$50-74,999","$75-99,999","$100-149,999","$150,000+"]



# frequencies and plots function
def valuer(df, var, order, title, save=None):
    print()
    df[var] = pd.Categorical(df[var], categories=order, ordered=False)
    print(df[var].value_counts(normalize=True, sort=False))
    print()
    df[var].value_counts(normalize=True, sort=False).plot(kind='bar')
    if save:
        plt.xticks(fontsize=10, rotation=90)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.title(title)
        # plt.gcf().subplots_adjust(bottom=0.20)
        plt.savefig(save)
    plt.show()
valuer(df_agg, 'Business_Ownership', business_ownership, 'Labor Status', '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership.png')
valuer(df_agg, 'Monthly_Student_Loan_Payment', monthly_payments, 'Average Monthly Student Loan Payment', '/Users/Hmurray/Desktop/data/SHED/student_loans/monthly.png')
valuer(df_agg, 'Monthly_Student_Loan_Payment', monthly_nan, 'Average Monthly Student Loan Payment','/Users/Hmurray/Desktop/data/SHED/student_loans/monthly_nan.png')
valuer(df_agg, 'Total_student_loan', total, 'Total Student Loan Debt','/Users/Hmurray/Desktop/data/SHED/student_loans/total.png')
valuer(df_agg, 'Total_student_loan', total_nan, 'Total Student Loan Debt','/Users/Hmurray/Desktop/data/SHED/student_loans/total_nan.png')
valuer(df_agg, 'age_categories', age_categories, 'Age','/Users/Hmurray/Desktop/data/SHED/student_loans/age_categories.png')
valuer(df_agg, 'income_categories', income_categories, 'Income', '/Users/Hmurray/Desktop/data/SHED/student_loans/income_categories.png')


# cross tabs
# HOW DO I SAVE EACH CROSSTAB SEPERATELY???
def crosstab_all(dataset, attributelist):
    for v in var:
        print()
        name = pd.crosstab(dataset[v],dataset["Business_Ownership"], normalize=True, margins=True)
        pd.DataFrame(name)
        print(name)


total_monthly = (pd.crosstab(df_agg['Monthly_Student_Loan_Payment'], df_agg['Total_student_loan'], normalize='columns')).round(4)*100
total_monthly.to_csv('/Users/Hmurray/Desktop/data/SHED/student_loans/total_monthly.csv')
print(total_monthly)


var=['Monthly_Student_Loan_Payment','Total_student_loan','age_categories','income_categories']
crosstab_all(df_agg, var)



sys.exit()
