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
df = data[['ppagecat', 'D3A', 'SL3', 'SL4', 'SL6']]

# rename columns
df.rename(columns={"ppagecat": "age_categories", "D3A": "Business_Ownership", "SL3": "Total_Student_Loans", "SL4": "Monthly_Student_Loan_Payment" },inplace=True)

# rename strings
df["Monthly_Student_Loan_Payment"] = df["Monthly_Student_Loan_Payment"].str.replace\
    ("I am currently not required to make any payments on these loans", "No payment required", case = True)
df['Business_Ownership'] = df['Business_Ownership'].str.replace("For a single company or employer", "Employed", case = True)
df['Business_Ownership'] = df['Business_Ownership'].str.replace("For yourself or your family business", "Family- or Self-Employed", case = True)

# quick value count
print(df['Total_Student_Loans'].value_counts(normalize=True))

# fill NaN with no student loan debt
df['Total_Student_Loans'].fillna('No student loan debt', inplace=True)
print(df.head())

# order categories
age = ["18-24", "25-34", "35-44", "45-54", "55-64", "65-74", "75+"]
business_ownership = ["Employed","Family- or Self-Employed"]
total = ["No student loan debt", "Less than $5,000", "$5,000 to $9,999","$10,000 to $14,999","$15,000 to $19,999","$20,000 to $24,999",\
        "$25,000 to $29,999","$30,000 to $39,999","$40,000 to $49,999","$50,000 to $74,999", "$75,000 to $99,999", "$100,000 or above"]
monthly = ["No student loan debt","None required","$1 to $49","$50 to $99","$100 to $199","$200 to $299","$300 to $399",\
                "$400 to $499","$500 to $749","$750 to $999","$1,000 or above"]
behind = ["Yes","No"]

# set the order
df.loc[:, ("age_categories")] = pd.Categorical(df.loc[:, ("age_categories")], categories=age)
df.loc[:, ("Business_Ownership")] = pd.Categorical(df.loc[:, ("Business_Ownership")], categories=business_ownership)
df.loc[:, ("Total_Student_Loans")] = pd.Categorical(df.loc[:, ("Total_Student_Loans")], categories=total)
df.loc[:, ("Monthly_Student_Loan_Payment")] = pd.Categorical(df.loc[:, ("Monthly_Student_Loan_Payment")], categories=monthly)
df.loc[:, ("SL6")] = pd.Categorical(df.loc[:, ("SL6")], categories=behind)
print(df['age_categories'].value_counts(normalize=True, sort=False))

# value counts
no_debt = df['Total_Student_Loans'].value_counts(normalize=True, sort=False)
no_debt = pd.DataFrame(no_debt)
no_debt = no_debt.iloc[0,0]

# plot
def valuer1(df, var, save=None):
    print()
    print(df[var].value_counts(normalize=True))
    print()
    (df[var].value_counts(normalize=True).plot(kind='bar'))
    if save:
        plt.xticks(fontsize=10, rotation=0)
        plt.tight_layout()
        plt.savefig(save)

valuer1(df, 'Business_Ownership', '/Users/Hmurray/Desktop/data/SHED/student_loans/Business_Ownership_1.png')
valuer1(df, 'SL6', '/Users/Hmurray/Desktop/data/SHED/student_loans/SL6.png')


# calculate % no debt for each category
status_no_debt = df.groupby('Business_Ownership').Total_Student_Loans.value_counts(normalize=True).unstack(0)
print(status_no_debt)
status_no_debt.to_excel('/Users/hmurray/Desktop/data/SHED/student_loans/status_no_debt.xlsx')

# calculate % with debt
# total_debt
total_debt = 100 - (100*no_debt)
print(total_debt)

# employee debt
emp_debt = status_no_debt.iloc[11, 0]
emp_debt = 100 - (100*emp_debt)
print(emp_debt)

# entrepreneur debt
ent_debt = status_no_debt.iloc[11, 1]
ent_debt = 100 - (100*ent_debt)
print(ent_debt)

# plot % with debt for labor status
top = [('Employed',20.51),('Family- or Self-Employed',11.31)]
labels, ys = zip(*top)
xs = np.arange(len(labels))
width = .5
plt.bar(xs, ys, width, align='center')
plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(np.arange(0, 50, 5))
plt.title('Percent with Student Loan Debt')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('/Users/hmurray/Desktop/data/SHED/student_loans/plot_status_with_debt.png')

# Plot Behind by Ownership
print(df.groupby('Business_Ownership').SL6.value_counts(normalize=True).unstack(0))
df.groupby('Business_Ownership').SL6.value_counts(normalize=True).unstack(0).plot(kind='bar')
plt.xticks(fontsize=10, rotation=90)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.title('Are you behind behind or in collections for your student loans?')
plt.savefig('/Users/hmurray/Desktop/data/SHED/student_loans/behind.png')

# overall total student debt
print(df['Total_Student_Loans'].value_counts(normalize=True))
print(df['Monthly_Student_Loan_Payment'].value_counts(normalize=True))
