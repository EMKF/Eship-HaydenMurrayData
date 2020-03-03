import os
import sys
import time
import zipfile
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# KESE - OPPORTUNITY SHARE OF ENTREPRENEURS
kese = pd.read_csv('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/original_pull/KESE_opp.csv')

# United States OSE
kese_us = kese[51:52]
kese_us = kese_us.iloc[:,:26]
kese_us.to_excel('/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/kese_opp_US.xlsx', index=False)
print(kese_us)

# plot US OSE
df = kese_us.transpose().iloc[3: ].rename(columns={51:'ose'}).assign(year=range(1996, 2019)).reset_index(drop=True)



# quick_plot(df)
matplotlib_plot(df, 'ose')
matplotlib_plot(df, 'ose', '/Users/hmurray/Desktop/Data_Briefs/ASE/MO_ASE_Reasons_Own_Business/Data_Reasons_Own_Business/ose_plot.png')


# plot 1
def quick_plot(df):
    df.plot.line('year', 'ose')
    plt.show()


def matplotlib_plot_gender1(df):
    print(df.head())
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot('year', 'ose_women', data=df, label='Women')
    ax.plot('year', 'ose_men', data=df, label='Men')
    ax.set_ylim([.65, .95])
    ax.set_xticks(range(1998, 2019, 2))
    ax.set_title('Opportunity Share of New Entrepreneurs')
    plt.legend()
    plt.show()

def kese_gender_plotter_ex1():
    kese_gender.\
        transpose().\
        iloc[5:].\
        rename(columns={53:'ose_men', 54: 'ose_women'}).\
        assign(year=range(1998, 2019)).\
        reset_index(drop=True).\
        pipe(matplotlib_plot_gender1)
# kese_gender_plotter_ex1()

def matplotlib_plot_gender2(df):
    # todo: fancier ways
    print(df.head())
    # sys.exit()
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    for gender in ['Male', 'Female']:
        ax.plot('year', 'ose', data=df.query('gender == "{}"'.format(gender)), label=gender)
    ax.set_ylim([.65, .95])
    ax.set_xticks(range(1998, 2019, 2))
    ax.set_title('Opportunity Share of New Entrepreneurs')
    plt.legend()
    plt.show()

def kese_data_gender_prep(gender):
    if gender == "men":
        return kese_gender.\
            transpose().\
            iloc[5:, 0].\
            pipe(pd.DataFrame).\
            rename(columns={53:'ose'}).\
            assign(year=range(1998, 2019), gender='Male').\
            reset_index(drop=True)
    else:
        return kese_gender.\
            transpose().\
            iloc[5:, 1].\
            pipe(pd.DataFrame).\
            rename(columns={54:'ose'}).\
            assign(year=range(1998, 2019), gender='Female').\
            reset_index(drop=True)
kese_data_gender_prep('men').\
    append(kese_data_gender_prep('women')).\
    pipe(matplotlib_plot_gender2)
print(df)

# matplotlib_plot_gender1(df)
# matplotlib_plot_gender2(df)