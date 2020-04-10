# data downloaded manually from tab, "Person Income (state and local)" option, "Annual Personal Income by State"
# url: https://apps.bea.gov/regional/downloadzip.cfm

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

# pull BEA employment data
emp = pd.read_csv('/Users/hmurray/Desktop/data/BEA/BEA_data/bea_download/SAEMP25N__ALL_AREAS_1998_2018.csv')

# pull BEA income data
inc = pd.read_csv('/Users/hmurray/Desktop/data/BEA/BEA_data/bea_download/SAINC5N__ALL_AREAS_1998_2019.csv')

# subset using startswith()
emp = emp[emp.columns[pd.Series(emp.columns).str.startswith(('GeoName', 'Description', '2'))]]
inc = inc[inc.columns[pd.Series(inc.columns).str.startswith(('GeoName', 'Description', '2'))]]

# FILTER FUNCTION
def filterer(df):
    df = df[df['GeoName'] == 'United States']
    df.reset_index(inplace=True, drop=True)
    return df
emp = filterer(emp)
inc = filterer(inc)

# Filter for Proprietors employment and Proprietors' income 8/
emp = emp[(emp['Description'] == ' Proprietors employment') | (emp['Description'] == ' Wage and salary employment')]
inc = inc[(inc['Description'] == ' Proprietors\' income 8/') | (inc['Description'] == ' Wages and salaries')]

# Definitions of variables (https://apps.bea.gov/regional/definitions/)
wage_salary = "The remuneration receivable by employees (including corporate officers) from employers for the provision\
 of labor services. It includes commissions, tips, and bonuses; employee gains from exercising stock options; and\
 pay-in-kind. Judicial fees paid to jurors and witnesses are classified as wages and salaries. Wages and salaries are\
  measured before deductions, such as social security contributions, union dues, and voluntary employee contributions to defined contribution pension plans."
wage_salary_emp = "Wage and salary employment, also referred to as wage and salary jobs, measures the average annual\
 number of full-time and part-time jobs in each area by place of work. All jobs for which wages and salaries are paid\
  are counted. Although compensation paid to jurors, expert legal witnesses, prisoners, and justices of the peace\
   (for marriage fees), is counted in wages and salaries, these activities are not counted as jobs in wage and salary\
    employment. Corporate directorships are counted as self-employment. The following description of the sources and\
     methods used in estimating wage and salary employment is divided into two sections: Employment in industries\
      covered by unemployment insurance (UI) programs, and employment in industries not covered by UI."
proprietors_employment = "Consists of farm proprietors employment and nonfarm proprietors employment."
proprietors_income = "Proprietors' income with inventory valuation and capital consumption adjustments is the\
 current-production income (including income in kind) of sole proprietorships, partnerships,\
 and tax-exempt cooperatives. Corporate directors' fees are included in proprietors' income.\
 Proprietors' income includes the interest income received by financial partnerships and the\
 net rental real estate income of those partnerships primarily engaged in the real estate business."


# show definitions
print()
print(proprietors_employment)
print()
print(proprietors_income)
print()

# drop unnecessary columns, transpose, reset index, rename columns, and sum quarterly values of income
emp = emp.drop(['GeoName', 'Description'], axis=1).transpose().reset_index(drop=False).rename(columns={'index':'year', 1:'wage_salary_emp', 2:'prop_emp'})
inc = inc.drop(['GeoName', 'Description'], axis=1).transpose().reset_index(drop=False).rename(columns={'index':'year', 11: 'wage_salary', 15:'prop_inc'})

# merge dataframes
df = pd.merge(emp, inc, on='year')

# change to numeric
def numberer(df, col):
    for x in col:
        df[x] = pd.to_numeric((df[x]))
col = ('wage_salary_emp', 'prop_emp', 'wage_salary', 'prop_inc')
numberer(df, col)

# calculate average income
df['avg_inc'] = ((df['wage_salary']/df['wage_salary_emp'])* 1000)
df['avg_prop_inc'] = ((df['prop_inc']/df['prop_emp'])* 1000)
print(df)

# plot avg proprietor income
df.plot(x='year', y=['avg_prop_inc', 'avg_inc'])
plt.title('Average Income of Employees and Proprietors in the United States')

# export df and plot
df.to_excel('/Users/hmurray/Desktop/data/BEA/BEA_Data/avg_prop_inc.xlsx')
plt.savefig('/Users/hmurray/Desktop/data/BEA/BEA_Data/plot_avg_prop_inc.png')


