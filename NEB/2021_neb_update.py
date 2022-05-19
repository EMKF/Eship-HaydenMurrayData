import sys
import pandas as pd
import kauffman.data as kauffman
import matplotlib.pyplot as plt
import datetime
import numpy as np
from textwrap import wrap
from matplotlib.dates import date2num

pd.set_option('max_columns', 1000)
pd.set_option('max_info_columns', 1000)
pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 30000)
pd.set_option('max_colwidth', 4000)
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.options.mode.chained_assignment = None

def data_create():
    # pull 2021 neb data download
    df = pd.read_csv('s3://emkf.data.research/indicators/neb/data_outputs/neb_download.csv')
    # filter df for US
    df = df[(df['name'] == 'United States')].reset_index(drop=True)
    # subset df by necessary columns
    df = df[['fips', 'name', 'year', 'actualization', 'bf_per_capita', 'velocity', 'newness', 'index']]
    # rename columns
    df = df.rename(columns={'bf_per_capita': 'rate_new_employer_business', 'index': 'NEBAS_index'})
    return df

def table_1(df):
    # save df table locally
    df.to_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/table_1.xlsx')
    return df

def ba_reference():
    # import ba numbers
    ba = pd.read_excel('/Users/hmurray/Desktop/NEB/2021/data/plots/ba_reference.xlsx')
    # rename columns
    ba = ba.rename(columns={'BA_BA': 'Business Applications', 'BF_SBF8Q': 'Employer Business Formations'})
    ba.plot(x='time', y=['Business Applications', 'Employer Business Formations'])
    plt.title("\n".join(wrap("FIGURE 1: Between 2005 and 2021, business applications increased from 2,509,369"
                             " to 5,385,721 and employer business formations increased from 480,566 to 493,185", 62)))
    plt.xlabel('Year')
    plt.ylabel('Business Applications and New Employer Business Formations')
    # axes = plt.gca()
    plt.tight_layout()
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/fig1_ba_plot.png')
    plt.show()

def actualization_plots(df):
    df.plot(x='year', y=['actualization'])
    plt.title("\n".join(wrap("In 2005, approximately one in five new businesses across the United States"
                             " became an employer (19.15%). In 2021, this has decreased to less than one in ten new"
                             " businesses becoming an employer (9.16%).", 62)))
    plt.xlabel('Year')
    plt.ylabel('Rate of New Employer Business Actualization')
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, .35])
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/national_actualization.png')
    plt.show()
    return df

def rate_new_emp_bus_plots(df):
    df.plot(x='year', y=['rate_new_employer_business'])
    plt.title("\n".join(wrap("In 2005, approximately 160 new employer businesses were formed for every"
                             " 100,000 people compared to 120 in 2020.", 62)))
    plt.xlabel('Year')
    plt.ylabel('Rate of New Employer Business')
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, .20])
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/national_rate_new_emp.png')
    plt.show()
    return df

def velocity_plots(df):
    df.plot(x='year', y=['velocity'])
    plt.title("\n".join(wrap("In 2005, it took roughly one and a half quarters for a new business to become an employer"
                             ", compared to over two quarters in 2017.", 62)))
    plt.xlabel('Year')
    plt.ylabel('Time in quarters between application and first hire')
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, 2.5])
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/national_velocity.png')
    plt.show()
    return df

def newness_plots(df):
    df.plot(x='year', y=['newness'])
    plt.title("\n".join(wrap("Figure 5: In 2006, new employer firms made up about 9% of all employers, "
                             "compared to about 7% in 2019.", 62)))
    plt.xlabel('Year')
    plt.ylabel('Percent of all employer firms that are new employer businesses')
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, .12])
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/national_newness.png')
    plt.show()
    return df


def nebas_index_plots(df):
    df.plot(x='year', y=['NEBAS_index'])
    plt.title("\n".join(wrap("The NEBAS Index has decreased every year for which data are available,"
                             " except for 2011-2012, when it increased from .80 to .81.", 62)))
    plt.xlabel('Year')
    plt.ylabel('NEBAS Index')
    axes = plt.gca()
    plt.tight_layout()
    axes.set_ylim([0, 1.5])
    plt.savefig('/Users/hmurray/Desktop/NEB/2021/data/plots/national_nebas_index.png')
    plt.show()
    return df

if __name__ == '__main__':
    df = data_create()
    df = table_1(df)
    # ba_reference()
    df = actualization_plots(df)
    df = rate_new_emp_bus_plots(df)
    df = velocity_plots(df)
    df = newness_plots(df)
    df = nebas_index_plots(df)
    print(df)